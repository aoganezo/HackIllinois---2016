from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect, render

import json
import requests
import urllib

# Create your views here.
def index(request):

    # get a particular contact information
    r = requests.get(request.session['instance_url'] + '/services/data/v36.0/sobjects/Contact/00336000004QgTxAAK', params=request.session['payload'], headers=request.session['headers'])

    # get a list of views for a particular sobject
    #r = requests.get(instance_url + '/services/data/v36.0/sobjects/Lead/listviews', params=payload, headers=headers)
    #r = requests.get(instance_url + '/services/data/v36.0/sobjects/Account/listviews', params=payload, headers=headers)
    #r = requests.get(instance_url + '/services/data/v36.0/sobjects/Contact/listviews', params=payload, headers=headers)

    # get all of the results for a particular view
    #r = requests.get(instance_url + '/services/data/v36.0/sobjects/Lead/listviews/00B36000002PRKyEAO/results', params=payload, headers=headers)
    #r = requests.get(instance_url + '/services/data/v36.0/sobjects/Account/listviews/00B36000002PRM5EAO/results', params=payload, headers=headers)
    #r = requests.get(instance_url + '/services/data/v36.0/sobjects/Contact/listviews/00B36000002PRM6EAO/results', params=payload, headers=headers)

    context = {
        'results': r.json()
    }

    return render(request, 'mainapp/index.html', context)

def getUserInformation(request):
    # get a list of views for a particular sobject
    r = requests.get(request.session['instance_url'] + "/services/data/v36.0/query/?q=SELECT FirstName, LastName, MailingAddress FROM Contact WHERE ID = '" + request.GET.get('id') + "'", params=request.session['payload'], headers=request.session['headers'])
    request_json = r.json()
    return HttpResponse(json.dumps(request_json['records']))


def getContacts(request):
    # get a list of views for a particular sobject
    r = requests.get(request.session['instance_url'] + "/services/data/v36.0/query/?q=SELECT ID, FirstName, LastName, MailingAddress FROM Contact", params=request.session['payload'], headers=request.session['headers'])
    request_json = r.json()
    request.session['contacts'] = json.dumps(request_json['records'])

    return HttpResponse(request.session['contacts']);

def getAccounts(request):
    r = requests.get(request.session['instance_url'] + '/services/data/v36.0/sobjects/Account/listviews', params=request.session['payload'], headers=request.session['headers'])
    request_json = r.json()
    accounts = {}
    for i in range(len(request_json['listviews'])):
        if request_json['listviews'][i]['developerName'] == "AllAccounts":
            accounts = request_json['listviews'][i]
            break

    # get all of the results for a particular view
    r = requests.get(request.session['instance_url'] + accounts['url'] + '/results', params=request.session['payload'], headers=request.session['headers'])
    request_json = r.json()
    request.session['accounts'] = json.dumps(request_json['records'])

    return HttpResponse(request.session['accounts'])

def getLeads(request):
    r = requests.get(request.session['instance_url'] + '/services/data/v36.0/sobjects/Lead/listviews', params=request.session['payload'], headers=request.session['headers'])
    request_json = r.json()
    all_open_leads = {}
    for i in range(len(request_json['listviews'])):
        if request_json['listviews'][i]['developerName'] == "AllOpenLeads":
            all_open_leads = request_json['listviews'][i]
            break

    # get all of the results for a particular view
    r = requests.get(request.session['instance_url'] + all_open_leads['url'] + '/results', params=request.session['payload'], headers=request.session['headers'])
    request_json = r.json()
    request.session['leads'] = json.dumps(request_json['records'])

    return HttpResponse(request.session['leads'])

def getPayload(request):
    return HttpResponse(request.session['payload']);

def getHeaders(request):
    return HttpResponse(request.session['headers']['Authorization']);

def getInstanceUrl(request):
    return HttpResponse(request.session['instance_url']);
