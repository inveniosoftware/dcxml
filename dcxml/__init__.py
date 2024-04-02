# -*- coding: utf-8 -*-
#
# This file is part of dcxml.
# Copyright (C) 2016-2018 CERN.
#
# dcxml is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Dublin Core XML generation from Python dictionaries.

The Dublin Core Python package allows you to generate XML (either as string or
ElementTree) for the 15 elements in Simplified Dublin Core. By default the
package wraps the 15 elements in an OAI DC element (customizable).

See http://dublincore.org/documents/dces/ for the description of all 15
elements.

First let's create a Python dictionary with all 15 elements:

>>> data = dict(
...     contributors = ['CERN'],
...     coverage = ['Geneva'],
...     creators = ['CERN'],
...     dates = ['2002'],
...     descriptions = ['Simple Dublin Core generation'],
...     formats = ['application/xml'],
...     identifiers = ['dublin-core'],
...     languages = ['en'],
...     publishers = ['CERN'],
...     relations = ['Invenio Software'],
...     rights = ['MIT'],
...     sources = ['Python'],
...     subjects = ['XML'],
...     titles = ['Dublin Core XML'],
...     types = ['Software'],
... )

The structure of the dictionary is:

* Keys: Normally the plural version of the DC element name except for (
  ``rights`` and ``coverage``).
* Values: List of strings. Each item in the list will result in one DC element.

Now, let's generate the Dublin Core XML:

>>> from dcxml import simpledc
>>> xml = simpledc.tostring(data)

and print the 15 elements (without the container element)

>>> for l in xml.splitlines()[2:-1]:
...     print(l)
  <dc:contributor>CERN</dc:contributor>
  <dc:coverage>Geneva</dc:coverage>
  <dc:creator>CERN</dc:creator>
  <dc:date>2002</dc:date>
  <dc:description>Simple Dublin Core generation</dc:description>
  <dc:format>application/xml</dc:format>
  <dc:identifier>dublin-core</dc:identifier>
  <dc:language>en</dc:language>
  <dc:publisher>CERN</dc:publisher>
  <dc:relation>Invenio Software</dc:relation>
  <dc:rights>MIT</dc:rights>
  <dc:source>Python</dc:source>
  <dc:title>Dublin Core XML</dc:title>
  <dc:type>Software</dc:type>

The container element is by default the ``<oai_dc:dc>`` element:

>>> print(xml.splitlines()[1])
<oai_dc:dc ...

In case you need an ElementTree instead of a string, it's as simple as:

>>> tree = simpledc.dump_etree(data)

"""

from __future__ import absolute_import, print_function

from .version import __version__

__all__ = ('__version__', )
