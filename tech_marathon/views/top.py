from django.views.generic import TemplateView
from django.shortcuts import render, redirect, reverse

class TopTemplateView(TemplateView):

  def index(request):
    return render(request, 'tech_marathon/top_page.html')

