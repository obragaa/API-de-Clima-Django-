import os

import requests
from django.shortcuts import render
from .models import Cidade


def index(request):
    # a chave da API vem do ambiente, nunca do código
    chave = os.environ.get('OPENWEATHER_API_KEY', '')
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=' + chave

    if request.method == 'POST':
        cidade = request.POST['cidade']
        r = requests.get(url.format(cidade)).json()

        cidade_clima = {
            'cidade': cidade,
            'temperatura': r['main']['temp'],
            'descricao': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }

        Cidade.objects.create(nome=cidade)

    else:
        cidade_clima = {}

    return render(request, 'clima/clima.html', cidade_clima)
