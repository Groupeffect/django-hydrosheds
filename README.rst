=====================
django-hydrosheds
=====================

A reusable Django application that provides ready-to-use GeoDjango models,
REST API endpoints, serializers, and admin integration for the
`HydroSHEDS <https://www.hydrosheds.org/products>`_ family of datasets:

- **HydroLAKES** — global lake and reservoir polygons
- **HydroRIVERS** — global river network line segments
- **HydroBASINS** — global watershed / sub-basin boundaries
- **HydroWASTE** — global wastewater treatment plant locations

.. contents:: Table of Contents
   :depth: 2
   :local:


Requirements
============

- Python ≥ 3.12
- Django ≥ 6.0

Runtime dependencies (installed automatically):

- ``django-filter`` ≥ 25
- ``djangorestframework`` ≥ 3.16


Installation
============

Install from PyPI:

.. code-block:: bash

   pip install django-hydrosheds

Or via `uv <https://docs.astral.sh/uv/>`_:

.. code-block:: bash

   uv add django-hydrosheds


Quick Start
===========

1. Add ``hydrosheds`` and its dependencies to ``INSTALLED_APPS``:

.. code-block:: python

   INSTALLED_APPS = [
       # ...
       "django.contrib.gis",
       "django_filters",
       "rest_framework",
       "hydrosheds",
   ]

2. Include the URL configuration in your project's ``urls.py``:

.. code-block:: python

   from django.urls import path, include

   urlpatterns = [
       # ...
       path("api/", include("hydrosheds.urls")),
   ]

3. Run migrations:

.. code-block:: bash

   python manage.py migrate


Models
======

All models live under ``hydrosheds.db`` and are backed by abstract base classes
defined in ``hydrosheds.db.core``. Each field carries descriptive ``help_text``
derived from the official HydroSHEDS technical documentation.

+---------------------+-------------------------------------+-------------------+
| Concrete Model      | Abstract Base (core)                | Geometry          |
+=====================+=====================================+===================+
| ``HydroLake``       | ``HydroLakePoint``                  | ``PointField``    |
+---------------------+-------------------------------------+-------------------+
| ``HydroRiver``      | ``HydroRiverLine``                  | ``LineStringField``|
+---------------------+-------------------------------------+-------------------+
| ``HydroBasin``      | ``HydroBasinPolygon``               | ``MultiPolygon``  |
+---------------------+-------------------------------------+-------------------+
| ``HydroWaste``      | ``HydroWastePoint``                 | ``PointField``    |
+---------------------+-------------------------------------+-------------------+

All geometry fields use **SRID 4326** (WGS 84).


REST API
========

The package ships with ``ModelViewSet`` views registered through a
``DefaultRouter``. Each endpoint supports **filtering**, **search**, and
**ordering** out of the box via ``django-filter``.

+---------------------+----------------------------+
| Endpoint            | ViewSet                    |
+=====================+============================+
| ``/HydroLakePoint`` | ``HydroLakePointViewSet``  |
+---------------------+----------------------------+
| ``/HydroRiverLine`` | ``HydroRiverLineViewSet``  |
+---------------------+----------------------------+
| ``/HydroWastePoint``| ``HydroWastePointViewSet`` |
+---------------------+----------------------------+
| ``/HydroBasinPolygon``| ``HydroBasinViewSet``    |
+---------------------+----------------------------+

Permissions default to ``IsAuthenticatedOrReadOnly``.


Management Command 'geodata'
============

Download shapefiles from https://www.hydrosheds.org/products

Use the bundled management command to import shapefiles:

.. code-block:: bash
   # load data to database table
   python manage.py geodata -f path/to/HydroRIVERS_v10.shp -n HydroRiver --load

   # print model classes and mappings
   python manage.py geodata -f path/to/HydroRIVERS_v10.shp -n HydroRiver 

   # print help
   python manage.py geodata -h

Configuration
=============

The following Django settings are available:

``HYDROSHEDS_DISABLE_MODELS``
   Set to ``True`` to prevent model registration (useful in projects that only
   need the abstract base classes).

``HYDROSHEDS_DISABLE_ADMIN``
   Set to ``True`` to skip automatic admin site registration.


License
=======

GPL-3.0 — see ``LICENSE`` for details.


Links
=====

- Repository: https://github.com/groupeffect/django-hydrosheds
- Changelog: https://github.com/groupeffect/django-hydrosheds/blob/main/CHANGELOG.rst
- HydroSHEDS: https://www.hydrosheds.org/products
