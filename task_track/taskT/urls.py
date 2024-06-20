from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.Signup.as_view(), name="signup"),
    path('login/', views.Login.as_view(), name="login"),
    path('add-task/', views.AddTask.as_view(), name="addtask")
]