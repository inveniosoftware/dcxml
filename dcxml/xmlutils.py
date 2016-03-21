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

"""XML utilities."""

from __future__ import absolute_import, print_function

from collections import OrderedDict

from lxml import etree


def dump_etree_helper(container_name, data, rules, nsmap, attrib):
    """Convert DataCite JSON format to DataCite XML.

    JSON should be validated before it is given to to_xml.
    """
    output = etree.Element(container_name, nsmap=nsmap, attrib=attrib)

    for rule in rules:
        if rule not in data:
            continue

        element = rules[rule](rule, data[rule])
        for e in element:
            output.append(e)

    return output


def etree_to_string(root, pretty_print=True, xml_declaration=True,
                    encoding='utf-8'):
    """Dump XML etree as a string."""
    return etree.tostring(
        root,
        pretty_print=pretty_print,
        xml_declaration=xml_declaration,
        encoding=encoding,
    ).decode('utf-8')


class Rules(object):
    """Rules container."""

    def __init__(self):
        """Initialize rules object."""
        self.rules = OrderedDict()

    def __getitem__(self, key):
        """Get rule for key."""
        return self.rules[key]

    def __iter__(self):
        """Get iterator for rules."""
        return iter(self.rules)

    def rule(self, key):
        """Decorate as a rule for a key in top level JSON."""
        def register(f):
            self.rules[key] = f
            return f
        return register
