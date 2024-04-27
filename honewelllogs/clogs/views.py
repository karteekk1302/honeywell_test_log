from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Clogs
from .Serializers import Clogsserializer
from .utils import insert_cdr_data
from honewelllogs.honewelllogs.settings import cdr_file_path


class ClogsGenerateByCDRAPIView(APIView):
    def get(self, request):
        insert_cdr_data(cdr_file_path)
        return Response({"message": "Sucessfully Generated."}, status=200)


class ClogsAPIView(APIView):
    def get(self, request):
        clogs = Clogs.objects.all()
        serializer = Clogsserializer(clogs, many=True)
        return Response(serializer.data, status=200)
