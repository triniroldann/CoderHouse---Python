from django.shortcuts import render
from django.http import HttpResponse
from doctors.models import Doctors
from doctors.forms import DoctorsForm
from django.views.generic import ListView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
@login_required
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
@login_required
def update_doctor(request,id):
    doctor= Doctors.objects.get(id=id)
    if request.method == "GET":
        context= {
            "form": DoctorsForm(
            initial={
            'name': doctor.name,
            'speciality' : doctor.speciality,
            'birth_date' : doctor.birth_date,
        })}
        return render(request, "doctors/doctor.update.html", context=context)
    elif request.method == "POST":
        form=DoctorsForm(request.POST)
        if form.is_valid():
                doctor.name=form.cleaned_data['name']
                doctor.speciality=form.cleaned_data['speciality']
                doctor.birth_date=form.cleaned_data['birth_date']
                doctor.save()
                context= {"message": "Se modificó un doctor exitosamente"}
                return render(request, 'doctors/doctor.update.html', context= context)
        else:
            context= {"form_errors": form.errors, 
            "form": DoctorsForm}
            return render(request, 'doctors/doctor.update.html', context= context)

class Doctors_list(ListView):
    model= Doctors
    template_name= 'doctors/list_doctors.html'
    form= DoctorsForm
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(name__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list
class DoctorDeleteView(LoginRequiredMixin, DeleteView):
    model = Doctors
    template_name = "doctors/doctor.delete.html"
    success_url= '/doctors/list-doctors/'
    
