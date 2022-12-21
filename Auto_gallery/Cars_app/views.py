from django.shortcuts import render
#from django.http import HttpResponse 
from Cars_app.models import CarsModel
# Create your views here.
def carsListView(request):
    Cars = CarsModel.objects.all()

    context= {
        "carslist":Cars
    }
    return render(request,"Cars_app/carslist.html",context)
