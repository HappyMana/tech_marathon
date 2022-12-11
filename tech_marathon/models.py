from django.db import models
from django.utils import timezone

class User(models.Model):
  name = models.CharField(max_length=20)
  email = models.CharField(max_length=30)
  goal = models.CharField(max_length=200, null=True)

class Category(models.Model):
  name = models.CharField(max_length=20)

class Book(models.Model):
  title = models.CharField(max_length=50)
  memo = models.CharField(max_length=200, null=True)
  read_status = models.BooleanField(default=False)
  begin_date = models.DateTimeField('purchased date')
  end_date = models.DateTimeField('finished reading date', null=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  category = models.ManyToManyField(Category, related_name='book', null=True)
