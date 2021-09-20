"""
Implementation of a class that optionally has a value (none otherwise)
"""

__version__ = '0.1'
__author__ = 'Javier Sanz-Cruzado, Pablo Castells'
__email__ = 'javier.sanz-cruzado@uam.es, pablo.castells@uam.es'
__copyright__ = """
 Copyright (C) 2021 Information Retrieval Group at Universidad Autónoma
 de Madrid, http://ir.ii.uam.es.

 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this
 file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
__license__ = 'Mozilla Public License v. 2.0'


class Optional:
    """
    Class for optional objects.
    """

    def __init__(self):
        """
        Initializes the object as None (empty).
        """
        self.object = None

    @staticmethod
    def empty():
        """
        Builds an empty object.
        :returns: the empty optional value.
        """
        opt = Optional()
        opt.object = None
        return opt

    @staticmethod
    def of(obj):
        """
        Builds an optional object with a given value.
        :param obj: the value to store.
        :return: the optional object, initialized with the given value.
        """
        opt = Optional()
        opt.object = obj
        return opt

    def is_empty(self):
        """
        Checks whether the object is empty or not.
        :returns: True if the object is empty, False otherwise.
        """
        return self.object is None

    def get(self):
        """
        Returns the value of the object.
        :returns: the value of the object.
        """
        return self.object
