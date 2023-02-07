from django.shortcuts import render
from django.http import HttpResponse
from surgeries.models import Surgeries, Category
from surgeries.forms import SurgeriesForm
from django.contrib.auth.decorators import login_required
@login_required
def create_surgerie(request):
    if request.method == "GET":
        context= {"form": SurgeriesForm()}
        return render(request, "surgeries/newsurgerie.html", context=context)
    elif request.method == "POST":
        form=SurgeriesForm(request.POST)
        if form.is_valid():
            Surgeries.objects.create(
                organ=form.cleaned_data['organ'],
                price=form.cleaned_data['price'],
                legal_age=form.cleaned_data['legal_age'],
            )
            context= {"message": "Se añadió una nueva cirugía exitosamente"}
            return render(request, 'surgeries/newsurgerie.html', context= context)
        else:
            context= {"form_errors": form.errors, 
            "form": SurgeriesForm}
            return render(request, 'sugeries/newsurgerie.html', context= context)

def list_surgeries(request):
    all_surgeries = Surgeries.objects.all()
    context = {
        'surgeries': all_surgeries,
    }
    return render(request, 'surgeries/listsurgeries.html', context=context)

@login_required
def create_category(request, name):
    Category.objects.create(name=name)
    return HttpResponse('Categoria creada')
def list_categories(request):
    all_categories = Category.objects.all()
    context = {
        'categories':all_categories
    }
    return render(request, 'surgeries/list_categories.html', context=context)

