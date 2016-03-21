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

"""Module tests."""

from __future__ import absolute_import, print_function

from dcxml import simpledc


def test_elements():
    """Test simple dc."""
    elements = [
        ('contributors', 'contributor'),
        ('coverage', 'coverage'),
        ('creators', 'creator'),
        ('dates', 'date'),
        ('descriptions', 'description'),
        ('formats', 'format'),
        ('identifiers', 'identifier'),
        ('languages', 'language'),
        ('publishers', 'publisher'),
        ('relations', 'relation'),
        ('rights', 'rights'),
        ('sources', 'source'),
        ('subjects', 'subject'),
        ('titles', 'title'),
        ('types', 'type'),
    ]

    # Test each element individually
    for plural, singular in elements:
        # Test multiple values
        tree = simpledc.dump_etree({plural: ['value 1', 'value 2']})
        elems = tree.xpath(
            '/oai_dc:dc/dc:{0}'.format(singular), namespaces=simpledc.ns)
        assert len(elems) == 2, singular
        assert elems[0].text == 'value 1'
        assert elems[1].text == 'value 2'

        # Test empty values
        tree = simpledc.dump_etree({plural: []})
        elem = tree.xpath(
            '//dc:{0}'.format(singular), namespaces=simpledc.ns)
        assert len(elem) == 0, singular

    # Test all elements together
    data = {}
    for plural, singular in elements:
        data[plural] = ['test 1', 'test 2']

    tree = simpledc.dump_etree(data)
    for plural, singular in elements:
        elems = tree.xpath(
            '/oai_dc:dc/dc:{0}'.format(singular), namespaces=simpledc.ns)
        assert len(elems) == 2, singular
        assert elems[0].text == 'test 1'
        assert elems[1].text == 'test 2'

    # Test tostring
    xml = simpledc.tostring(data)
    for plural, singular in elements:
        assert '<dc:{0}>'.format(singular) in xml
