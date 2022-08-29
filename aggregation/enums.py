from urllib.parse import urljoin

from django.conf import settings
import os

RECEIVED_DATA_CACHE_KEY = 'received_data'

RESULT_FILE_NAME = os.path.join(settings.MEDIA_ROOT, 'reserved/aggregated_result.csv')

RESULT_FILE_URL = urljoin(settings.HOST_URL, 'media/reserved/aggregated_result.csv')
