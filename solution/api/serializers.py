from rest_framework import serializers

from solution.models import *


class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'