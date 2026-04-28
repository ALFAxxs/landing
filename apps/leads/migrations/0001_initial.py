from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name',       models.CharField(max_length=150, verbose_name='Ism')),
                ('phone',      models.CharField(max_length=30,  verbose_name='Telefon')),
                ('email',      models.EmailField(verbose_name='Email')),
                ('message',    models.TextField(blank=True, verbose_name='Xabar')),
                ('status',     models.CharField(
                    choices=[
                        ('new',        "🆕 Yangi"),
                        ('seen',       "👁 Ko'rildi"),
                        ('processing', '🔄 Ishlanmoqda'),
                        ('done',       '✅ Yakunlandi'),
                        ('cancelled',  '❌ Bekor qilindi'),
                    ],
                    default='new', max_length=20, verbose_name='Status'
                )),
                ('note',       models.TextField(blank=True, verbose_name='Admin eslatmasi')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yuborilgan vaqt')),
                ('updated_at', models.DateTimeField(auto_now=True,     verbose_name='Yangilangan vaqt')),
            ],
            options={
                'verbose_name':        'Murojaat',
                'verbose_name_plural': 'Murojaatlar',
                'ordering':            ['-created_at'],
            },
        ),
    ]
