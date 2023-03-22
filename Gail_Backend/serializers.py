
from rest_framework import serializers
from Gail_Backend.models import Motor, Current

class MotorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motor
        fields = ["motor_id"]

class CurrentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Current
        fields = ["motor_id"]