from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.response import Response

from .models import Сompound, News
from .serializers import CompoundSerializer, NewsListSerializer, NewsSerializer, CompoundListSerializer
from .swaggerdec import compound_post_swagger, compound_get_swagger, compound_get_detail_swagger, compound_delete_swagger, new_post_swagger, new_get_swagger, new_get_detail_swagger, new_delete_swagger


class CompoundAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @compound_get_swagger
    def get(self, request, *args, **kwargs):
        compounds = Сompound.objects.all()
        serializer = CompoundListSerializer(compounds, many=True)
        return Response(serializer.data)
    
    @compound_post_swagger
    def post(self, request, *args, **kwargs):
        serializer = CompoundSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Сотрудник успешно создан'}, status=status.HTTP_201_CREATED)
        return Response({'msg': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class CompoundDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @compound_get_detail_swagger
    def get(self, request, com_id, *args, **kwargs):
        try:
            compound = Сompound.objects.get(id=com_id)
        except Сompound.DoesNotExist:
            return Response({'msg': 'Сотрудник не найден'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CompoundSerializer(compound)
        return Response(serializer.data)
    
    @compound_delete_swagger
    def delete(self, request, com_id, *args, **kwargs):
        try:
            com_obj = Сompound.objects.get(id=com_id)
        except Сompound.DoesNotExist:
            return Response({"msg": "Сотрудник не найден"}, status=status.HTTP_404_NOT_FOUND)
        com_obj.delete()
        return Response({"msg": "Сотрудник успешно удален"}, status=status.HTTP_204_NO_CONTENT)


    def put(self, request, com_id, *args, **kwargs):
        try:
            com_obj = Сompound.objects.get(id=com_id)
        except Сompound.DoesNotExist:
            return Response({"msg": "Сотрудник не найден"}, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = CompoundSerializer(com_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'msg': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class NewsAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @new_get_swagger
    def get(self, request, *args, **kwargs):
        news = News.objects.all()
        serializer = NewsListSerializer(news, many=True)
        return Response(serializer.data)

    @new_post_swagger    
    def post(self, request, *args, **kwargs):
        context = {'request': request}
        serializer = NewsSerializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Новость успешно создана'}, status=status.HTTP_201_CREATED)
        return Response({'msg': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class NewsDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    @new_get_detail_swagger
    def get(self, request, new_id, *args, **kwargs):
        try:
            new = News.objects.get(id=new_id)
        except News.DoesNotExist:
            return Response({'msg': 'Новость не найдена'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = NewsSerializer(new)
        return Response(serializer.data)

    def put(self, request, new_id, *args, **kwargs):
        try:
            new_obj = News.objects.get(id=new_id)
        except News.DoesNotExist:
            return Response({"msg": "Новость не найдена"}, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = NewsSerializer(new_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'msg': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    @new_delete_swagger
    def delete(self, request, new_id, *args, **kwargs):
        try:
            new_obj = News.objects.get(id=new_id)
        except News.DoesNotExist:
            return Response({"msg": "Новость не найдена"}, status=status.HTTP_404_NOT_FOUND)
        new_obj.delete()
        return Response({"msg": "Новость успешно удалена"}, status=status.HTTP_204_NO_CONTENT)


