from django.shortcuts import render

from travello.models import Destination


def index(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.price = 700
    dest1.offer=True
    dest1.img='destination_1.jpg'
    dest1.desc = 'Nulla pretium tincidunt felis, nec.'
    dest2 = Destination()
    dest2.name = 'Delhi'
    dest2.price = 900
    dest2.img='destination_2.jpg'
    dest2.desc = 'do do odo dododododo.'
    dest3 = Destination()
    dest3.name = 'Kolkata'
    dest3.price = 500
    dest3.img='destination_3.jpg'
    dest3.desc = 'Gooooood gud!!!!!.'
    dests=[dest1,dest2,dest3]
    return render(request, 'index.html', {'dests': dests})
