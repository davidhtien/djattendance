from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    
    #utilities view
    url(r'^$', 'utilities.views.home', name='home'),
    url(r'^all$', 'utilities.views.all_data', name='all'),
)

