from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('single/<int:id>/', single, name='single'),
    path('save_form/', save_form, name='save_form'),
    path('contato/', contato, name='contato')
]
