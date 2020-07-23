from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('single/<int:id>/', single, name='single'),
    path('sobre/', single, name='sobre'),
    path('contato/', single, name='contato')
]
