from rest_framework import serializers

from .models import Company, Event


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('title', 'description', 'address', 'postcode')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('title', 'description', 'image', 'date')
