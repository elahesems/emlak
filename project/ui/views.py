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




            new = Homes(name=name,price=price,price_unit=price_unit,bathrooms=bathrooms,square=square,parking=parking,rooms=rooms,image=image,address=address,type=type)
            new.save()

            return redirect('satlik_list')
        except:
            pass
    return render(request, 'back/new_satlik.html')

def satlik_list(request):
    homes=Homes.objects.filter(type='satlik')

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

def delete_method(request,pk):
    home = Homes.objects.get(pk=pk)
    if home.type == 'satlik':
        home.delete()
        return redirect('satlik_list')
    elif home.type == 'kiralik':
        home.delete()
        return redirect('new_kiralik_list')





def new_kiralik(request):
    form = CreateHome()
    if request.method == "POST":
        try:
            form = CreateHome(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('new_kiralik_list')
            else:
                messages.info(request, 'valid değil!')
                return redirect('new_kiralik')
        except:
            messages.info(request, 'resim veya bilgiler gelmedi!')
            return redirect('new_kiralik')

    context = {'form':form}

    return render(request, 'back/new_kiralik.html', context)


def new_kiralik_list(request):
    kiraliklar = Homes.objects.filter(type='kiralik')
    context = {'homes':kiraliklar}
    return render(request, 'back/new_kiralik_list.html', context)


def edit_kiralik(request,pk):
    home = Homes.objects.get(pk=pk)
    form = CreateHome(instance=home)
    if request.method == "POST":
        form = CreateHome(request.POST,request.FILES,instance=home)
        if form.is_valid():
            try:
                form.save()
                return redirect('new_kiralik_list')
            except:
                messages.info(request, 'Error occurred! try again!')
                return redirect('edit_kiralik')
        else:
            messages.info(request, 'Error occurred! try again!')
            return redirect('edit_kiralik')

    context={'form':form}
    return render(request,'back/edit_kiralik.html',context)