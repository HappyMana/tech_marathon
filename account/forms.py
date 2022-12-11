from django import forms

class AccountForm(forms.Form):
  name = forms.CharField(label="名前")
  password = forms.CharField(label="パスワード", widget=forms.PasswordInput(), min_length=8)