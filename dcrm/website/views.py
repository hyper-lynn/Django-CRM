from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from . import forms
from .models import Record
from django.db import models

# Create your views here.
def home(request):
    records = Record.objects.all()
    #check to see if login
    if request.method == "POST":
        username = request.POST['user_id']
        password = request.POST['password']
        #authenticate
        user = authenticate(request , username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f"You are now Login. Welcome back {username}.")
            return redirect('home')
        else:
            messages.success(request,"There was an error , Login again!")
            return redirect('home')
    else:
        return render(request,'website/home.html',{'records':records})

def logout_user(request):
    logout(request)
    messages.success(request,"Logout Successfully!")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have been Register!")
            return redirect('home')
    else:
        form =  forms.SignUpForm()

        return render(request,"website/register.html",{'form':form})
    
    return render(request,"website/register.html",{'form':form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request,'website/record.html',{'customer_record':customer_record})
    else:
        messages.success(request,"Access Denied ! You must Login first! ")
        return redirect('home')

def delete_record(request,pk):
    delete_record = Record.objects.get(id=pk)
    delete_record.delete()
    # models.Model.save()
    messages.success(request,"Record Deleted successfully ")
    return redirect('home')


def add_record(request):
    form = forms.AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
        return render(request, 'website/add_record.html', {'form':form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')
    
    
def update_record(request,pk):
	if request.user.is_authenticated:
		current_record = forms.Record.objects.get(id=pk)
		form = forms.AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'website/update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
    


    
    