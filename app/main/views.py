from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from requests import Request, Session

import os


# Create your views here.
def home_page(request):
    return render(request, 'main/home.html')

@login_required
def api_page(request):
    url = "http://api:8000/predict"

    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.getenv("API_KEY"),
    }

    session = Session()
    session.headers.update(headers)
    return render(request, "main/api_page.html")