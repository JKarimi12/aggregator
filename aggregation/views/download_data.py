from django.http import HttpResponseRedirect
from rest_framework.generics import GenericAPIView

from aggregation.enums import RESULT_FILE_URL


class DownloadDataView(GenericAPIView):

    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(redirect_to=RESULT_FILE_URL)
