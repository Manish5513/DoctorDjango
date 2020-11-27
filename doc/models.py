from django.db import models

class Patient(models.Model):
    name=models.CharField(max_length=25)
    phone=models.IntegerField('your-phone')
    email=models.EmailField()
    schedule=models.CharField(max_length=15)
    day=models.CharField(max_length=15)
    Service=models.CharField(max_length=20)
    message=models.TextField(max_length=200)
    
    def __str__(self):
        return self.name
        

