from django.urls import path

from . import views

urlpatterns = [

    path('',views.index,name='home'),
    path('signin/',views.signin,name='signin'),
    path('panel/',views.panel,name='panel'),
    path('new_home/',views.new_home,name='new_home'),
    path('satlik_list/',views.satlik_list,name='satlik_list'),
    path('edit_satlik/<str:pk>/',views.edit_satlik,name='edit_satlik'),
    path('delete_satlik/<str:pk>/',views.delete_satlik,name='delete_satlik'),
    path('new_kiralik/',views.new_kiralik,name='new_kiralik'),
]
