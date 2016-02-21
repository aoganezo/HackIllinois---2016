from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

import requests
import json

# Create your views here.
def search(request):
    payload = {'apikey': 'YZ6LCPhjR5aPavu1LWG6ezk8O0DEwidl', 'origin': request.GET.get('origin'), 'destination': request.GET.get('destination')}
    r = requests.get('https://api.sandbox.amadeus.com/v1.2/flights/inspiration-search', params=payload)

    return HttpResponse(json.dumps(r.json()))

def nearestairport(request):
    payload = {'apikey': 'YZ6LCPhjR5aPavu1LWG6ezk8O0DEwidl', 'latitude': request.GET.get('latitude'), 'longitude': request.GET.get('longitude')}
    r = requests.get('https://api.sandbox.amadeus.com/v1.2/airports/nearest-relevant', params=payload)

    return HttpResponse(json.dumps(r.json()))
