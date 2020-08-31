# Generated by Django 2.2.12 on 2020-05-27 03:01

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=40, unique=True, verbose_name='email')),
                ('first_name', models.TextField(max_length=30)),
                ('last_name', models.TextField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone Number')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, null=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('waiver', models.BooleanField(default=True, verbose_name='I agree')),
            ],
            options={
                'verbose_name_plural': 'Accounts',
            },
        ),
    ]
