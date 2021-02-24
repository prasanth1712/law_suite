from django.shortcuts import render,reverse
from django.views.generic import ListView , DetailView
from App1.models import Company


class CompanyListView(ListView):
    template_name = 'generic_list.html'
    model = Company
    context_object_name = 'object_list'
    extra_context = {'dynamic_url':'App1:company_detail'}


class CompanyDetailView(DetailView):
    template_name='company_detail.html'
    model = Company
    context_object_name = 'company'