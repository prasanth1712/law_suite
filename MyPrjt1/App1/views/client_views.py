from django.shortcuts import render,reverse
from django.views.generic import ListView,DetailView
from App1.models import Client
import logging

class ClientListView(ListView):
    template_name = 'generic_list.html'
    model = Client
    context_object_name = 'object_list'
    extra_context = {'dynamic_url':'App1:client_detail'}
    
class ClientDetailView(DetailView):
    template_name = 'generic_detail.html'
    model = Client
    context_object_name = 'object'