"""
Return value for rating matrices and impressions.
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

from enum import Enum


class AddingReturn(Enum):
    """
    Definition of values for checking the addition / removal of values in rating matrix.
    """

    # ERROR value: when the value could not be added / removed / updated.
    ERROR = -1
    # NONE value: no modification has been done.
    NONE = 0
    # ADDED value: the value was straightforwardly added (it did not previously exist).
    ADDED = 1
    # UPDATED value: the value was updated from a previous state.
    UPDATED = 2
