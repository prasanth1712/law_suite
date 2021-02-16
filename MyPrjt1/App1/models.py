from django.db import models

# Create your models here.
class WhoCols(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    created_by =  models.CharField(max_length=200,null=True,blank=True)
    date_updated = models.DateTimeField(auto_now_add=True)
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
    bank_name =  models.CharField(max_length=200)
    account_number =  models.IntegerField(unique=True,)
    rtgs_number = models.IntegerField()
    ifsc_code =  models.CharField(max_length=200)

    def __str__(self):
        return self.bank_name
    
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(rtgs_number__gt=0),name='rtgs_number'),
            models.CheckConstraint(check=models.Q(rtgs_number__gt=0),name='account_number')
        ]

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

class Court(Address,WhoCols):
    court_name =  models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.court_name

class Stage(WhoCols):
    stage_name =  models.CharField(max_length=200,null=True,blank=True)
    stage_description =  models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.stage_name

class Case(WhoCols):
    case_number = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    description =  models.CharField(max_length=2000,null=True,blank=True)
    court_name =  models.ForeignKey(Court,on_delete=models.CASCADE)
    stage =  models.ForeignKey(Stage,on_delete=models.CASCADE)
    next_date = models.DateTimeField()

    def __str__(self):
        return self.case_number+' - '+self.client+' - '+self.stage