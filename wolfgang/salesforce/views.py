from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render

import json
import requests
import urllib

# Create your views here.
def index(request):
    return render(request, 'salesforce/index.html')

def loginrequest(request):

    params = {"response_type": "code",
              "client_id": "3MVG9uudbyLbNPZOEkKHOygDnrFCXHj1DpAYCpvC4vattO5e2fOG7aeh_E3J11tPVPGnbUI0KI0GCUY2qhDlX",
              "redirect_uri": "https://127.0.0.1:8000/salesforce/login"}

    context = {
        'login_url': 'https://login.salesforce.com/services/oauth2/authorize?' + urllib.parse.urlencode(params),
    }

    return render(request, 'salesforce/login.html', context)

def login(request):
    payload = {'code': request.GET.get('code'), 'client_id': '3MVG9uudbyLbNPZOEkKHOygDnrFCXHj1DpAYCpvC4vattO5e2fOG7aeh_E3J11tPVPGnbUI0KI0GCUY2qhDlX', 'client_secret': '5507061653828921927', 'grant_type': 'authorization_code', 'redirect_uri': 'https://127.0.0.1:8000/salesforce/login'}
    r = requests.post('https://login.salesforce.com/services/oauth2/token', params=payload)

    request_json = r.json()
    access_token = request_json['access_token']
    instance_url = request_json['instance_url']

    headers = {'Authorization': 'Bearer ' + access_token}

    request.session['payload'] = payload
    request.session['headers'] = headers
    request.session['instance_url'] = instance_url

    return render(request, 'salesforce/login.html')
