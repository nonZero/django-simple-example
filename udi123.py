from django.http import HttpResponse
from django.utils.html import escape

print "LOADING UDI123"


def foo(request):
    return HttpResponse("Hello {}!".format(escape(request.GET['name'])))


def printer(request, n=20, c="*"):
    n = int(n)
    return HttpResponse(c * n)
