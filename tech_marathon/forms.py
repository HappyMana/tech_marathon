from django import forms

class BookForm(forms.Form):
  title = forms.CharField(label="タイトル")
  memo = forms.CharField(label="メモ")
  read_status = forms.BooleanField(label="よんだか")
  begin_date = forms.DateField(label="購入日")
  end_date = forms.DateField(label="読破日")

class SignInForm(forms.Form):
  name = forms.CharField(label="名前")
  password = forms.CharField(label="パスワード", widget=forms.PasswordInput(), min_length=8)

class SignUpForm(forms.Form):
  name = forms.CharField(label="名前")
  email = forms.CharField(label="メールアドレス")
  password = forms.CharField(label="パスワード", widget=forms.PasswordInput(), min_length=8)
