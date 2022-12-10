from django.urls import path
from .views import top, user, book

app_name = 'tech_marathon'
urlpatterns = [
    path('', top.TopTemplateView.index, name='top'),

    path('sign_in/', user.UserTemplateView.sign_in, name='sign_in'),
    path('sign_up/', user.UserTemplateView.sign_up, name='sign_up'),
    path('my_page/', user.UserTemplateView.my_page, name='my_page'),
    path('my_page/edit/', user.UserTemplateView.edit, name='my_page_edit'),
    path('other_users/', user.UserTemplateView.other_users, name='other_users'),
    path('other_user/<int:user_id>/', user.UserTemplateView.other_user, name='other_user'),

    path('book/<int:book_id>', book.BookTemplateView.show, name='book_show'),
    path('book/new', book.BookTemplateView.new, name='book_new'),
    path('book/create', book.BookTemplateView.create, name='book_create'),
    path('book/edit/<int:book_id>', book.BookTemplateView.edit, name='book_edit'),
    path('book/delete', book.BookTemplateView.delete, name='book_delete'),
    path('book/unread_books', book.BookTemplateView.unread_books, name='unread_books'),
]
