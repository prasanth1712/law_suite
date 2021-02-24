from django.test import TestCase
from App1.models import Bank
# Create your tests here.

class Test_Bank(TestCase):
    def setUp(self):
        print('setup')
    
    def test_1(self):
        assert(1,1)

    def test_bank(self):
        b = Bank()
        b.account_number='123'
        b.bank_name = 'ABC'
        b.rtgs_number='111'
        b.ifsc_code='IFSC'
        b.save()
        bl=len(Bank.objects.all())
        assert(bl,1)

    def tearDown(self):
        print('tear_down')
