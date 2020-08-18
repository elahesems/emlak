from django.shortcuts import render

# Create your views here.
from ui.models import Sliders


def index(request):
    sliders = Sliders.objects.all()
    context = {'sliders':sliders}
    return render(request,'front/index.html',context)