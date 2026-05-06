# apps/leads/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
from django.utils import timezone
from django.db.models import Q
import csv

from apps.leads.models import Lead
from apps.leads.forms import LeadForm, LeadStatusForm


# ===== LANDING PAGE =====

def index(request):
    if request.method == 'POST':
        # Honeypot — bot bu maydonni to'ldiradi, inson to'ldirmaydi
        if request.POST.get('website', '').strip():
            # Botga muvaffaqiyat ko'rsatamiz, lekin saqlamaymiz
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            return redirect('/?success=1')

        # Rate limiting — bir IP dan 1 soatda max 5 ta murojaat
        ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')).split(',')[0].strip()
        from django.core.cache import cache
        cache_key = f"lead_limit_{ip}"
        count = cache.get(cache_key, 0)
        if count >= 5:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': {'phone': ['Juda kop urinish. Biroz kuting.']}})
            return redirect('/?success=1')
        cache.set(cache_key, count + 1, 3600)

        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            messages.success(request, 'Murojaatingiz qabul qilindi!')
            return redirect('/?success=1')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = LeadForm()

    return render(request, 'index.html', {'form': form})


# ===== ADMIN PANEL =====

def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_leads')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_staff:
            login(request, user)
            return redirect('admin_leads')
        messages.error(request, 'Login yoki parol noto\'g\'ri.')
    return render(request, 'admin/login.html')


def admin_logout(request):
    logout(request)
    return redirect('admin_login')


@login_required
def admin_leads(request):
    qs = Lead.objects.all()

    # Filterlar
    status = request.GET.get('status', '')
    search = request.GET.get('q', '')
    date_from = request.GET.get('date_from', '')
    date_to   = request.GET.get('date_to', '')

    if status:
        qs = qs.filter(status=status)
    if search:
        qs = qs.filter(Q(name__icontains=search) | Q(phone__icontains=search) | Q(email__icontains=search))
    if date_from:
        qs = qs.filter(created_at__date__gte=date_from)
    if date_to:
        qs = qs.filter(created_at__date__lte=date_to)

    # Statistika
    stats = {
        'total':      Lead.objects.count(),
        'new':        Lead.objects.filter(status='new').count(),
        'processing': Lead.objects.filter(status='processing').count(),
        'done':       Lead.objects.filter(status='done').count(),
    }

    return render(request, 'admin/leads.html', {
        'leads':      qs,
        'stats':      stats,
        'selected_status': status,
        'query':      search,
        'date_from':  date_from,
        'date_to':    date_to,
        'statuses':   Lead.STATUS_CHOICES,
    })


@login_required
def admin_lead_detail(request, pk):
    lead = get_object_or_404(Lead, pk=pk)

    # Ko'rildi deb belgilash
    if lead.status == 'new':
        lead.status = 'seen'
        lead.save(update_fields=['status', 'updated_at'])

    if request.method == 'POST':
        form = LeadStatusForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.success(request, 'Status yangilandi.')
            return redirect('admin_lead_detail', pk=pk)
    else:
        form = LeadStatusForm(instance=lead)

    return render(request, 'admin/lead_detail.html', {
        'lead': lead,
        'form': form,
    })


@login_required
@require_POST
def admin_lead_status(request, pk):
    """AJAX status o'zgartirish"""
    lead = get_object_or_404(Lead, pk=pk)
    new_status = request.POST.get('status')
    valid = [s[0] for s in Lead.STATUS_CHOICES]
    if new_status in valid:
        lead.status = new_status
        lead.save(update_fields=['status', 'updated_at'])
        return JsonResponse({'success': True, 'status': lead.get_status_display()})
    return JsonResponse({'success': False}, status=400)


@login_required
def admin_export_csv(request):
    """Barcha murojaatlarni CSV ga export qilish"""
    response = HttpResponse(content_type='text/csv; charset=utf-8')
    response['Content-Disposition'] = f'attachment; filename="murojaatlar_{timezone.now().strftime("%Y%m%d")}.csv"'
    response.write('\ufeff')  # BOM for Excel

    writer = csv.writer(response)
    writer.writerow(['#', 'Ism', 'Telefon', 'Email', 'Xabar', 'Status', 'Sana'])

    for i, lead in enumerate(Lead.objects.all(), 1):
        writer.writerow([
            i,
            lead.name,
            lead.phone,
            lead.email,
            lead.message,
            lead.get_status_display(),
            lead.created_at.strftime('%d.%m.%Y %H:%M'),
        ])

    return response