# Generated by Django 2.2.12 on 2020-05-31 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='number',
            field=models.CharField(max_length=20, verbose_name='Phone Number'),
        ),
    ]
