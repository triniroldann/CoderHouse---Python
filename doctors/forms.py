from django import forms 

YEARS= [x for x in range(1940,2021)]

class DoctorsForm(forms.Form):
    name = forms.CharField(max_length=100, label='Nombre:')
    speciality = forms.CharField(max_length=100, label='Especialidad:')
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS), label='Fecha de nacimiento ')