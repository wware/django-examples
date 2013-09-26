from django.shortcuts import render_to_response
from django.http import HttpResponse
from html5offline.models import Pair

from django.template import RequestContext, loader


def index(request):
    template = loader.get_template('html5offline/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


def appcache(request):
    return render_to_response('html5offline/appcache', {}, mimetype='text/cache-manifest')


def pairs(request):
    return HttpResponse(Pair.get_json_all(), mimetype='application/json')
