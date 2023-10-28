from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from app.models import Client

# Create your views here.
def index(request):
    return render(request, "index.html")

def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(
            f"username = {username}\npassword = {password}"
        )
        all_username = [client.username for client in Client.objects.all()]
        if username in all_username:
            all_client = [client for client in Client.objects.all()]
            for client in all_client:
                if password == client.password:
                    return render(request, "homepage.html", {"username":username})
            
        return redirect('signin')
    else:
        return render(request, 'signin.html')
    
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(
            f"username = {username}\npassword = {password}"
        )
        all_username = [client.username for client in Client.objects.all()]
        if username in all_username:
            all_client = [client for client in Client.objects.all()]
            for client in all_client:
                if password == client.password:
                    return render(request, "homepage.html", {"username":username})
            
        return redirect('login')
    else:
        return render(request, 'login.html')
    
def homepage(request):
    all_client = Client.objects.all()
    return render(request, "homepage.html", {"all_client":all_client})