from rest_framework import serializers
from .models import URL

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = '__all__'
    
    def validate(self, data):
        if not data['exact_url']:
            raise serializers.ValidationError('No exact_url field')
        return data

