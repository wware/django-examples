Django examples
===============

Since my profession now seems to be "Django guy", I might as well
maintain a little collection of Django examples, branching off from
the `standard tutorial`_.

.. _`standard tutorial`: https://docs.djangoproject.com/en/1.5/intro/tutorial01/

Heroku
------

I'm going to run this stuff on Heroku just for convenience. It works and it's free.
I'd need to do some research if I were trying to deploy something seriously.

Django uses PostgreSQL. When I'm just messing around on the Macbook, I use SQLite.

The deployment command ``git push heroku master`` did not create or sync my PostgreSQL
database. But I found there is a Python shell command that can do the job::

    $ heroku run python manage.py syncdb

Some info about Python, Django, Gunicorn, and Heroku all playing together...

* https://devcenter.heroku.com/articles/getting-started-with-python
* https://devcenter.heroku.com/articles/getting-started-with-django
* https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/gunicorn/#running-django-in-gunicorn-as-a-generic-wsgi-application
* http://docs.gunicorn.org/en/latest/run.html
* http://michal.karzynski.pl/blog/2013/06/09/django-nginx-gunicorn-virtualenv-supervisor/

Trouble with the tutorial
-------------------------

One thing in the standard tutorial that didn't work for me is the
section on `Removing hardcoded URLs in templates`_ in the third part
of the tutorial. I got the following error when I tried it, and have done
only a little digging to try to understand what's happening::

 Reverse for ''detail'' with arguments '(1,)' and keyword arguments '{}' not found.

.. _`Removing hardcoded URLs in templates`: https://docs.djangoproject.com/en/1.5/intro/tutorial03/#removing-hardcoded-urls-in-templates

So I did a little digging, and in ``venv/lib/python2.7/site-packages/django/template/defaulttags.py``
I found ``URLNode.render`` which has this::

    try:
        url = reverse(project_name + '.' + view_name,
                  args=args, kwargs=kwargs,
                  current_app=context.current_app)
    except NoReverseMatch:
        if self.asvar is None:
            # Re-raise the original exception, not the one with
            # the path relative to the project. This makes a
            # better error message.
            raise e

And ``project_name`` says "mysite" instead of "polls". If I try to force the matter
by saying this in ``mysite.settings``::

    SETTINGS_MODULE = polls.settings

things don't go too much better. Yes, I get ``project_name`` saying "polls", but then
``polls`` hasn't been imported when we need it for the ``reverse`` call. Since this
removal of hardcoded URLs appears to be a matter of taste, useful for
very large websites but unnecessary for small ones, I will defer further investigation
to another time.

Other stuff I'd like to do
==========================

Priority queue
--------------

A to-do list should really be a `priority queue`_. If it's maintained online, accessible
to phone or tablet or Macbook, that's a handy thing. Python has a  `heap queue`_ module
designed for priority queues. I don't think that will be necessary for this purpose since
my to-do list might never have more than 100 items, and I might redefine priorities from
time to time. I might have a few different characteristics, which make it possible to sort
in a number of different ways.

In any event one of the apps should be a priority queue, however it is implemented.

.. _`priority queue`: http://en.wikipedia.org/wiki/Priority_queue
.. _`heap queue`: http://docs.python.org/2/library/heapq.html

Responsive web design
---------------------

I want to learn this stuff so I can make websites that work well on phones, tablets, and
laptops.

APIs of the Rich and Famous
---------------------------

* https://developers.google.com/drive/examples/python DrEdit, an example usage of the Google Drive API
* https://developers.google.com/events/io/sessions/351310959 The Freebase APIs: Tapping into Google's Knowledge Graph
* https://developers.google.com/maps/ Google Maps API

Database cleverness
-------------------

There is a bunch of Django stuff for optimizing SQL queries involving ``select_related``,
``prefetch_related``, ``only``, and ``exclude``, and those would be good to learn more
about. So database stuff, joins, prefetching, etc., all the `QuerySet API`_ stuff in Django.

.. _`QuerySet API`: https://docs.djangoproject.com/en/1.5/ref/models/querysets/

PayPal and e-commerce
---------------------

PayPal maintains a `sandbox`_ for debugging your application, and I should use the
`REST APIs`_ to work with the sandbox.

.. _`sandbox`: https://cms.paypal.com/us/cgi-bin/?cmd=_render-content&content_ID=developer/e_howto_testing_SBOverview
.. _`REST APIs`: https://developer.paypal.com/webapps/developer/docs/api/

There are some pre-existing e-commerce solutions for Django, such as `Satchmo`_ and `LFS`_
which are both open-source. There is also `Beginning Django E-Commerce`_, a book on Amazon
with 4.5 stars and an affordable Kindle edition.

.. _`Beginning Django E-Commerce`: http://www.amazon.com/Beginning-Django-E-Commerce-Experts-Development/dp/1430225351/
.. _`Satchmo`: http://www.satchmoproject.com/
.. _`LFS`: http://www.getlfs.com/

I should build a simple fake webstore with a shopping cart and a PayPal payment system,
using the sandbox. It should be trivially easy to flip a switch to make it a real webstore.
Obviously flipping the switch would include replacing fake products with real products.

Try to think through how you'll handle orders and fulfillment. There is a customer-facing
piece and a merchant-facing piece, and the merchant-facing piece should help the merchant
in getting stuff to customers in a timely fashion, and keeping track of any inventory.

