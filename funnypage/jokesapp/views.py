from django.shortcuts import render


# Create your views here.
def jokes(request):
    return render(request, "jokesapp/index.html")

