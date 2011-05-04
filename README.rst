integer_encoding
================
A simple python module that encodes integers into arbitrary-base element
sequences.

Usage
~~~~~
**Encoding**::

  >>> import integer_encoding
  >>> alphabet = 'abc123'
  >>> encode = integer_encoding.encoder(alphabet)
  >>> encode(0)
  ['a']
  >>> encode(1)
  ['b']
  >>> encode(2)
  ['c']
  >>> encode(6)
  ['b', 'a']
  >>> encode(1306)
  ['b', 'a', 'a', 'b', '2']
  >>> encode(1307)
  ['b', 'a', 'a', 'b', '3']

**Decoding**::

  >>> import integer_encoding
  >>> decode = integer_encoding.decoder('abc123')
  >>> decode('a')
  0
  >>> decode('b')
  1
  >>> decode('c')
  2
  >>> decode('ba')
  6
  >>> decode('baab2')
  1306
  >>> decode('baab3')
  1307

Installing
~~~~~~~~~~
Install from PyPI::

  $ pip install integer_encoding

or you grab the source and run::

  $ python setup.py install

Tests
~~~~~
To run the tests, first install tox_::

  $ pip install tox

then run `tox` from the project root directory::

  $ tox

.. _tox: http://pypi.python.org/pypi/tox
