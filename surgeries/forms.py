from django import forms 
class SurgeriesForm(forms.Form):
    organ= forms.CharField(max_length=100, label='Organo donde se realiza la operación: ')
    price = forms.FloatField(label='Precio:')
    legal_age= forms.BooleanField(required=False, label='¿Se requiere ser mayor de edad? :')