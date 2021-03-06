from django.shortcuts import render,reverse
from django.views.generic import ListView,DetailView
from App1.models import Bank


class BankListView(ListView):
    template_name = 'generic_list.html'
    model = Bank
    context_object_name = 'object_list'
    extra_context = {'dynamic_url':'App1:bank_detail'}


class BankDetailView(DetailView):
    template_name = 'generic_detail.html'
    model = Bank
    context_object_name = 'object'














# from .base_imports import *

# class BankView(CreateView):
#     template_name = 'bank.html'
#     form_class = BankForm
#     success_url=''
#     def post(self,request,*args,**kwargs):
#         form = self.form_class(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#         else:
#             return render(request,self.template_name,context=self.get_context_data())


