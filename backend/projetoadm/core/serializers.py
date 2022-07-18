from asyncore import read
from dataclasses import field
from pyexpat import model
from rest_framework import serializers 
from .models import Policial,Posto

class PostoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Posto
        fields='__all__'
        # depth = 1


class PolicialSerializer(serializers.ModelSerializer):
    
    posto=PostoSerializer()

    class Meta:
        model=Policial
        fields='__all__'
        depth = 1
        