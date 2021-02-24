from django.urls import path
from App1.views.company_views import CompanyListView,CompanyDetailView
from App1.views.bank_views import BankListView , BankDetailView
from App1.views.client_views import ClientListView , ClientDetailView
from App1.views.case_stage_views import CaseStageListView , CaseStageDetailView

app_name = 'App1'

urlpatterns = [
    path('company',CompanyListView.as_view(),name='company'),
    path('company_detail/<pk>',CompanyDetailView.as_view(),name='company_detail'),
    path('bank',BankListView.as_view(),name='bank'),
    path('bank_detail/<pk>',BankDetailView.as_view(),name='bank_detail'),
    path('client',ClientListView.as_view(),name='client'),
    path('client_detail/<pk>',ClientDetailView.as_view(),name='client_detail'),
    path('case_stage',CaseStageListView.as_view(),name='case_stage'),
    path('case_stage_detail/<pk>',CaseStageDetailView.as_view(),name='stage_detail'),
]