from django.views.generic import TemplateView
from django.shortcuts import render, redirect, reverse
from tech_marathon.models import Book
from django.contrib.auth.models import User

class TopTemplateView(TemplateView):

  # トップページ
  def index(request):
    ctx = {
      'user': User.objects.get(id=request.user.id),
      'books': Book.objects.prefetch_related('category').filter(user_id=request.user.id, read_status=True)
    }
    return render(request, 'tech_marathon/top.html', ctx)
