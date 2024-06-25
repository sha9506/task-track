from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.Signup.as_view(), name="signup"),
    path('login/', views.Login.as_view(), name="login"),
    path('cat-option/', views.CatOption.as_view(), name='catOption'),
    path('task-list/', views.TaskList.as_view(), name = "tasklist"),
    path('add-task/', views.AddTask.as_view(), name="addtask"),
    path('task-delete/', views.TaskDelete.as_view(), name='taskdelete'),
    path('task-update/', views.TaskUpdate.as_view(), name='taskupdate'),
    path('task-search/', views.TaskSearch.as_view(), name='tasksearch')
]