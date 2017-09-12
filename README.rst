===============
MediaMixProject
===============

Installing the API
==================

The api is provided as a python package. You may install it with ``pip`` or any
python package managing tool. We do not provide a python2 version yet.

To install the api in developper mode, use the following commands:

.. code:: raw
   $ git clone https://github.com/Squatt/MediaMixProject
   $ cd MediaMixProject
   $ pip3 install -e .

If you don't want to install the package system-wide, we recommend to use
``virtualenv``. Type these commands before ``pip install`` to use
``virtualenv``:

..code:: raw
	 ``$ virtualenv venv -p /usr/bin/python3
	 $ source venv/bin/activate``


Starting the API
================

Once the package is installed, an executable is provided to start the api:

``$ apimedia-server``
