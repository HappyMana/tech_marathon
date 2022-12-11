from django.views.generic import TemplateView
from django.shortcuts import render, redirect, reverse
from tech_marathon.models import Book
from tech_marathon.forms import SignInForm, SignUpForm
from django.db import models
from django.contrib.auth.models import User
class UserTemplateView(TemplateView):

  # ログインしているユーザのマイページ
  def my_page(request):
    ctx = {
      "user": User.objects.get(id=request.user.id)
    }
    return render(request, 'tech_marathon/user/my_page.html', ctx)

  # マイページ情報を編集
  # TODO
  def edit(request):
    return render(request, 'tech_marathon/user/edit.html')

  # 他のユーザーたち
  def other_users(request):
    ctx = {
      # TODO
      "other_users": User.object.exclude(id=request.user.id, read_status=True)
    }
    return render(request,'tech_marathon/user/other_users.html', ctx)

  # 他のユーザーの詳細ページ
  def other_user(request, user_id):
    ctx = {
      "user": User.objects.get(id=request.user.id),
      "books": Book.object.filter(user_id=user_id, read_status=True)
    }
    return render(request,'tech_marathon/user/other_user.html', ctx)
