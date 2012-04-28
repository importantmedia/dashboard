from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import redirect_to
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^dashboard/tag_generator', 'frontend.views.tag_generator'),
    url(r'^dashboard/', include(admin.site.urls)), 
    url(r'^$',  redirect_to, {'url': '/dashboard/'})
)
