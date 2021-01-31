from django.http import HttpResponse
from django.shortcuts import render
from uuid import uuid4
from django.template import loader


# Create your views here.
def create_order(request):
    order_id = uuid4()
    return HttpResponse(f'Order with id {order_id} has been created!')


def main_page(request):
    t = loader.get_template('support/templates/index.html')
    context = {'foo': 'bar'}
    return HttpResponse(t.render(context, request))
