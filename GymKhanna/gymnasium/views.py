from django.shortcuts import render
from django.http import HttpResponse
from .forms import EquipmentForm


def HomePage(request) :
    return render(request, 'gymnasium/home.html')

def FitnessClasses(request) :
    return render(request, 'gymnasium/fitnessClasses.html')

def AddEquipment(request) :
    if request.method == 'POST':  # data sent by user
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()  # this will save the details to database
            
            return HttpResponse('Project details added to database')
    else:  # display empty form
        form = EquipmentForm()
    return render(request, 'Manager/addEquipment.html', {'add_eqip_form' : form})