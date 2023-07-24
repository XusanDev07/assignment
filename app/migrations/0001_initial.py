# Generated by Django 4.2.3 on 2023-07-18 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doktor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=128)),
                ('familiya', models.CharField(max_length=128)),
                ('telegramnikname', models.CharField(max_length=1028)),
                ('yonalishi', models.CharField(max_length=128)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Xamshira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=128)),
                ('familiya', models.CharField(max_length=128)),
                ('telegramnikname', models.CharField(max_length=1028)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Xona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('odam_soni', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=128)),
                ('familiya', models.CharField(max_length=128)),
                ('phone', models.IntegerField()),
                ('xona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.xona')),
            ],
        ),
    ]