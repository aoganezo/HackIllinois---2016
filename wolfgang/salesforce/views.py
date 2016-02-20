from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render

import requests
import urllib

# Create your views here.

def loginrequest(request):

    params = {"response_type": "code",
              "client_id": "3MVG9uudbyLbNPZOEkKHOygDnrFCXHj1DpAYCpvC4vattO5e2fOG7aeh_E3J11tPVPGnbUI0KI0GCUY2qhDlX",
              "redirect_uri": "https://127.0.0.1:8000/salesforce/login"}

    context = {
        'login_url': 'https://login.salesforce.com/services/oauth2/authorize?' + urllib.parse.urlencode(params),
    }

    return render(request, 'salesforce/index.html', context)

def login(request):

    r = requests.post('https://login.salesforce.com/services/oauth2/token', params=payload)
    request_json = r.json()
    access_token = request_json['access_token']
    instance_url = request_json['instance_url']

    headers = {'Authorization': 'Bearer ' + access_token}

    # get a particular contact information
    r = requests.get(instance_url + '/services/data/v36.0/sobjects/Contact/00336000004QgTxAAK', params=payload, headers=headers)

    # get a list of views for a particular sobject
    #r = requests.get(instance_url + '/services/data/v36.0/sobjects/Lead/listviews', params=payload, headers=headers)
    #r = requests.get(instance_url + '/services/data/v36.0/sobjects/Account/listviews', params=payload, headers=headers)
    #r = requests.get(instance_url + '/services/data/v36.0/sobjects/Contact/listviews', params=payload, headers=headers)

    # get all of the results for a particular view
    #r = requests.get(instance_url + '/services/data/v36.0/sobjects/Lead/listviews/00B36000002PRKyEAO/results', params=payload, headers=headers)
    #r = requests.get(instance_url + '/services/data/v36.0/sobjects/Account/listviews/00B36000002PRM5EAO/results', params=payload, headers=headers)
    #r = requests.get(instance_url + '/services/data/v36.0/sobjects/Contact/listviews/00B36000002PRM6EAO/results', params=payload, headers=headers)

    context = {
        logged_in: logged_in,
        'results': r.json(),
    }

    return render(request, 'salesforce/index.html', context)
