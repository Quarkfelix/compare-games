from django import forms

class New_login_form(forms.Form):
    username = forms.CharField(label='Username', max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput(attrs={'class':'form-control'}))

class New_register_form(forms.Form):
    username = forms.CharField(label='Username', max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email (optional)', max_length=200, required=False, widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', max_length=200, widget=forms.PasswordInput(attrs={'class':'form-control'}))
