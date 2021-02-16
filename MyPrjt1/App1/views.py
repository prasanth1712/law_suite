from django.shortcuts import render,reverse
from django.http import HttpResponseRedirect    
from django.views.generic import FormView , CreateView
from .forms import BankForm
from .models import Bank
from django.core.exceptions import ValidationError
# Create your views here.

def appindex(request):
    return render(request,'app1.html')


class BankView(CreateView):
    template_name = 'bank.html'
    form_class = BankForm
    success_url=''
    def post(self,request,*args,**kwargs):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            return render(request,self.template_name,context=self.get_context_data())




    
