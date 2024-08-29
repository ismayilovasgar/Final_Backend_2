from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"home.html")

def pricing(request):
    return render(request,"pricing.html")


def features(request):
    return render(request,"features.html")

def download(request):
    return render(request,"download.html")

def lifestyle(request):
    return render(request,"lifestyle.html")