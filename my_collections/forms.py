from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.forms import ModelForm, TextInput
from models import Collection

class LoginForm(AuthenticationForm):
  username = forms.CharField(label="Username", max_length=30, required=True,
                             widget=forms.TextInput(attrs={'type':'email', 'class': 'form-control', 
                                  'name': 'username', 'id':'username', 'placeholder':'Email'}))
  password = forms.CharField(label="Password", max_length=30, 
                             widget=forms.TextInput(attrs={'type':'password', 'class': 'form-control', 
                              'name': 'password', 'id':'password', 'placeholder':'Password'}))

class RegistrationForm(forms.Form):
  email = forms.EmailField(required=True,widget=forms.TextInput())
  password = forms.CharField(label="Password", max_length=30, widget=forms.TextInput(attrs={'type':'password', 'class': 'form-control', 
                              'name': 'password', 'id':'password', 'placeholder':'Password'}))
  confirmPassword = forms.CharField(required=True,widget=forms.TextInput())

  def clean(self):
    password = self.cleaned_data.get('password')
    confirmPassword = self.cleaned_data.get('confirmPassword')

    if password and password != confirmPassword:
      raise forms.ValidationError("Passwords don't match")

    return self.cleaned_data

class CollectionForm(ModelForm):
  class Meta:
    model = Collection
    fields = ['id','name','description','isPrivate']
    widget = {
      'name' : TextInput(attrs={"class":"form-control"}),
    }
  id = forms.IntegerField()