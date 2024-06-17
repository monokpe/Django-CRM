from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout


def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "You have been logged in!".title())
            return redirect("home")
        messages.error(
            request, "There was an error logging in, please try again...".title()
        )
        return redirect("home")
    return render(request, "home.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...".title())
    return redirect("home")


def register_user(request):
    return render(request, "register.html", {})
