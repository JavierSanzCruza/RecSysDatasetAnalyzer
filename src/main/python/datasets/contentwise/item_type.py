"""
Enumeration for the different types of items in the ContentWise dataset.
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


class ContentWiseItemType(Enum):
    """
    Enumeration for the different types of items in the ContentWise dataset
    """

    MOVIES = 0
    MOVIES_CLIPS = 1
    TV_MOVIES = 2
    TV_SERIES = 3

    @staticmethod
    def from_value(val: int):
        """
        Obtains the type of the item from its value on the original dataset.
        """
        if val == 0:
            return ContentWiseItemType.MOVIES
        elif val == 1:
            return ContentWiseItemType.MOVIES_CLIPS
        elif val == 2:
            return ContentWiseItemType.TV_MOVIES
        elif val == 3:
            return ContentWiseItemType.TV_SERIES
        else:
            return None

