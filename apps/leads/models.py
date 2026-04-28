# apps/leads/models.py

from django.db import models


class Lead(models.Model):
    STATUS_CHOICES = [
        ('new',        '🆕 Yangi'),
        ('seen',       '👁 Ko\'rildi'),
        ('processing', '🔄 Ishlanmoqda'),
        ('done',       '✅ Yakunlandi'),
        ('cancelled',  '❌ Bekor qilindi'),
    ]

    name       = models.CharField(max_length=150, verbose_name="Ism")
    phone      = models.CharField(max_length=30,  verbose_name="Telefon")
    email      = models.EmailField(verbose_name="Email")
    message    = models.TextField(blank=True, verbose_name="Xabar")
    status     = models.CharField(
        max_length=20, choices=STATUS_CHOICES,
        default='new', verbose_name="Status"
    )
    note       = models.TextField(blank=True, verbose_name="Admin eslatmasi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yuborilgan vaqt")
    updated_at = models.DateTimeField(auto_now=True,     verbose_name="Yangilangan vaqt")

    class Meta:
        verbose_name        = "Murojaat"
        verbose_name_plural = "Murojaatlar"
        ordering            = ['-created_at']

    def __str__(self):
        return f"{self.name} — {self.phone} ({self.get_status_display()})"

    @property
    def is_new(self):
        return self.status == 'new'
