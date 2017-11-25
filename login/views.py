from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response

def show_index(request):
    t = get_template('index.html')
    html = t.render()
    return HttpResponse(html)


