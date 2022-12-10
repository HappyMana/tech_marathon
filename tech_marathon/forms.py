from django import forms

class BookForm(forms.Form):
  title = forms.CharField(label="タイトル")
  memo = forms.CharField(label="メモ")
  read_status = forms.BooleanField(label="よんだか")
  begin_date = forms.DateField(label="購入日")
  end_date = forms.DateField(label="読破日")
