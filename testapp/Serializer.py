from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        #field = ['name','age']
        #exclude = ['id']
        fields = '__all__'
