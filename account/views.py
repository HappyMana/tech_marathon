from django.shortcuts import render
from django.views.generic import TemplateView
from account.forms import AccountForm

class AcountTemplateForm(TemplateView):
  def login(request):
    ctx = {
      "form": AccountForm()
    }
    return render(request, 'account/login.html', ctx)
