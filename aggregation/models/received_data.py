from django.core.validators import FileExtensionValidator
from django.db import models

from aggregation.tasks import generate_result_csv


class ReceivedData(models.Model):

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ ایجاد',
    )

    csv_file = models.FileField(
        verbose_name='فایل csv آپلود شده',
        validators=[FileExtensionValidator(
            allowed_extensions=['csv'],
            message='فرمت فایل باید csv باشد.'
        )]
    )

    class Meta:
        verbose_name = 'فایل آپلود شده'
        verbose_name_plural = 'فایل‌های آپلود شده'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
        generate_result_csv.delay(self.csv_file.path)
