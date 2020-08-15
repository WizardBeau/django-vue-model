from django.shortcuts import render
from rest_framework import viewsets
from pro_model import serializers, models
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.

class TestViewSet(viewsets.ModelViewSet):
    queryset = models.Test.objects.all()
    serializer_class = serializers.TestSerializer

    @action(methods=['get'], detail=False)
    def get_all_test(self, request):
        return Response(self.serializer_class)