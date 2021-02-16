from django.shortcuts import render,reverse
from django.views.generic import ListView
from App1.models import Stage


class CaseStageListView(ListView):
    template_name = 'generic_list.html'
    model = Stage
    context_object_name = 'object_list'
