from django.urls import path
from . import views

app_name = 'App1'

urlpatterns = [
    path('',views.appindex,name='main'),
    path('bank',views.BankView.as_view(),name='bank')
]