# Generated by Django 3.2.14 on 2022-07-14 10:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReceivedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('csv_file', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['csv'], message='فرمت فایل باید csv باشد.')], verbose_name='فایل csv آپلود شده')),
            ],
            options={
                'verbose_name': 'فایل آپلود شده',
                'verbose_name_plural': 'فایل\u200cهای آپلود شده',
            },
        ),
    ]