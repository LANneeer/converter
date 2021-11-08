import json

from django.shortcuts import render
from django.http import HttpResponse
from core.forms import TranslateForm
from translater.translate import cyrillic_to_latin_text


def index(request):
    form = TranslateForm(request.POST, initial={'to': 'sample value'})
    return render(request, template_name='core/index.html', context={'form': form})


def translate(request):
    text = request.GET['from']
    result = {'result': cyrillic_to_latin_text(text)}
    return HttpResponse(json.dumps(result))
