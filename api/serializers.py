from rest_framework import serializers
from .models import fruitwine_table

class mySerializer(serializers.ModelSerializer):
    class Meta:
        model = fruitwine_table
        fields = ('ph', 'alcohol_content', 'temperature', 'volatile_acid')