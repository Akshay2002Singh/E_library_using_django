from django.shortcuts import render
from home.models import contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")

def e_books(request):
    return render(request,"e_books.html")

def buy_books(request):
    return render(request,"buy_books.html")

def contact_us(request):
    return render(request,"contact_us.html")

def submit_contact_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        temp_contact = contact(name=name,email=email,phone=phone,message=message)
        temp_contact.save()
        messages.success(request,"Your form has been submitted succesfully")
        return render(request,'contact_us.html')