from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.db.models import Max
import json


import app.main
from climate.models import Climate


def index(request):
    
    #remove the last_update field
    return HttpResponse(_stream_index(request.GET), content_type='application/json')
    
def _stream_index(queryDict):
    query = Climate.objects.values('region', 'type', 'year', 'month', 'data').annotate(last_update=Max('lastUpdate'))
    query = query.filter(**queryDict.dict())
    
    yield '['
    for c in query.order_by('year','month'):
        del c['last_update']
        yield ("%s,"%c).replace("u'", "'").replace("'", '"')
    yield '{}]'
    

def pull(request):
    return HttpResponse(_stream_pull(), content_type='application/json')

def _stream_pull():
    yield '['
    for c in app.main.ClimateApp(Climate).pull():
        yield "%s"%c
    yield ']'
    

def options(request):
    op_dict = {}
    _add_options(op_dict, 'region')
    _add_options(op_dict, 'type')
    _add_options(op_dict, 'year', True)
    _add_options(op_dict, 'month', True)
    return HttpResponse(json.dumps(op_dict), content_type='application/json')
        
def _add_options(op_dict, key, numeric=False):
    op_list = []
    for i in Climate.objects.values(key).distinct():
        op_list.append(i[key])
    if numeric:
        op_list = [int(x) for x in op_list]

    op_dict[key] = sorted(op_list)


