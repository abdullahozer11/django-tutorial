Django tutorial
###############

`Tutorial link <https://docs.djangoproject.com/en/4.1/>`_

Setup steps
-----------

1. Create a virtual environment .venv at the root of the repo:

.. code-block:: bash

    python3 -m .venv .

2. Activate the environment:

.. code-block:: bash

    . ./.venv/bin/activate

3. Install modules in the virtual environment:

.. code-block:: bash

    pip install -r requirements.txt

Part 1
------

Key commands:

- To create a project:

.. code-block:: bash

    django-admin startproject <project_name>

- To run the server:

.. code-block:: bash

    python manage.py runserver

- To create an app:

.. code-block:: bash

    python manage.py startapp <app_name>

Key learnings:

- A project can contain several apps.
- An app can be used in different projects.

Part 2
------

Key commands:

- To apply/unapply migrations:

.. code-block:: bash

    python manage.py migrate

- To create tables after a change of models:

.. code-block:: bash

    python manage.py makemigrations

- To see commands run by a migration:

.. code-block:: bash

    python manage.py sqlmigrate <app_name> <migration_id>

- Open the shell with to use Django API:

.. code-block:: bash

    python manage.py shell

- Create a super-user for the admin app

.. code-block:: bash

    python manage.py createsuperuser

Key learnings:

- Django default database is sqlite.
- There are existing common apps in django.contrib: admin, auth...
- Model classes must inherit from `django.db.models.Model`.
- Used apps are referred in the INSTALLED_APPS list in <project_name>/settings.py.
- <model_class_name>.<field>.<method>(<args>) is the general API syntax.
- One can interact with the models vis the Django Admin app.

Part 3
------

Key learnings:

- Views are methods that take a request as argument, and other parameters and
  return an HttpResponse object.
- URLs use patterns to general URL paths and to pass arguments views they are
  mapped to.
- Useful shortcuts in views are: `django.shortcuts.render` and
  `django.shortcuts.get_object_or_404`.
- Templates are called in view and passed arguments in a context.
- To avoid hardcoded URLs in templates, use the:  url '<path_name>' <argument>
- To avoid collisions of URLs, use the namespace syntax:
  url '<namespace_name><path_name>' <argument>.

Part 4
------

Key learnings:

- All POST forms that are targeted at internal URLs should use the
  `{% csrf_token %}` template tag to prevent from cross site request forgeries.
- request.POST is a dictionary-like object that lets you access submitted data.
  of a form by key name. (request.GET also exists).
-  `django.http.HttpResponseRedirect` can be the object returned by a view to
  redirect to a specific URL.
- The `django.urls.reverse` allows to not have to pass hardcoded URLs.
- If two POST requests are executed simultaneously on two different threads,
  using F(), can avoid race conditions:
  `See more <https://docs.djangoproject.com/en/4.1/ref/models/expressions/#avoiding-race-conditions-using-f>`_
- Generic views/class abstract common patterns of views to write less code.
- Generic views are built-in class-based views.
- They match the `pk` (primary key) argument of a model.
- They come from `django.views.generic`.
- `ListView`
    - abstracts the concept of "display a lit of objects".
    - uses a template called <app_name>/<model_name>_list.html.
    - has the automatically generated context variable <model_name>_list.
    - `context_object_name` variable can override <model_name>_list.
- `DetailView`
    - abstracts the concept of "display a detail page for a particular type of
      object".
    - uses a template called <app_name>/<model_name>_detail.html.

Part 5
------

Key commands:

- Run tests for an application:

.. code-block:: bash

    python manage.py test <app_name>

Key learnings:

- When running the tests, Django creates a specific database for the purpose of
  testing.
- Django test client can be set up using
  `django.test.utils.setup_test_environment` in the shell.
- It doesn't set up a test database, it is tested against existing data.
- We can use: `django.test.Client` to create a client instance and interact
  with the views.
- Inheriting from `django.test.TestCase` for creating our test class allows to
  get a `django.test.Client` on the fly.
- `assertContains` and `assertQuerySetEquals` are two examples of methods
  inherited from `django.test.TestCase` to perform assertions.
- At each method of the a test class, the database is reset.
- It is good practice to have
    - a separate TestClass for each model or view.
    - a separate test for each set of conditions you want to test.
- Django includes `django.test.LiveServerTestCase` to facilitate integration of
  UI testing with Django.

Part 6
------

- `django.contrib.staticfiles` is an application that helps collection static
  files from each of our applications into a single location that can easily be
  served in production.
- Inside an app, we create a folder called `static` in which Django will search
  for static files.
- Similarly to templates that we create under `<app_name>/templates/<app_name>`,
  we create static files under `<app_name>/static/<app_name>`.
- In the template, use `{% load static %}` to generate the absolute URL of
  static files.
- Always use the `{% static %}` tag only in files generated by django and use
  relative paths to link static files to each other like so:
  `{% static 'polls/style.css' %}`.
