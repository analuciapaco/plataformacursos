from django.urls import path, include
from django.conf.urls import url 
from simplemooc.core.views import home
from simplemooc.core import views
app_name = 'core'

urlpatterns =[ 
    url(r'^$',views.home, name='home'),
    path('contato/', views.contact, name='contact'),
]