from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
