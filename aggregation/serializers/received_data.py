from rest_framework import serializers

from aggregation.models import ReceivedData


class ReceivedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivedData
        fields = (
            'csv_file',
        )
