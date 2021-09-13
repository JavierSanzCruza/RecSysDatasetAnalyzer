"""
Representation of the temporal distributions of a given dataset.
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

import math


class TemporalDistribution:
    """
    Class for computing and storing the temporal distribution of a dataset. It obtains a list containing the number
    of ratings per item (it just stores these number, sorted from larger to smaller).
    """

    def __init__(self):
        """
        Constructor. Initializes the temporal distribution.
        """
        self.distribution = list()
        self.min_timestamp = math.inf
        self.max_timestamp = -1
        self.is_sorted = False

    def add_timepoint(self, user_id, item_id, timestamp):
        """
        Adds an individual time point to the series.
        :param user_id: the user.
        :param item_id: the item.
        :param timestamp: the moment of time when the rating is added.
        """
        self.distribution.append((user_id, item_id, timestamp))
        self.is_sorted = False

        if timestamp < self.min_timestamp:
            self.min_timestamp = timestamp
        if timestamp > self.max_timestamp:
            self.max_timestamp = timestamp

    def get_user_distribution(self):
        """
        Obtains the temporal distribution for the users (a list of (user_id, timestamp) pairs, sorted by ascending
        timestamp.
        """

        if not self.is_sorted:
            self.distribution.sort(key=lambda x: x[2])
            self.is_sorted = True
        return [(x[0], x[2]) for x in self.distribution]

    def get_item_distribution(self):
        """
        Obtains the temporal distribution for the items (a list of (item_id, timestamp) pairs, sorted by ascending
        timestamp.
        """

        if not self.is_sorted:
            self.distribution.sort(key=lambda x: x[2])
            self.is_sorted = True
        return [(x[1], x[2]) for x in self.distribution]
