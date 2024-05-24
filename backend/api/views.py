from django.shortcuts import render
from rest_framework import generics
from .models import TestModel
from .serializers import TestModelSerializers
# Create your views here.

class TestModelListCreated(generics.ListCreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializers

class TestModelRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestModelSerializers