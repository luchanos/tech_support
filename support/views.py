from django.http import HttpResponse
from django.shortcuts import render
from uuid import uuid4


# Create your views here.
def create_order(request):
    order_id = uuid4()
    return HttpResponse(f'Order with id {order_id} has been created!')
