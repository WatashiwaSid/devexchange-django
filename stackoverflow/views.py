from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def custom_404(request, exception):
    return render(request, '404.html', status=404)