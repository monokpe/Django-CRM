from .models import Record
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout


def home(request):
    records = Record.objects.all()

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
    return render(request, "home.html", {"records": records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...".title())
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(
                request, "You have successfully Registered! welcome!".title()
            )
            return redirect("home")
        return render(request, "register.html", {"form": form})

    form = SignUpForm()
    return render(request, "register.html", {"form": form})


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, "record.html", {"customer_record": customer_record})
    messages.error(request, "You must be signed in to view that page...".title())
    return redirect("home")


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "You have successfully deleted a record.".title())
        return redirect("home")
    messages.error(request, "You must be signed in to do that...".title())
    return redirect("home")


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "record successfully added.".title())
                return redirect("home")
        return render(request, "add_record.html", {"form": form})
    else:
        messages.success(request, "You must be logged in to do that.".title())
        return redirect("home")


def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "record successfully updated.".title())
            return redirect("home")
        return render(request, "update_record.html", {"form": form})
    else:
        messages.success(request, "You must be logged in to do that.".title())
        return redirect("home")
