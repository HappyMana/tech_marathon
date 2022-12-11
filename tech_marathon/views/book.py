from django.views.generic import TemplateView
from django.shortcuts import render, redirect, reverse
from tech_marathon.models import Book
from tech_marathon.forms import BookForm
from django.contrib.auth.models import User

class BookTemplateView(TemplateView):

  # 　詳細ページ
  def show(request, book_id):
    ctx = {
      "book": Book.objects.prefetch_related('category').get(id=book_id)
    }
    return render(request, 'tech_marathon/book/show.html', ctx)

  # 作成フォーム
  # TODO
  def new(request):
    ctx = {
      "form": BookForm()
    }
    return render(request, 'tech_marathon/book/new.html', ctx)

  # 登録
  # TODO
  def create(request):
    form = BookForm(request.POST)
    form.save(user_id=1)
    return redirect(request, 'tech_marathon/user/top.html')

  # 編集
  # TODO
  def edit(request, book_id):
    ctx = {
      "form": BookForm(),
      "book": Book.objects.filter(id=book_id)
    }
    return render(request, 'tech_marathon/book/edit.html', ctx)

  # 削除
  # TODO
  def delete(request):
    return redirect(request, 'tech_marathon/top.html')

  # 未読本を一覧表示
  def unread_books(request):
    ctx = {
      "user": User.objects.get(id=request.user.id),
      "books": Book.objects.filter(user_id=request.user.id, read_status=False)
    }
    return render(request, 'tech_marathon/book/unread_books.html', ctx)
