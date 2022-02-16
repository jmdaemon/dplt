.. dxp documentation master file, created by
   sphinx-quickstart on Tue Feb 15 13:10:38 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Dxp: A Data eXPloration library
===============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   reference/index


Dxp provides useful functions to read, write, and manipulate 
Pandas DataFrames and Numpy Arrays. Dxp also provides a hookable interface to
easily get started.

Install
=======
To install Dxp to your system run ``pip install dxp``

Usage
=====

Create a ``pop.py`` file in a directory with the following:

.. code-block:: python

   # pop.py
   import dxp.util as du

   def pop(data: dict):
       pass

Then run ``dxp input.csv``. Assuming you have an ``input.csv`` file set up,
dxp will process the file and hand execution off to your ``pop.py`` file for
you to process. From there you make use of dxp's library functions.

Contributing
============
Anyone is free to contribute, just open an issue, or fork
the project and create an upstream PR.

If you need to contact me, you can email me at mailto:diza@unbc.ca

Todo
====

* Create examples for docs
* Add more unit tests & do fuzzing
* Add more useful functionality

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
