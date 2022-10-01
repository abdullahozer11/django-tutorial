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
