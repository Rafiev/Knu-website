from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model


from .serializers import CustomUserSerializer
from .swaggerdec import user_post_swagger, user_delete_swagger

User = get_user_model()

class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @user_post_swagger
    def post(self, request, *args, **kwargs): 
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Вы успешно добавили пользователя'}, status=status.HTTP_201_CREATED)
        return Response({'msg': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    @user_delete_swagger
    def delete(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({'msg': 'У вас недостаточный уровень доступа'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        try:
            user = request.data.get('username')
            delete_user = User.objects.get(username=user)
            delete_user.delete()
            return Response({'msg': 'Вы успешно удалили пользователя'}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'msg': 'Данного пользователя не существует'}, status=status.HTTP_400_BAD_REQUEST)
