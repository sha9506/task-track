from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField( max_length=254, unique=True)
    password = models.CharField(max_length=50)
    
class Category(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    
class Task(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    cat_id = models.ForeignKey("Category", on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    due_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
