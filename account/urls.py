from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path
from django.views.generic import CreateView
app_name = 'account'
urlpatterns = [
  path('signup/',CreateView.as_view(
    template_name='account/signup.html',
    form_class=UserCreationForm,
    success_url='/',),name = 'signup'),
path('login/',LoginView.as_view(
  redirect_authenticated_user=True,
  template_name='account/login.html'
),name='login' ),
path('account/logout/',LogoutView.as_view(),name='logout'),

]