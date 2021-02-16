from django.shortcuts import render,reverse
from django.views.generic import ListView , DetailView
from App1.models import Company


class CompanyListView(ListView):
    template_name = 'generic_list.html'
    model = Company
    context_object_name = 'object_list'


class CompanyDetailView(DetailView):
    template_name = 'generic_detail.html'
    model = Company
    context_object_name = 'object'
    
    