from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from .forms import GuideRegInfoForm
from planner.models import GUIDE, USER
# Create your views here.

def index(request):
    template = loader.get_template('WebsiteFrontPage.html')
    context = {}
    return HttpResponse(template.render(context, request))

def register_guide(request):
    template = loader.get_template('registrationpage.html')
    context={}
    return HttpResponse(template.render(context, request))

def register_user(request):
    template = loader.get_template('registrationUser.html')
    context={}
    return HttpResponse(template.render(context, request))

def login(request):
    template = loader.get_template('loginForm.html')
    context={}
    return HttpResponse(template.render(context, request))


def login_validation(request):
    template = loader.get_template('profile.html')
    email=request.POST['email']
    password=request.POST['pass']

    context={'email': email, 'password': password}
    #validation left
    return HttpResponse(template.render(context, request))



def guide_registration_data(request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    password=request.POST['password']
    email=request.POST['email']
    phoneNumber=request.POST['phoneNumber']
    address=request.POST['address']
    gender=request.POST['gender']
#about, image + some form validation required here
    model=GUIDE(FirstName=first_name, LastName=last_name, Email=email,
                Password=password,Address=address, Contact=phoneNumber,Gender=gender)
    model.save()
    #return  render(request, 'registrationpage.html')
    template = loader.get_template('profile.html')
    context = {'type': "guide", 'email': email, 'password': password}
    return HttpResponse(template.render(context, request))

def user_registration_data(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    password = request.POST['password']
    email = request.POST['email']
    phoneNumber = request.POST['phoneNumber']
    address = request.POST['address']
    gender = request.POST['gender']
    # about, image + some form validation required here
    model = USER(FirstName=first_name, LastName=last_name, Email=email,
                  Password=password, Address=address, Contact=phoneNumber, Gender=gender)
    model.save()
    # return  render(request, 'registrationpage.html')
    template = loader.get_template('profile.html')
    context = {'type': "user", 'email': email, 'password': password}
    return HttpResponse(template.render(context, request))