# apps/leads/forms.py

from django import forms
from apps.leads.models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model  = Lead
        fields = ['name', 'phone', 'email', 'message']
        widgets = {
            'name':    forms.TextInput(attrs={'placeholder': 'Ismingiz', 'class': 'form-input'}),
            'phone':   forms.TextInput(attrs={'placeholder': '+998 __ ___ __ __', 'class': 'form-input', 'type': 'tel'}),
            'email':   forms.EmailInput(attrs={'placeholder': 'email@example.com', 'class': 'form-input'}),
            'message': forms.Textarea(attrs={'placeholder': 'Savolingiz yoki xabaringiz...', 'class': 'form-textarea', 'rows': 4}),
        }
        labels = {
            'name':    'Ism *',
            'phone':   'Telefon *',
            'email':   'Email *',
            'message': 'Xabar (ixtiyoriy)',
        }
        error_messages = {
            'name':  {'required': 'Iltimos, ismingizni kiriting.'},
            'phone': {'required': 'Iltimos, telefon raqamingizni kiriting.'},
            'email': {
                'required': 'Iltimos, email manzilingizni kiriting.',
                'invalid':  'Email manzil noto\'g\'ri formatda.',
            },
        }


class LeadStatusForm(forms.ModelForm):
    class Meta:
        model  = Lead
        fields = ['status', 'note']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'note':   forms.Textarea(attrs={'rows': 3, 'class': 'form-textarea', 'placeholder': 'Izoh...'}),
        }
        labels = {
            'status': 'Status',
            'note':   'Admin eslatmasi',
        }
