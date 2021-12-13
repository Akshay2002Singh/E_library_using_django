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
    path("login_user",views.login_user,name='login_user'),
    path("login_user_form",views.login_user_form,name='login_user_form'),
    path("create_user",views.create_user,name='create_user'),
    path("create_user_form",views.create_user_form,name='create_user_form'),
    path("log_out",views.log_out,name='log_out'),
    path("upload_book_page",views.upload_book_page,name='upload_book_page'),
    path("upload_book_by_user",views.upload_book_by_user,name='upload_book_by_user'),
]
