from django.http import HttpResponse
from django.shortcuts import render
from app.models import *
import json

from django.db.models import Q
# Create your views here.

def index(request):
    return render(request,'index.html')


def get_data(request):
    data = []
    province = Province.objects.filter(~Q(name="")).filter(~Q(name="Cordoba省"))
    for i in province:
        temp = {}
        temp["name"] = i.name
        temp["value"] = i.goods_set.all().count()
        data.append(temp)
    return HttpResponse(json.dumps(data), content_type="application/json")