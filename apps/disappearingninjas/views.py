# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect #, HttpResponse

# Create your views here.
def index(request):
    # print 'Run that function!'
    return render(request, 'disappearingninjas/index.html')

def ninjas(request):
    return render(request, 'disappearingninjas/allninjas.html')

def thisninja(request, color):
    if color == 'blue':
        ninja = 'leonardo'
    elif color == 'orange':
        ninja = 'michelangelo'
    elif color == 'red':
        ninja = 'raphael'
    elif color == 'purple':
        ninja = 'donatello'
    else:
        ninja = 'notapril'
    context = {
        'color': color,
        'ninja': ninja
    }
    return render(request, 'disappearingninjas/thisninja.html', context)
