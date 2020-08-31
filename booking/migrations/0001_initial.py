# Generated by Django 2.2.12 on 2020-05-27 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('description', models.CharField(max_length=150, null=True)),
                ('price', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('category', models.CharField(choices=[('Grm', 'Grooming'), ('b&b', 'Bed and Bath'), ('Photo', 'Photography'), ('Ao', 'Add-Ons')], default='Grm', max_length=21)),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(default=1, max_length=15)),
                ('paid', models.BooleanField(default=False)),
                ('dateMade', models.DateTimeField(auto_now_add=True, null=True)),
                ('dateBooked', models.DateTimeField(null=True)),
                ('timeBooked', models.TimeField(null=True)),
                ('pet', models.ManyToManyField(to='pets.Pet')),
                ('services', models.ManyToManyField(to='booking.Services')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
    ]