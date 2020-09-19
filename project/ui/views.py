from django.shortcuts import render
from django.contrib.auth import authenticate
from .forms import CreateAdminUserForm
from .models import Sliders, Homes


def index(request):
    sliders = Sliders.objects.all()
    homes = Homes.objects.all()
    context = {'sliders':sliders,'homes':homes}
    return render(request,'front/index.html',context)

def signin(request):
    if request.method == "POST":
        user=request.POST.get("username")
        password=request.POST.get("password")
        if authenticate(username=user,password=password):
            print('ok')

    return render(request,'front/signin.html')


