from rest_framework import serializers
from .models import update_table, history_table
import datetime
from django.utils import timezone

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = update_table
        fields = ('ph', 'alcohol_content', 'temperature', 'volatile_acid')

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = history_table
        fields = ('ph', 'alcohol_content', 'temperature', 'volatile_acid')

