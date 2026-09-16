from django.shortcuts import render
def home(request):
    return render(request,'home.html')
def journal(request):
    return render(request, "journal.html")
