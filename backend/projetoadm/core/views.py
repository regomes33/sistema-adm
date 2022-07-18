from urllib import response
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.http import JsonResponse
from .models import Policial
from .serializers import PolicialSerializer




# class PolicialListView(generics.ListCreateAPIView):
#     serializer_class= PolicialSerializer
#     queryset=Policial.objects.all()

    

def api_policial(request):
    context={}
    if request.method == "GET":
        policiais = Policial.objects.all()
        policiais_serializer = PolicialSerializer(policiais, many=True)
        return JsonResponse(policiais_serializer.data, safe=False)
    
    elif request.method == "POST":
        policial_data = JSONParser.parse(request)
        policiais_serializer = PolicialSerializer(data=policial_data)
        if policial_data.is_valid():
            policiais_serializer.save()
            return JsonResponse("adicionado com sucesso", safe=False)
        return JsonResponse("Não foi possivel Salvar", safe=False)
    elif request.method == "PUT":
        policial_data = JSONParser().parse(request)
        policiais = Policial.objects.get(PolicialId=policial_data["PolicialId"])
        policiais_serializer = PolicialSerializer(policiais, data=policial_data)
        if policiais_serializer.save.is_valid():
            policiais_serializer.save()
            return JsonResponse("Atualizado com sucesso", safe=False)
        return JsonResponse("Falha ao atualizar ")
    return render(request,'api/policial/',context)

