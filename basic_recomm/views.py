from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .make_font_db import make_db_font
from .compare_sim import search_most_sim
from django.http import JsonResponse


def index(request):
    #make_db_font()
    return render(request, 'basic_recomm/base.html')

def search_font(request):
    selected_key=request.GET.getlist('selected_key[]')
    #selected_key = json.loads(request.GET.get('selected_key'))
    #selected_key=request.GET.get('selected_key')
    print("******************************************")
    print(selected_key)
    print("******************************************")
    l1,l2=search_most_sim(selected_key)

    context={'sim1':l1, 'sim2':l2}
    return JsonResponse(context)

