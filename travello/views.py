from django.shortcuts import render

from travello.models import Destination


def index(request):
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})
