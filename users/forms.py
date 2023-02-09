from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from users.models import UserProfile

YEARS= [x for x in range(1940,2021)]

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True, label='Nombre')
    last_name = forms.CharField(max_length=100, required=True, label='Apellido')
    email= forms.EmailField(required=True)
    class Meta: 
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username':forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'id':'username'
                }
            ),
            'email':forms.EmailInput(
                attrs= {
                    'class':'form-control',
                    'id':'email'
                }
            )
        }
class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, label='Username')
    first_name = forms.CharField(max_length=100, required=True, label='Nombre')
    last_name = forms.CharField(max_length=100, required=True, label='Apellido')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
class UserProfileForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS), label='Fecha de nacimiento ')
    class Meta:
        model = UserProfile
        fields = [ 'email', 'profile_picture']
