from ..models.properties import *
from rest_framework import serializers


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = '__all__'
