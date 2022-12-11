from django.views.generic import TemplateView
from django.shortcuts import render, redirect, reverse
from tech_marathon.models import Book, User
from tech_marathon.forms import SignInForm, SignUpForm

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
      # TODO
      "books": Book.object.filter(user_id=user_id, read_status=True)
    }
    return render(request,'tech_marathon/user/other_user.html', ctx)

  # ログアウト
  # TODO
  def log_out(request):
    return redirect(request,'tech_marathon/user/log_out.html')
