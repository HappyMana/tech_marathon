from django.views.generic import TemplateView
from django.shortcuts import render, redirect, reverse
from tech_marathon.models import Book
from tech_marathon.forms import SignInForm, SignUpForm
from django.db import models
from django.contrib.auth.models import User
class UserTemplateView(TemplateView):

  # サインアップ
  # TODO
  def sign_up(request):
    ctx = {
      "form": SignUpForm()
    }
    return render(request, 'tech_marathon/user/sign_up.html', ctx)

  # サインイン
  # TODO
  def sign_in(request):
    ctx = {
      "form": SignInForm()
    }
    return render(request, 'tech_marathon/user/sign_in.html', ctx)

  # ログインしているユーザのマイページ
  def my_page(request):
    ctx = {
      # TODO
      # 認証ができたらコメントアウトをはずす
      "user": User.objects.get(id=request.user.id)
      #"user": User.objects.get(id=1)
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
      # 認証ができたらコメントアウトをはずす
      # "other_users": User.object.exclude(id=request.user.id, read_status=True)
      "other_users": User.objects.exclude(id=1)
    }
    return render(request,'tech_marathon/user/other_users.html', ctx)

  # 他のユーザーの詳細ページ
  def other_user(request, user_id):
    ctx = {
      # TODO
      # 認証ができたらコメントアウトをはずす
      # "books": Book.object.filter(user_id=user_id, read_status=True)
      "books": Book.objects.filter(user_id=2)
    }
    return render(request,'tech_marathon/user/other_user.html', ctx)

  # ログアウト
  # TODO
  def log_out(request):
    return redirect(request,'tech_marathon/user/log_out.html')
