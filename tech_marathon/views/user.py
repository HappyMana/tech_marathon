from django.views.generic import TemplateView
from django.shortcuts import render, redirect, reverse

class UserTemplateView(TemplateView):

  # サインアップ
  def sign_up(request):
    return render(request, 'tech_marathon/user/sign_up.html')

  # サインイン
  def sign_in(request):
    return render(request, 'tech_marathon/user/sign_in.html')

  # ログインしているユーザのマイページ
  def my_page(request):
    return render(request, 'tech_marathon/user/my_page.html')

  # マイページ情報を編集
  def edit(request):
    return render(request, 'tech_marathon/user/edit.html')

  # 他のユーザーたち
  def other_users(request):
    return render(request,'tech_marathon/user/other_users.html')

  # 他のユーザーの詳細ページ
  def other_user(request, user_id):
    ctx = {
      "user_id": user_id
    }
    return render(request,'tech_marathon/user/other_user.html', ctx)

  # ログアウト
  def log_out(request):
    return redirect(request,'tech_marathon/user/sign_in.html')
