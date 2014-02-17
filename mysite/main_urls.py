from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',


    #url(r'^$', 'udi123.foo', name='home'),

    #url(r'^$', udi123.printer),
    #url(r'^udi/$', 'blog.views.udi'),
    #
    #url(r'tttrrr^$', udi123.printer),
    #
    #url(r'^(\d+)/$', 'udi123.printer'),
    #url(r'^(?P<c>[a-z])/$', 'udi123.printer'),
    #
    #url(r'^xyzzy/$', 'udi123.printer', {'n': 50, 'c':'!'}),
    #url(r'^ab/$', 'udi123.printer', {'n': 30, 'c':'?'}),
    #url(r'^zzz234/$', 'udi123.printer', {'n': 20, 'c':'&'}),
    #url(r'^zzzcdcd234/$', 'udi123.printer', {'n': 20, 'c':'&'}),
    #url(r'^zzz2cdcddcdcd34/$', 'udi123.printer', {'n': 20, 'c':'&'}),



    url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
