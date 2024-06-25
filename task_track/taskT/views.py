from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from taskT.models import User, Task, Category
import traceback
import re
from django.db.models import Q

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
            print(traceback.format_exc())
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
        
        
class CatOption(APIView):
    def get(self, request):
        try:
            cat_object = Category.objects.all().values()
            return Response(data= cat_object, status=200)
        except:
            return Response(status=400)
        
class AddTask(APIView):
    def post(self, request):
        try:
            name = request.data.get('name')
            user_id = request.data.get('user_id')
            cat_id = request.data.get('cat_id')
            status = request.data.get('status')
            due_at = request.data.get('due_at')
            user = User.objects.get(pk = user_id)
            category = Category.objects.get(name=cat_id)      
            Task_object = Task(name = name, user_id=user, cat_id = category, due_at= due_at, status = status)
            Task_object.save()           
            return Response(data="task added", status = 200)
        except User.DoesNotExist:
            return Response(data="User Doesnot Exist", status = 400)
        except Category.DoesNotExist:
            return Response(data="Invalid Category Name", status = 400)
        except:
            return Response(data="invalid", status = 400)
        
class TaskList(APIView):
    def get(self, request):
        try:
            user_id = request.query_params.get('user_id')
            task_list = Task.objects.filter(user_id__id = user_id).values('name', 'due_at', 'cat_id', 'status')
            return Response(data = task_list, status=200)
        except:
            return Response(data = "Server Error", status=400)
            
class TaskDelete(APIView):
    def delete(self , request):
        try:
            id = request.query_params.get('id')
            task_delete_object = Task.objects.get(pk = id)
            task_delete_object.delete()
            return Response(data= "Task deleted", status=200)
        except Task.DoesNotExist:
            return Response(data= "Task Does Not Exist", status = 400)
        except:
            return Response(data= "server error", status=400)
            
class TaskUpdate(APIView):
    def put(self, request):
        try:
            id = request.query_params.get('id')
            status = request.query_params.get('status')
            task_update_object = Task.objects.get(pk = id)
            task_update_object.status = status
            task_update_object.save()
            return Response(data = "Task Updated", status = 200)
        except Task.DoesNotExist:
            return Response(data= "Task Does Not Exist", status = 400)
        except:
            return Response(data= "server error", status=400)
        
class TaskSearch(APIView):
    def get(self, request):
        try:
            search_cat = request.query_params.get('search_cat')
            name = request.query_params.get('name')
            task_search_object = Task.objects.filter(Q(name = name) | Q(cat_id__name = search_cat)).values('name', 'due_at', 'status')
            return Response(data = task_search_object, status = 200)
        except:
            return Response(data = "Server error", status=400)
            
                        