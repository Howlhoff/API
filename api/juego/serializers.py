from .models import *
from rest_framework import serializers

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = juego
        fields = ('__all__')
        
