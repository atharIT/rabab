
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib import auth

from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import  AccountCreationForm, SupervisorCreationForm ,AdminCreationForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


#################### index#######################################
def index(request):
    return render(request, 'user/index.html', {'title' :'index'})

########### register here #####################################
def volunteerRegister(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST.get('email')
            password = request.POST.get('password')
            print(email, password)
            user = auth.authenticate(username=email, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect(reverse('authentications:index'))
                return HttpResponse('Your id is inactive')
            return HttpResponse('Invalid login details provided')


    else:
        form =AccountCreationForm()
    return render(request, 'user/register.html', {'form': form, 'title' :'reqister here'})

def superviorRegister(request):
    if request.method == 'POST':
        form = SupervisorCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST.get('email')
            password = request.POST.get('password')
            print(email, password)
            user = auth.authenticate(username=email, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect(reverse('authentications:index'))
                return HttpResponse('Your id is inactive')
            return HttpResponse('Invalid login details provided')


    else:
        form =SupervisorCreationForm()
    return render(request, 'user/register2.html', {'form': form, 'title' :'reqister here'})

def adminRegister(request):
    if request.method == 'POST':
        form = AdminCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST.get('email')
            password = request.POST.get('password1')
            print(email, password)
            user = auth.authenticate(username=email, password=password)

            if user:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect(reverse('authentications:index'))
                return HttpResponse('Your id is inactive')
            return HttpResponse('Invalid login details provided')


    else:
        form =AdminCreationForm()
    return render(request, 'user/register1.html', {'form': form, 'title' :'reqister here'})

################ login forms###################################################

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        user = auth.authenticate(username=email, password=password)

        if user:
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('authentications:index'))
            return HttpResponse('Your id is inactive')
        return HttpResponse('Invalid login details provided')


    context = {}
    return render(request, 'user/login.html', context=context)



def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('authentications:index'))
