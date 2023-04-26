from urllib import response
from black import maybe_install_uvloop
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Policial,Posto,Graduacao
from .serializers import PolicialSerializer,PostoSerializer,GraduacaoSerializer
from rest_framework import viewsets



class PolicialViewSet(viewsets.ModelViewSet):
    serializer_class= PolicialSerializer
    queryset=Policial.objects.all()

    
class PostoViewSet(viewsets.ModelViewSet):
    serializer_class= PostoSerializer
    queryset=Posto.objects.all()

class GraduacaoViewSet(viewsets.ModelViewSet):
    serializer_class= GraduacaoSerializer
    queryset=Graduacao.objects.all()