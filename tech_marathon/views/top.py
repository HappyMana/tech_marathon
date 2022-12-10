from django.views.generic import TemplateView
from django.shortcuts import render, redirect, reverse
from tech_marathon.models import Book, User
class TopTemplateView(TemplateView):

  # トップページ
  def index(request):
    ctx = {
      # TODO
      # 認証ができたらコメントアウトをはずす
      # 'user': request.user,
      # 'books': Book.objects.filter(user_id=request.user.id, read_status=True)
      'user': User.objects.get(id=1),
      'books': Book.objects.filter(user_id=1, read_status=True)
    }
    return render(request, 'tech_marathon/top.html', ctx)
