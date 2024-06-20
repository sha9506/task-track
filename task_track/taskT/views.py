from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from taskT.models import Task
from taskT.models import User

# Create your views here.

class Signup(APIView):
    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            email = request.data.get('email')
            
            if not email or not password:
                return Response(data="Enter your credentials", status=400)
            
            if not self.validate_email(email = email):
                return Response(data="Invalid email", status=400)
            
            User_object = User(username = username, email = email, password = password, first_name = first_name, last_name = last_name)
            User_object.save()
            
            return Response(data="User Registered", status = 200)
        
        except Exception:
            return Response(data="Invalid Entry", status=400)
        
    def validate_email(self, email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        return False

class Login(APIView):
    def post(self, request):
        try:
            username = request.data.get("usename")
            password = request.data.get("password")
            User_object.get(username = username , password = password)
            return Response(data="Login Successful", status= 200)
        except:
            return Response(data="Invalid Credentials", status= 400)
        
class AddTask(APIView):
    def post(self, request):
        try:
            name = request.data.get('name')
            catagory = request.data.get('catagory')
            status = request.data.get('status')
            
            Task_object = Task(name = name, catagory = catagory, status = status)
            Task_object.save()
                    
            return Response(data="task added", status = 200)
        except:
            return Response(data="invalid", status = 400)