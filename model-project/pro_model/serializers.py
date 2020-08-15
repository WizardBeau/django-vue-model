from rest_framework import serializers
from pro_model import models

class TestSerializer(serializers.Serializer):
    class Meta:
        fields = "__all__"
        model = models.Test