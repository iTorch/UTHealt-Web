# Generated by Django 3.2.6 on 2021-08-16 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0004_signosvitales_ritmo_cardiaco'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signosvitales',
            old_name='peso_diario',
            new_name='pasos_diario',
        ),
    ]