from django.shortcuts import render
from rest_framework import viewsets
from .serializers import mySerializer
from rest_framework import generics
from .models import fruitwine_table

# Create your views here.

class UploadData(generics.CreateAPIView):
    model = fruitwine_table
    serializer_class = mySerializer

class result_list(generics.ListAPIView):

    serializer_class = mySerializer

    def get_queryset(self):
        return fruitwine_table.objects.all()