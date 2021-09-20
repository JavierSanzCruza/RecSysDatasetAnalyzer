"""
Representation of the ContentWise dataset items.
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

from src.main.python.datasets.contentwise.item_type import ContentWiseItemType


class ContentWiseItem:
    """
    Class for storing the information of the ContentWise dataset items.
    """
    def __init__(self,
                 item_id: int,
                 series_id: int,
                 episode: int,
                 item_type: ContentWiseItemType):
        """
        Initializes the item.
        :param item_id: the identifier of the item.
        :param series_id: the identifier of the series this item belongs to.
        :param episode: the episode number of the item in the given series.
        :param item_type: the type of the item.
        """
        self.item_id = item_id
        self.series_id = series_id
        self.episode = episode
        self.type = item_type

    def get_item_id(self) -> int:
        """
        Obtains the item identifier.
        :return: the item identifier.
        """
        return self.item_id

    def get_series_id(self) -> int:
        """
        Obtains the series identifier.
        :return: the series identifier.
        """
        return self.series_id

    def get_episode(self) -> int:
        """
        Obtains the episode number of the series this item appears in.
        :return: the episode number of the series this item appears in.
        """
        return self.episode

    def get_item_type(self) -> ContentWiseItemType:
        """
        Returns the type of the item.
        :return: the type of the item
        """
        return self.type
