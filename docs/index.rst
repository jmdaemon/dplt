.. dxp documentation master file, created by
   sphinx-quickstart on Tue Feb 15 13:10:38 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Dxp
===

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   reference/index
.. usage
.. install
.. config


Dxp is a data exploration library.
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

   def populate(data: du.Data, output_csv: str, graph_csv: str):
       pass

From there you can start using some of the library functions.

Contributing
============
Anyone is free to contribute, just open an issue, or fork the project and create an upstream PR. If you need to contact me, you can email me at mailto:diza@unbc.ca

Todo
====

* Replace hookable dynmod interface with callable cli
* Create examples for docs
* Add unit testing & fuzzing
* Remove various side effects
* Clarify intent of dxp modules. dxp.cli, dxp.lab have confusing behaviors. 
* Create data object with holds a path. Replaces ``pop(data, output_csv, graph_csv`` with data object that contains the inputs, outputs, and optional graph dataframes and paths required.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
