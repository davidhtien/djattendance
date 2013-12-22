from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import autofixture

admin.autodiscover()
autofixture.autodiscover()

urlpatterns = patterns('',
	url(r'^accounts/login/$', login),
	url(r'^accounts/logout/$', logout),
    url(r'^$', 'ap.views.home'),
    url(r'^base_example/$', 'ap.views.base_example'),

    url(r'^terms/', include('terms.urls', namespace="terms")),
    url(r'^dailybread/', include('dailybread.urls', namespace="dailybread")),
    url(r'^import/', include('imports.urls', namespace="imports")),

    # Examples:
    # url(r'^$', 'ap.views.home', name='home'),
    # url(r'^ap/', include('ap.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

