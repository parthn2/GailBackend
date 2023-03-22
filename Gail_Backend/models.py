from django.db import models

# Create your models here.
class Motor(models.Model):
    motor_id=models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.motor_id)
    
class Current(models.Model):
    value=models.FloatField()
    motor=models.ForeignKey(Motor, on_delete=models.CASCADE)

class Voltage(models.Model):
    value=models.FloatField()
    motor=models.ForeignKey(Motor, on_delete=models.CASCADE)
    

