from django import forms
from .models import signup,login

class UserCreationForm(forms.ModelForm):
    
     class Meta:
        model = signup
        fields = ('fullname', 'email', 'username','password')

class AuthenticationForm(forms.ModelForm):
    class meta:
        model = login
        fields = ('user','passw')