from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse("ござござ！")

def temp(request):
    template = loader.get_template('app/index.html')
    context = {'goza': 'ござ'}
    return HttpResponse(template.render(context, request))
