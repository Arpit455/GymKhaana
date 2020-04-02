from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import EquipmentForm, NotificationForm
from users.models import CustomUser, CustomerProfile
from .models import Membership
import datetime

def HomePage(request) :
    return render(request, 'gymnasium/home.html')


def FitnessClasses(request) :
    return render(request, 'gymnasium/fitnessClasses.html')


def Aquatics(request) :
    return render(request, 'gymnasium/aquatics.html')


@login_required
def AddEquipment(request) :
    if request.method == 'POST':  # data sent by user
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()  # this will save the details to database
            return HttpResponse('Project details added to database')
    else:  # display empty form
        form = EquipmentForm()
    return render(request, 'Manager/addEquipment.html', {'add_eqip_form' : form})


@login_required
def DisplayCustomerProfile(request) :
    user_object = CustomUser.objects.get(username=request.user)
    customer_profile_object = CustomerProfile.objects.get(account=user_object)
    membership_object = Membership.objects.get(name=user_object)
    membership_deadline = membership_object.deadline
    membership_deadline = membership_deadline.replace(tzinfo=None)
    if membership_deadline >= datetime.datetime.now(tz=None) :
        membership_status = "Active"
    else :
        membership_status = "Inactive"
    return render(request, 'Customer/profile.html', {'customer' : customer_profile_object, 'membership_status' : membership_status, 'membership' : membership_object})


def PostNotification(request) :
    if request.method == 'POST' :
        form = NotificationForm(request.POST)
        if form.is_valid() :
            form.save()
    else :
        form = NotificationForm()
    return render(request, 'Manager/postNotification.html', {'new_notification_form' : form})


