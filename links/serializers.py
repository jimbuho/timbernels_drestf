from rest_framework import serializers

from .validators import TitleValidator
from .models import Link

class LinkSerializer(serializers.ModelSerializer, TitleValidator):
    
    class Meta:
        model = Link
        fields = "__all__"

class LinkUpdateSerializer(serializers.ModelSerializer, TitleValidator):
    
    class Meta:
        model = Link
        fields = ['title']
        
    
