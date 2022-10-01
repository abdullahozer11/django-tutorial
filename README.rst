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
  url '<namespace_name><path_name>' <argument>
