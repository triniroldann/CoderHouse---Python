from django.shortcuts import render
from django.http import HttpResponse
from doctors.models import Doctors
from doctors.forms import DoctorsForm
def create_doctor(request):
    if request.method == "GET":
        context= {"form": DoctorsForm ()}
        return render(request, "doctors/newdoctor.html", context=context)
    elif request.method == "POST":
        form=DoctorsForm(request.POST)
        if form.is_valid():
            Doctors.objects.create(
                name=form.cleaned_data['name'],
                speciality=form.cleaned_data['speciality'],
                birth_date=form.cleaned_data['birth_date'],
            )
            context= {"message": "Se añadió un nuevo doctor exitosamente"}
            return render(request, 'doctors/newdoctor.html', context= context)
        else:
            context= {"form_errors": form.errors, 
            "form": DoctorsForm}
            return render(request, 'doctors/newdoctor.html', context= context)

def list_doctors(request):
    if 'search' in request.GET:
        search = request.GET['search']
        all_doctors = Doctors.objects.filter(name__contains=search)
    else: 
        all_doctors = Doctors.objects.all()
    context = {
        'doctors': all_doctors,
            }
    return render(request, 'doctors/list_doctors.html', context=context)