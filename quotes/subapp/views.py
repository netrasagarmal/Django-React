from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
import json
# Create your views here.

class ReactView(APIView):
	
	serializer_class = ReactSerializer

	def get(self, request):
		detail = [ {"name": detail.name,"detail": detail.detail}
		for detail in React.objects.all()]
		return Response(detail)

	def post(self, request):

		serializer = ReactSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data)

class Sample(APIView):
    serializer_class = sampleSerializer
  
    def get(self, request):
        data1 = {
            "user": {
                "name": "Sagar Patil",
                "age": 21,
                "Place": "Baramati",
                "Blood group": "O-ve"
            }
        }
        
        # Serializing json
        res1 = json.dumps( data1 )
        return Response(res1)
  
    def post(self, request):
  
        serializer = sampleSerializer(data=request.data)
        # Data to be written 
        data1 = {
            "user": {
                "name": "satyam kumar",
                "age": 21,
                "Place": "Patna",
                "Blood group": "O+"
            }
        }
        
        # Serializing json
        res1 = json.dumps( data1 )
        if serializer.is_valid(raise_exception=True):
            print(serializer.data['userName']+" age is : "+serializer.data['age'])
            print(res1)
            return  Response(res1)
