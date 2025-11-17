from django.http import HttpResponse

def hello_world(request):
    return(HttpResponse('<body style="padding: 0; margin: 0; background-color: #bbb;"><h1 style="text-align: center; font-family: monospace; padding-top: 700px;">Hello, django-World!</h1></body>'))
