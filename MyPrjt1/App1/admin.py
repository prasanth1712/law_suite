from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Client,Company,Bank,Court,Case,Stage

# Register your models here.

@admin.register(Company)
class CompanyAdmin(ModelAdmin):
    fields = ('company_name',('gst_number','registration_number'),'bank'\
             ,('address_line_1','address_line_2','address_line_3'),('state','city','pincode','country') \
            ,('created_by','updated_by')
             )

@admin.register(Court)
class CourtAdmin(ModelAdmin):
    fields = ('court_name'\
             ,('address_line_1','address_line_2','address_line_3'),('state','city','pincode','country') \
             ,('created_by','updated_by')
             )

@admin.register(Client)
class ClientAdmin(ModelAdmin):
    fields = ('client_name'\
             ,('address_line_1','address_line_2','address_line_3'),('state','city','pincode','country') \
             ,('created_by','updated_by')
             )
@admin.register(Bank)
class BankAdmin(ModelAdmin):
    fields = ('bank_name',('account_number','rtgs_number','ifsc_code')\
             ,('address_line_1','address_line_2','address_line_3'),('state','city','pincode','country') \
             ,('created_by','updated_by')
             )

@admin.register(Stage)
class StageAdmin(ModelAdmin):
    fields = ('stage_name','stage_description'\
             ,('created_by','updated_by')
             )

@admin.register(Case)
class CaseAdmin(ModelAdmin):
    fields = (('client','court_name','case_number')\
             ,'description'
             ,'next_date'
             ,('created_by','updated_by')
             )