from django import forms

class New_login_form(forms.Form):
    username = forms.CharField(label='Username', max_length=200)
    password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput)

class New_register_form(forms.Form):
    username = forms.CharField(label='Username', max_length=200)
    email = forms.EmailField(label='Email (optional)', max_length=200, required=False)
    password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput)