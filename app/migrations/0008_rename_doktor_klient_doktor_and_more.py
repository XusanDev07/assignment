# Generated by Django 4.2.3 on 2023-07-19 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_klient_xamshira'),
    ]

    operations = [
        migrations.RenameField(
            model_name='klient',
            old_name='doktor',
            new_name='Doktor',
        ),
        migrations.RenameField(
            model_name='klient',
            old_name='xamshira',
            new_name='Xamshira',
        ),
        migrations.RenameField(
            model_name='klient',
            old_name='xona',
            new_name='Xona',
        ),
    ]
