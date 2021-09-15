# from django.shortcuts import render
# from testapp.models import Student
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#from rest_framework.parsers import JSONParser
#from testapp.serializers import Student_serializer
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .Serializer import StudentSerializer





# from .models import *
# from .serializers import *
#


@api_view(['GET'])
def create_student(request):
     print(request.META)
     #serializers = StudentSerializer(student_objs,many=True)

     return Response({'status':200})
@api_view(['POST'])
def post_student(request):
    data=request.data
    print(data)
    serializers = StudentSerializer(data = request.data)

    if not serializers.is_valid():
        print(serializers.errors)
        return Response({'status':403,'errors':serializers.data,'msg':'something went wrong'})
        serializers.save()
    return Response({'status':200})

@api_view(['PUT'])
def update_student(request , id):
    try:
        student_objs = Student.objects.get(id = id)
        serializers = StudentSerializer(student_objs ,data = request.data,partial = True)
        if not serializers.is_valid():
            print(serializers.errors)
            return Response({'status':404,'errors':serializers.data,'msg':'something went wrong'})
        serializers.save()
        return Response({'status':200})
    except Exception as e:
       return Response({'status':404,'message':e.__str__()})






























# @api_view(['DELETE','GET','PUT','POST'])
# def create_student(request):
#     if request.method == "POST":
#         payloadData = JSONParser().parse(request)
#         print(payloadData)
#         Studentserializer = Student_serializer(data=payloadData)
#         flag = Studentserializer.is_valid()
#         print(flag)
#         if flag:
#             Studentserializer.save()
#             return Response(Studentserializer.data, status=201)
#         return Response({'message': 'The Student was not created'}, status = 400)
#
#
#     elif request.method == "GET":
#         #stud_data = Student.objects.all()
#         print(request.GET)
#         #print("this is stud_data",stud_data)
#         stud_serializer = Student_serializer(stud_data,many=True)
#         return Response(stud_serializer.data)
