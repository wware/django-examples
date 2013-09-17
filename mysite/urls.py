from django.conf.urls import patterns, include, url
import hello.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', hello.views.index, name='index'),
    url(r'^README.html$', hello.views.readme, name='index'),
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^responsive/', include('responsive.urls', namespace='responsive')),
    url(r'^pqueue/', include('pqueue.urls', namespace='pqueue')),
    url(r'^admin/', include(admin.site.urls)),
)
