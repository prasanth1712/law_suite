from django.forms import ModelForm
from django.core.exceptions import NON_FIELD_ERRORS
from .models import Bank,Case,Client,Company,Court 

class BankForm(ModelForm):
    class Meta:
        model = Bank
        fields = ('bank_name','account_number','rtgs_number','ifsc_code'\
             ,'address_line_1','address_line_2','address_line_3','state','city','pincode','country'
             )
        exclude = ('created_by','updated_by')
        