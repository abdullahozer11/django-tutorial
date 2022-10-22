=====
Polls
=====

Polls is a Django app to conduct web-based polls. For each question, visitors
can choose between a fixed number of answers.

Detailed documentation is in the `docs` directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS settings like this:

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'polls',
    ]

2. Include the polls URLconf in your project `url.py` file like this:

.. code-block:: python

    urlpatterns = [
        ...
        path('polls/', include('polls.urls')),
    ]

3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit: `<http://127.0.0.1:8000/admin/>`_ to
  create a poll (you'll need the Admin app enabled).

5. Visit `<http://127.0.0.1:8000/polls/>`_ to participate in the poll.
