from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PredictApiForm
from requests import Request, Session
import json
import os


# Create your views here.
def home_page(request):
    return render(request, 'main/home.html')

@login_required
def api_page(request):
    url = "http://api:8000/predict"

    headers = {
    'Accepts': 'application/json',
    }

    session = Session()
    session.headers.update(headers)
    

    if request.method == "POST":
        form = PredictApiForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            input_data = json.dumps(form.cleaned_data)
            response = session.post(url, data=input_data)
            
            data = json.loads(response.text)
            print(data)
            form.save()
            
            
            return render(request, "main/api_perso.html", context={"data" : data})

    else:
        form = PredictApiForm()
    return render(request, "main/api_page.html", context={"form": form})