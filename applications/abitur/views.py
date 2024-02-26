from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from  .serializers import ApplicantSerializer
from .models import Applicant
from .swaggerdec import applicant_post_swagger, applicant_get_swagger, applicant_delete_swagger
from .permissions import IsAdmin

class ApplicantAPIView(APIView):
    permission_classes = [IsAdmin]
    
    @applicant_get_swagger
    def get(self, request, *args, **kwargs):
        applicants_list = Applicant.objects.all()
        serializer = ApplicantSerializer(applicants_list, many=True)
        return Response(serializer.data)

    @applicant_post_swagger
    def post(self, request, *args, **kwargs,):
        serializer = ApplicantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Абитуриент успешно создан'}, status=status.HTTP_201_CREATED)
        return Response({'msg': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class ApplicantDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @applicant_delete_swagger
    def delete(self, request, appl_id, *args, **kwargs):
        try:
            appl_obj = Applicant.objects.get(id=appl_id)
        except Applicant.DoesNotExist:
            return Response({"msg": "Абитуриент не найден"}, status=status.HTTP_404_NOT_FOUND)
        appl_obj.delete()
        return Response({"msg": "Абитуриент успешно удален"}, status=status.HTTP_204_NO_CONTENT)
    

    