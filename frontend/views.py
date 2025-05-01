from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def register_page(request):
    return render(request, 'register.html')

def login_page(request):
    return render(request, 'login.html')

def deposit_form_page(request):
    return render(request, 'deposit_form.html')

def deposit_list_page(request):
    return render(request, 'deposit_list.html')

@login_required
def new_deposit_page(request):
    return render(request, "new_deposit.html")