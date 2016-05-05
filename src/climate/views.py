from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.db.models import Max
import json


import app.main
from climate.models import Climate

# Create your views here.
def index(request):
    
    #remove the last_update field
    return HttpResponse(_stream_index(request.GET), content_type='application/json')
    
def _stream_index(queryDict):
    query = Climate.objects.values('region', 'type', 'year', 'month').annotate(last_update=Max('lastUpdate'))
    query = query.filter(**queryDict.dict())
    
    yield '['
    for c in query.order_by('year','month'):
        del c['last_update']
        yield "%s,"%c
    yield ']'
    

def pull(request):
    return HttpResponse(_stream_pull(), content_type='application/json')

def _stream_pull():
    yield '['
    for c in app.main.pull(Climate):
        yield "{%s},"%c
    yield ']'
    



