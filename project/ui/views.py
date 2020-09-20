from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import CreateAdminUserForm, CreateHome
from .models import Sliders, Homes
from django.contrib.auth.decorators import login_required


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
            return redirect('panel')

    return render(request,'front/signin.html')



def panel(request):

    return render(request, 'back/panel.html')

def new_home(request):
    if request.method =="POST":

        try:

            name=request.POST.get('name')
            price=request.POST.get('price')
            price_unit=request.POST.get('price_unit')
            bathrooms=request.POST.get('bathrooms')
            square=request.POST.get('square')
            parking=request.POST.get('parking')
            rooms=request.POST.get('rooms')
            image=request.FILES.get('image')
            address=request.POST.get('address')
            type=request.POST.get('type')

            if price is int:
                pass
            else:
                messages.info(request, 'please enter an integer to price')
                return redirect('new_home')

            new = Homes(name=name,price=price,price_unit=price_unit,bathrooms=bathrooms,square=square,parking=parking,rooms=rooms,image=image,address=address,type=type)
            new.save()

            return redirect('satlik_list')
        except:
            pass
    return render(request,'back/new_home.html')

def satlik_list(request):
    homes=Homes.objects.all()
    context={'homes':homes}

    return render(request,'back/satlik_list.html',context)

def edit_satlik(request,pk):
    home=Homes.objects.get(pk=pk)
    if request.method == "POST":
        try:

            name = request.POST.get('name')
            price = request.POST.get('price')
            price_unit = request.POST.get('price_unit')
            bathrooms = request.POST.get('bathrooms')
            square = request.POST.get('square')
            parking = request.POST.get('parking')
            rooms = request.POST.get('rooms')
            image = request.FILES.get('image')
            address = request.POST.get('address')
            type = request.POST.get('type')



            new = Homes(name=name, price=price, price_unit=price_unit, bathrooms=bathrooms, square=square,
                        parking=parking, rooms=rooms, image=image, address=address, type=type)
            new.save()

            return redirect('satlik_list')
        except:
            pass


    context = {'home': home}
    return render(request,'back/edit_satlik.html',context)

def delete_satlik(request,pk):
    home = Homes.objects.get(pk=pk)
    home.delete()
    return redirect('satlik_list')




def new_kiralik(request):
    form = CreateHome()
    if request.method == "POST":
        try:
            form = CreateHome(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('panel')
            else:
                messages.info(request, 'valid değil!')
                return redirect('new_kiralik')
        except:
            messages.info(request, 'resim veya bilgiler gelmedi!')
            return redirect('new_kiralik')

    context = {'form':form}

    return render(request, 'back/new_kiralik.html', context)