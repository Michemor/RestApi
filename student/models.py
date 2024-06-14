from django.db import models

# Create your models here.

class Student(models.Model):
    """
    Stores informationa about any student
    1. name (text)
    2. email (text)
    3. password (text)
    4. age (Integer)
    """
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    age = models.IntegerField()
    
