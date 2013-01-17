"""Main urls.py of the pyconsg project."""
from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'pyconsg.views.home', name='home'),
    # url(r'^pyconsg/', include('pyconsg.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(settings.ADMIN_URL, include(admin.site.urls)),
    url(r'^admin/', include('admin_honeypot.urls')),
)
