from django.urls import path
from .views import top

app_name = 'tech_marathon'
urlpatterns = [
    path('top_page/', top.TopTemplateView.index, name='top_page'),
]
