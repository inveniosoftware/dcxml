# -*- coding: utf-8 -*-
#
# This file is part of dcxml.
# Copyright (C) 2016 CERN.
#
# dcxml is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# dcxml is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with dcxml; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Generation of Simple Dublin Core XML v1.1.

By default the package will wrap elements in an OAI DC element. This behavior
can be changed by specifying ``container``, ``nsmap`` and ``attribs`` to the
API functions.
"""

# import pkg_resources
from lxml import etree

#  from .jsonutils import validator_factory
from .xmlutils import Rules, dump_etree_helper, etree_to_string

rules = Rules()

ns = {
    'dc': 'http://purl.org/dc/elements/1.1/',
    'oai_dc': 'http://www.openarchives.org/OAI/2.0/oai_dc/',
    'xml': 'xml',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
}
"""Default namespace mapping."""

container_attribs = {
    '{http://www.w3.org/2001/XMLSchema-instance}schemaLocation':
    'http://www.openarchives.org/OAI/2.0/oai_dc/ '
    'http://www.openarchives.org/OAI/2.0/oai_dc.xsd',
}
"""Default container element attributes."""

container_element = '{http://www.openarchives.org/OAI/2.0/oai_dc/}dc'
"""Default container element."""


def dump_etree(data, container=None, nsmap=None, attribs=None):
    """Convert dictionary to Simple Dublin Core XML as ElementTree.

    :param data: Dictionary.
    :param container: Name (include namespace) of container element.
    :param nsmap: Namespace mapping for lxml.
    :param attribs: Default attributes for container element.
    :returns: LXML ElementTree.
    """
    container = container or container_element
    nsmap = nsmap or ns
    attribs = attribs or container_attribs
    return dump_etree_helper(container, data, rules, nsmap, attribs)


def tostring(data, **kwargs):
    """Convert dictionary to Simple Dublin Core XML as string.

    :param data: Dictionary.
    :param container: Name (include namespace) of container element.
    :param nsmap: Namespace mapping for lxml.
    :param attribs: Default attributes for container element.
    :returns: LXML ElementTree.
    """
    return etree_to_string(dump_etree(data), **kwargs)


def rule_factory(plural, singular):
    """Element rule factory."""
    @rules.rule(plural)
    def f(path, values):
        for v in values:
            if v:
                elem = etree.Element(
                    '{{http://purl.org/dc/elements/1.1/}}{0}'.format(singular))
                elem.text = v
                yield elem
    f.__name__ = plural
    return f


contributors = rule_factory('contributors', 'contributor')

coverage = rule_factory('coverage', 'coverage')

creators = rule_factory('creators', 'creator')

dates = rule_factory('dates', 'date')

descriptions = rule_factory('descriptions', 'description')

formats = rule_factory('formats', 'format')

identifiers = rule_factory('identifiers', 'identifier')

languages = rule_factory('languages', 'language')

publishers = rule_factory('publishers', 'publisher')

relations = rule_factory('relations', 'relation')

rights = rule_factory('rights', 'rights')

sources = rule_factory('sources', 'source')

subject = rule_factory('subjects', 'subject')

titles = rule_factory('titles', 'title')

types = rule_factory('types', 'type')
