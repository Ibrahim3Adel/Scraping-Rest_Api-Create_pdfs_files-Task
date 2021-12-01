from django.db.models import query
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import novel_auth
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import novelserializer
from rest_framework import viewsets
from django.views.generic import ListView
from .helper import PDF


class NovelViewSet(viewsets.ModelViewSet):
     queryset = novel_auth.objects.all()
     serializer_class = novelserializer
     popo = novel_auth.objects.raw('SELECT * FROM novels_novel_auth')
     for i in popo:
        PDF.takeit(i.Author_Name,i.Novel_link,i.Novel_Name)
     


#@api_view(['GET'])
#def getnovels(request):
#     novels=novel_auth.objects.all()
#     serializer = novelserializer(novels,many=True)

#     return Response(serializer.data)


#@api_view(['Get'])
#def getnovel(request,pk):
#     novel = novel_auth.objects.get(id=pk)
#     serializer = novelserializer(novel,many = False)
#     return Response(serializer.data)

#@api_view(['POST'])
#def createnovel(request):
    
#     serializer = novelserializer(data= request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

#@api_view(['POST'])
#def updatenovel(request,pk):
#     novel = novel_auth.objects.get(id=pk)
#     serializer = novelserializer(instance = novel,data= request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

#@api_view(['DELETE'])
#def deletenovel(request,pk):
#     novel = novel_auth.objects.get(id=pk)
#     novel.delete()
#     return Response('item deleted')
