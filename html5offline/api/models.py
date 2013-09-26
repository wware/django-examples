from tastypie.resources import ModelResource
from html5offline.models import Pair
from tastypie.serializers import Serializer
from tastypie.authorization import Authorization
from tastypie import fields


class PairResource(ModelResource):

    key = fields.CharField(attribute='key')
    value = fields.CharField(attribute='value')

    class Meta:
        queryset = Pair.objects.all()
        allowed_methods = ['get', 'post']
        resource_name = 'pair'
        serializer = Serializer()
        authorization = Authorization()
