# Generated by Django 3.1.1 on 2020-09-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20200913_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='address',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AlterField(
            model_name='detail',
            name='detail_text',
            field=models.CharField(default=None, max_length=300),
        ),
        migrations.AlterField(
            model_name='detail',
            name='e_mail',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]
