from django.shortcuts import render, redirect


def welcome(request):
    return render(request, 'registration/welcome.html')
