from django.urls import path
from django.conf.urls import url 
from . import views
from simplemooc.courses.views import details

app_name = 'courses'

urlpatterns =[ 
    path('', views.index, name='index'),
   # url(r'^(?P<pk>\d+)/$', details, name='details'), (obs: passa o parametro pk de um ou + digitos para consulta)
	url(r'^(?P<slug>[\w_-]+)/$', details, name='details'), #w alfa numerico, underline ou ifen esses caracteres q o slug permite
]