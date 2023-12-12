from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.
def home(request):
    books = Books.objects.all()    
    return render(request, 'home.html', {'books':books})

def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = AddBookForm()
        return render(request, 'add_book.html', {'form': form})

def book(request, pk):
    book = Books.objects.get(id=pk)
    return render(request, 'book.html', {'book':book})

def issue_book(request, pk):
    book = Books.objects.get(id=pk)
    book.status = 'ISSUED'
    book.save()
    return redirect('home')
    
def return_book(request, pk):
    book = Books.objects.get(id=pk)
    book.status = 'RETURNED'
    book.save()
    return redirect('home')

def delete_book(request, pk):
    book = Books.objects.get(id=pk)
    book.delete()
    return redirect('home')

def update_book(request, pk):
    book = Books.objects.get(id=pk)
    if request.method == 'POST':
        form = AddBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = AddBookForm(instance=book)
        return render(request, 'update_book.html', {'form': form})