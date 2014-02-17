from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import udi123

urlpatterns = patterns('udi123',


    #url(r'^$', 'udi123.foo', name='home'),

    url(r'^$', udi123.printer),

    url(r'^(\d+)/$', 'printer'),
    url(r'^(\d+)/([a-z])/$', 'printer'),
    url(r'^(?P<c>[a-z])/$', 'printer'),

    url(r'^xyzzy/$', 'printer', {'n': 50, 'c':'!'}),



    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
