from django.shortcuts import render,reverse
from django.views.generic import ListView
from App1.models import Client


class ClientListView(ListView):
    template_name = 'generic_list.html'
    model = Client
    context_object_name = 'object_list'
