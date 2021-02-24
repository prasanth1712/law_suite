from django.shortcuts import render,reverse
from django.views.generic import ListView,DetailView
from App1.models import Stage


class CaseStageListView(ListView):
    template_name = 'generic_list.html'
    model = Stage
    context_object_name = 'object_list'
    extra_context = {'dynamic_url':'App1:stage_detail'}


class CaseStageDetailView(DetailView):
    template_name = 'generic_detail.html'
    model = Stage
    context_object_name = 'object'