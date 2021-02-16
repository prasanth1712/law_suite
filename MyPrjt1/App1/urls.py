from django.urls import path
from App1.views.company_views import CompanyListView,CompanyDetailView
from App1.views.bank_views import BankListView
from App1.views.client_views import ClientListView
from App1.views.case_stage_views import CaseStageListView

app_name = 'App1'

urlpatterns = [
    path('company',CompanyListView.as_view(),name='company'),
    path('company_detail/<pk>',CompanyDetailView.as_view(),name='company_detail'),
    path('bank',BankListView.as_view(),name='bank'),
    path('client',ClientListView.as_view(),name='client'),
    path('case_stage',CaseStageListView.as_view(),name='case_stage'),
]