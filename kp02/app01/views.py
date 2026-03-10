from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def response(request):
    return HttpResponse("Hello World")


def response2(request):
    html_text = '''
    <html>
    <head>
    <style>
    h1 {text-align: center;}
    p {text-align: center;}
    div {text-align: center;}
    </style>
    </head>
    <body>

    <h1>Резюме</h1>
    <p>Я Шишлаков Володимир студент групи ПІ-31 навчаюся на спеціальності 175 в КПІ</p>
    <div>Мої хобі:
    <li>Комп'ютерні ігри</li>
    <li>Кіно/серіали</li>
    <li>Музика</li>
    </div>

    </body>
    </html>
    '''

    return HttpResponse(html_text)