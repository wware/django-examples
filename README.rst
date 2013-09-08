Django examples
===============

Since my profession now seems to be "Django guy", I might as well
maintain a little collection of Django examples, branching off from
the `standard tutorial`_.

Heroku
------

I'm going to run this stuff on Heroku just for convenience. It works and it's free.
I'd need to do some research if I were trying to deploy something seriously.

Django uses PostgreSQL. When I'm just messing around on the Macbook, I use SQLite.

The deployment command ``git push heroku master`` did not create or sync my PostgreSQL
database. But I found there is a Python shell command that can do the job::

    $ heroku run python manage.py syncdb

Trouble with the tutorial
-------------------------

One thing in the standard tutorial that didn't work for me is the
section on `Removing hardcoded URLs in templates`_ in the third part
of the tutorial. I got the following error when I tried it, and have done
only a little digging to try to understand what's happening::

 Reverse for ''detail'' with arguments '(1,)' and keyword arguments '{}' not found.

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
``polls`` hasn't been imported when we need it for the ``reverse`` call. It looks like,
if it did actually work, I would need this instead of what's shown in the tutorial::

    <li><a href="{% url 'views.detail' poll.id %}">{{ poll.question }}</a></li>

Since this removal of hardcoded URLs appears to be a matter of taste, useful for
very large websites but unnecessary for small ones, I will defer further investigation
to another time.

Other stuff I'd like to do
--------------------------

There is a bunch of Django stuff for optimizing SQL queries involving
``select_related``, ``prefetch_related``, ``only``, and ``exclude``,
and those would be good to learn more about.

.. _`standard tutorial`: https://docs.djangoproject.com/en/1.5/intro/tutorial01/
.. _`Removing hardcoded URLs in templates`:https://docs.djangoproject.com/en/1.5/intro/tutorial03/#removing-hardcoded-urls-in-templates
