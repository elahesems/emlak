from django.shortcuts import render

from ui.models import Sliders, Homes


def index(request):
    sliders = Sliders.objects.all()
    homes = Homes.objects.all()

    context = {'sliders':sliders,'homes':homes}
    return render(request,'front/index.html',context)




