# views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SensorData
from .serializers import SensorDataSerializer

class SensorDataView(APIView):
    def post(self, request, format=None):
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensagem": "Dados recebidos com sucesso!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    sensor_data = SensorData.objects.all()
    return render(request, 'api_nodeRed/home.html', {'sensor_data': sensor_data})
