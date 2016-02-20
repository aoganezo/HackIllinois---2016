from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

import requests

# Create your views here.
def index(request):
    payload = {'apikey': 'YZ6LCPhjR5aPavu1LWG6ezk8O0DEwidl', 'origin': 'NYC', 'destination': 'LAX'}
    r = requests.get('https://api.sandbox.amadeus.com/v1.2/flights/inspiration-search', params=payload)

    context = {
        'results': r.json()['results'],
    }

    return render(request, 'amadeus/index.html', context)
