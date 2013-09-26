from tastypie.api import Api
from django.conf.urls import include, patterns, url

from html5offline import views
from html5offline.api.models import PairResource

v1_api = Api(api_name='v1')
v1_api.register(PairResource())

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^appcache$', views.appcache),
    (r'^api/', include(v1_api.urls)),
)
