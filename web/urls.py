
from django.conf.urls import patterns, url
from web.views import InicioView

urlpatterns = patterns ('',
    url(r'^$', InicioView.as_view(), name='inicio'),
                          )
