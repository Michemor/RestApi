from rest_framework import serializers

from .models import Student

class Student_serializer(serializers.ModelSerializer):
    """
    packages the data in a way that can be transmitted or saved easily
    i.e objects in a database 
    """

    class Meta:
        # data about data
        
