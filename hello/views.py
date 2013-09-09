import os

from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    template = loader.get_template('hello/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


# This hack below works fine on my Macbook but fails dismally on Heroku and would probably
# fail in a lot of production environments. You really need a consistent story about how to
# handle static files. Read https://devcenter.heroku.com/articles/django-assets.

def readme(request):
    if not os.popen("find hello/templates/hello -name 'README.html' -newer README.rst").read().strip():
        rst2html = os.popen('find * -name rst2html.py').read().strip()
        os.system(rst2html + ' README.rst hello/templates/hello/README.html')
    template = loader.get_template('hello/README.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))
