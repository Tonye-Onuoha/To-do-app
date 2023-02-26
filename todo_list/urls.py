from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('add',views.addtodoitem,name="add"),
    path('completed/<num>',views.completed,name="complete"),
    path('delete_complete/',views.deletecomplete,name="deletecomplete"),
    path('delete_all/',views.delete_all,name="delete_all")
]
