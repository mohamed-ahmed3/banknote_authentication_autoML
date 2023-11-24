from rest_framework import serializers
from .models import *


class DatasetModelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = DatasetModels
        fields = [
            'file',
            'serialized_model'
        ]
