from asyncore import read
from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers 
from .models import Graduacao, Policial,Posto


class PostoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Posto
        fields='__all__'
           


class GraduacaoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Graduacao
        fields='__all__'
        


class PolicialSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Policial
        fields = '__all__'
        
        

    