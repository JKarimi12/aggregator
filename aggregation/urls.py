from django.urls import path

from aggregation.views import ReceiveDataView, DownloadDataView

urlpatterns = [
    path('upload/', ReceiveDataView.as_view()),
    path('download/', DownloadDataView.as_view()),
]
