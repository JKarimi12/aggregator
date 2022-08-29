from rest_framework.generics import CreateAPIView

from aggregation.serializers import ReceivedDataSerializer


class ReceiveDataView(CreateAPIView):
    serializer_class = ReceivedDataSerializer
