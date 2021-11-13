from os import name
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("e_books",views.e_books,name='e_books'),
    path("buy_books",views.buy_books,name='buy_books'),
    path("contact_us",views.contact_us,name='contact_us'),
    path("submit_contact_form",views.submit_contact_form,name='submit_contact_form'),
]
