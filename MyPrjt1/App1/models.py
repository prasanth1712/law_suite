from django.db import models

# Create your models here.
class WhoCols(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    created_by =  models.CharField(max_length=200,null=True,blank=True)
    date_updated = models.DateTimeField()
    updated_by =  models.CharField(max_length=200,null=True,blank=True)

    class Meta:
        abstract = True

class Address(models.Model):

    address_line_1 = models.CharField(max_length=200,null=True,blank=True)
    address_line_2 = models.CharField(max_length=200,null=True,blank=True)
    address_line_3 = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=200,null=True,blank=True)
    state = models.CharField(max_length=200,null=True,blank=True)
    pincode = models.CharField(max_length=200,null=True,blank=True)
    country = models.CharField(max_length=200,null=True,blank=True)

    class Meta:
        abstract = True

class Bank(Address,WhoCols):
    bank_name =  models.CharField(max_length=200,null=True,blank=True)
    account_number =  models.IntegerField(null=True,blank=True)
    rtgs_number = models.IntegerField(null=True,blank=True)
    ifsc_code =  models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.bank_name+' - '+self.city

class Company(Address,WhoCols):
    company_name =  models.CharField(max_length=200,null=True,blank=True)
    gst_number =  models.CharField(max_length=200,null=True,blank=True)
    registration_number =  models.CharField(max_length=200,null=True,blank=True)
    bank = models.ForeignKey(Bank,on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.company_name
    


class Client(Address,WhoCols):
    client_name =  models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.client_name


