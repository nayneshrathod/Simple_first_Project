from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewUserForm
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login


# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name='home.html',
                  context={"tutorials": AllCourses.objects.all})


# Create your views here.

def index(request):
    sq = {"0": {
        "title": "Naynesh",
        "desc": ''' Lorem ipsum dolor sit amet, consectetur adipisicing elit. A adipisci est eveniet, excepturi facere fugiat
                minus odit provident sit! At quaerat quo rem tempora tenetur vero? Cum magnam minus necessitatibus?
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. A adipisci est eveniet, excepturi facere
                fugiat
                minus odit provident sit! At quaerat quo rem tempora tenetur vero? Cum magnam minus necessitatibus?
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. A adipisci est eveniet, excepturi facere
                fugiat
                minus odit provid '''},
        "1": {
            "title": "Khumesh",
            "desc": ''' Lorem ipsum dolor sit amet, consectetur adipisicing elit. A adipisci est eveniet, excepturi facere fugiat
                minus odit provident sit! At quaerat quo rem tempora tenetur vero? Cum magnam minus necessitatibus?
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. A adipisci est eveniet, excepturi facere
                fugiat
                minus odit provident sit! At quaerat quo rem tempora tenetur vero? Cum magnam minus necessitatibus?
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. A adipisci est eveniet, excepturi facere
                fugiat
                minus odit provid '''},
        "2": {
            "title": "Ganesh",
            "desc": ''' Lorem ipsum dolor sit amet, consectetur adipisicing elit. A adipisci est eveniet, excepturi facere fugiat
                minus odit provident sit! At quaerat quo rem tempora tenetur vero? Cum magnam minus necessitatibus?
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. A adipisci est eveniet, excepturi facere
                fugiat
                minus odit provident sit! At quaerat quo rem tempora tenetur vero? Cum magnam minus necessitatibus?
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. A adipisci est eveniet, excepturi facere
                fugiat
                minus odit provid '''},
        "3": {
            "title": "Ramesh",
            "desc": ''' Lorem ipsum dolor sit amet, consectetur adipisicing elit. A adipisci est eveniet, excepturi facere fugiat
                minus odit provident sit! At quaerat quo rem tempora tenetur vero? Cum magnam minus necessitatibus?
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. A adipisci est eveniet, excepturi facere
                fugiat
                minus odit provident sit! At quaerat quo rem tempora tenetur vero? Cum magnam minus necessitatibus?
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. A adipisci est eveniet, excepturi facere
                fugiat
                minus odit provid '''},
        "4": {
            "title": "Archit",
            "desc": ''' Lorem ipsum dolor sit amet, consectetur adipisicing elit. A adipisci est eveniet, excepturi facere fugiat
                minus odit provident sit! At quaerat quo rem tempora tenetur vero? Cum magnam minus necessitatibus?
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. A adipisci est eveniet, excepturi facere
                fugiat
                minus odit provident sit! At quaerat quo rem tempora tenetur vero? Cum magnam minus necessitatibus?
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. A adipisci est eveniet, excepturi facere
                fugiat
                minus odit provid '''}}
    return render(request, 'index.html', context=sq)


def home(request):
    sq = '''  <body style='background:black;'>
                <h1 style='text-align:center;
                font-size:120px;
                z-index:5;
                background:-webkit-linear-gradient(285deg, orange 10%,orange 45%,white 45%,white 65%,green 65%,green 100%);
                -webkit-background-clip:text;
                -webkit-text-stroke:0.5px blue;
                -webkit-text-fill-color:transparent;
                -webkit-font-family:'TeX Gyre Chorus';
                text-shadow:  1px 1px #fff,-1px 1px #fff,1px -1px #fff,-1px -1px #fff,1px 1px 5px #555;
                '>
                Naynesh
            </h1>
            </body>'''
    return HttpResponse(sq)


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name='login.html',
                  context={"form": form})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "register.html",
                  context={"form":form})
