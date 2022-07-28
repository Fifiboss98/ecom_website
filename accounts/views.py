from django.shortcuts import render

def sign_up(request):
    return render(request, 'signup.html')

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    return render(request, 'logout.html')