# Create your views here.

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from app import serializers
from app.models import Book
from app.serializers import BookSerializer

class BokkListCreate(APIView):
    def get(self,request):
        queryset=Book.objects.all()
        serializer_instance=BookSerializer(queryset,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer_instance=BookSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class BookRetrieveUpdateDelete(APIView):
    def get(self,request,pk):
        b=get_object_or_404(Book,id=pk)
        serializer_instance=BookSerializer(b)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        b=get_object_or_404(Book,id=pk)
        serializer_instance=BookSerializer(instance=b,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk):
        b=get_object_or_404(Book,id=pk)
        serializers_instance=BookSerializer(instance=b,data=request.data,partial=True)
        if serializers_instance.is_valid():
            serializers_instance.save()
            return Response(serializers_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        b=get_object_or_404(Book,id=pk)
        b.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)