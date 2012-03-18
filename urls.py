from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'liftium.views.home', name='home'),
    # url(r'^liftium/', include('liftium.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'dashboard/', include(admin.site.urls)), # for the dev server
    url(r'^$', include(admin.site.urls)), # for apache
)
