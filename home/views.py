from django.http import response
from django.shortcuts import redirect, render
from home.models import contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login ,logout
from django.conf import settings
from django.core.mail import send_mail
from home.models import upload_book
from django.http.response import HttpResponse


# Create your views here.
def index(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()
        
    return render(request,"index.html",context)

def e_books(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()
        context["extra_books"] = upload_book.objects.all()
    return render(request,"e_books.html",context)

def buy_books(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()
    return render(request,"buy_books.html",context)

def contact_us(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()
    return render(request,"contact_us.html",context)

def submit_contact_form(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        temp_contact = contact(name=name,email=email,phone=phone,message=message)
        temp_contact.save()
        messages.success(request,"Your form has been submitted succesfully")

        # send msg to admin
        subject = f'Got complain from {name}'
        message = f'Issue : {message}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['06akshay2002@gmail.com', ]
        send_mail( subject, message, email_from, recipient_list )

        # send msg to user
        subject = f'Contact E-library'
        message = f'Hello {name},\nOur team will contact you soon.\nThank you'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        return render(request,'contact_us.html',context)

def login_user(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()
    return render(request,"sign_in.html",context)

def login_user_form(request):

    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username,password= password)
        if user is not None:
            login(request,user)
            return redirect ("/")
        else:
            return redirect("/login")

def create_user(request):
    return render(request,"sign_up.html")

def create_user_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username,email,password)
        user.first_name=name
        user.save()
        messages.success(request,"You are now an user.")
        return render(request,'sign_up.html')

def log_out(request):
    logout(request)
    return redirect("/")

def upload_book_page(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()
    return render(request,"upload_book_page.html",context)

def upload_book_by_user(request):
    context = {
        "login" : 0
        }
    if request.user.is_authenticated:
        context["login"]=1
        context["user"]=request.user.get_username()

    if request.method == "POST":
        temp_book= upload_book()
        temp_book.detail = request.POST.get('book_name')
        temp_book.image = request.FILES['thumbnail']
        temp_book.book = request.FILES['file']
        temp_book.save()
        messages.success(request,"Your book uploaded succesfully")

        # send msg to admin
        subject = f'Book uploaded by {request.user.get_username()}'
        message = f'{request.user.get_username()} uploaded a book.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['06akshay2002@gmail.com', ]
        send_mail( subject, message, email_from, recipient_list )

        # send msg to user
        subject = f'BOOK REVIEW'
        message = f'Hello {request.user.get_username()},\nYou uploaded a book on Elite library.\nYour book will be reviewed soon, if anything malacious found then we will remove it.\nThank you for your contribution.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.user.email, ]
        send_mail( subject, message, email_from, recipient_list )

        return render(request,'upload_book_page.html',context)