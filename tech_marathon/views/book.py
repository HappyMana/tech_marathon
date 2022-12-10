from django.views.generic import TemplateView
from django.shortcuts import render, redirect, reverse

class BookTemplateView(TemplateView):

  # 　詳細ページ
  def show(request, book_id):
    ctx = {
      "book_id": book_id
    }
    return render(request, 'tech_marathon/book/show.html', ctx)

  # 作成フォーム
  def new(request):
    return render(request, 'tech_marathon/book/new.html')

  # 登録
  def create(request):
    return redirect(request, 'tech_marathon/user/top.html')

  # 編集
  def edit(request, book_id):
    ctx = {
      "book_id": book_id
    }
    return render(request, 'tech_marathon/book/edit.html', ctx)

  # 削除
  def delete(request):
    return redirect(request, 'tech_marathon/top.html')

  # 未読本を一覧表示
  def unread_books(request):
    return render(request, 'tech_marathon/book/unread_books.html')
