from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'frontend.views.home', name='home'),
    # url(r'^frontend/', include('frontend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'tag_generator', 'frontend.views.tag_generator'),
    url(r'dashboard/', include(admin.site.urls)), # for the dev server
    url(r'', include(admin.site.urls)), # for apache
)
