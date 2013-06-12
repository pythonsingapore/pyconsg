"""Main urls.py of the pyconsg project."""
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.views.generic.simple import direct_to_template

import symposion.views

import pyconsg.views


admin.autodiscover()
WIKI_SLUG = r'(([\w-]{2,})(/[\w-]{2,})*)'

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG is False and settings.SANDBOX is True:
    # This helps if you set `DEBUG = False` locally. This way you don't need
    # to setup a webserver in order to get 404, 500 pages and media files
    # served.
    urlpatterns += patterns('',
        (r'^404/$', 'django.views.defaults.page_not_found'),
        (r'^500/$', 'django.views.defaults.server_error'),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += patterns(
    '',
    url(r'^$',
        direct_to_template, {'template': 'homepage.html', },
        name='home'),
    url(r'^proposals/$',
        direct_to_template, {'template': 'proposals.html', },
        name='proposals'),
    url(r'^sponsorship/$',
        direct_to_template, {'template': 'sponsorship.html', },
        name='sponsorship'),

    url(settings.ADMIN_URL, include(admin.site.urls)),
    url(r'^admin-.+/', include('admin_honeypot.urls')),

    url(r'^account/signup/$',
        symposion.views.SignupView.as_view(),
        name='account_signup'),
    url(r'^account/login/$',
        symposion.views.LoginView.as_view(),
        name='account_login'),
    url(r'^account/logout/$',
        pyconsg.views.PyconSGLogoutView.as_view(),
        name='account_logout'),
    url(r'^account/', include('account.urls')),

    url(r'^checkout/group/', include('paypal_pyconsg.group_checkout_urls')),
    url(r'^checkout/',
        TemplateView.as_view(template_name='checkout_closed.html'),
        name='paypal_checkout'),
    # url(r'^checkout/', include('paypal_express_checkout.urls')),

    url(r'^schedule/', include('symposion.schedule.urls')),
    url(r'^dashboard/checkout-choices/', include('paypal_pyconsg.urls')),
    url(r'^dashboard/', symposion.views.dashboard, name='dashboard'),
    url(r'^speaker/', include('symposion.speakers.urls')),
    url(r'^proposals/', include('symposion.proposals.urls')),
    url(r'^sponsors/', include('symposion.sponsorship.urls')),
    url(r'^boxes/', include('symposion.boxes.urls')),
    url(r'^teams/', include('symposion.teams.urls')),
    url(r'^reviews/', include('symposion.reviews.urls')),
    url(r'^markitup/', include('markitup.urls')),

    url(r'^', include('cms.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
