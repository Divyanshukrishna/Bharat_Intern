from django.shortcuts import render
from .models import Form
# Create your views here.

def homepage(request):
    if request.method == 'POST':
        fname=request.POST.get('fname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        en=Form(fname=fname, username=username, password=password ,email=email, phone=phone, cpassword=cpassword)
        en.save()
    return render(request,"index.html")