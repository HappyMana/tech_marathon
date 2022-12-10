from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path

urlpatterns = [
path('login/',LoginView.as_view(
  redirect_authenticated_user=True,
  template_name='account/login.html'
),name='login' ),
path('logout/',LogoutView.as_view(),name='logout')

]