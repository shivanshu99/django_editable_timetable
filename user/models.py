from django.contrib.auth.models import User


from django.db import models  
class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    edays = models.CharField(max_length=100)  
    esub1 = models.CharField(max_length=100) 
    esub2 = models.CharField(max_length=100)  
    esub3 = models.CharField(max_length=100)
    esub4 = models.CharField(max_length=100) 
    esub5 = models.CharField(max_length=100) 
    esub6 = models.CharField(max_length=100) 
    esub7 = models.CharField(max_length=100) 
    esub8 = models.CharField(max_length=100) 
    class Meta:  
        db_table = "employee"  