from django.shortcuts import get_list_or_404, render
from rest_framework.views import APIView
from Gail_Backend import serializers

from Gail_Backend.serializers import MotorSerializer
from .models import Motor, Current, Voltage
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class MotorList(APIView):
    def get(self, request):
        items = Motor.objects.all()
        serializer = MotorSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        motor = Motor.objects.filter(motor_id=request.data['motor_id'])
        if not motor:
            Motor.objects.create(motor_id = request.data['motor_id']).save()
            motor = Motor.objects.filter(motor_id=request.data['motor_id'])
        Current.objects.create(value=request.data['current'], motor=motor[0]).save()
        Voltage.objects.create(value=request.data['voltage'], motor=motor[0]).save()
        return Response('done')


class MotorDetail(APIView):
    def get(self, request, motor_id):
        motor = Motor.objects.filter(motor_id=motor_id)
        current = list(Current.objects.filter(motor=motor[0]).values_list('value', flat=True))
        voltage = list(Voltage.objects.filter(motor=motor[0]).values_list('value', flat=True))
        return Response({'current': current, 'voltage': voltage})