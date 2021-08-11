from django.shortcuts import render, HttpResponse
import os

# Create your views here.

def index(request):
    files = [f for f in os.listdir("../pet") if os.path.isfile(os.path.join("../pet", f))]
    context = {
        'files': files
    }
    print(files)
    return render(request, "main/index.html.jinja", context)