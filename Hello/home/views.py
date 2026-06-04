from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "variable1":"I am Solider boy",
        "variable2": "Homelander the god"
    }
    return render(request, 'index.html')
    # return HttpResponse("this is home page")


def home(request):
    return render(request, 'home.html')
    # return HttpResponse("this is about page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is services page")

def contact(request):
    
    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")