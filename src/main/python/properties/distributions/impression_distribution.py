"""
Representation of the distribution of impressions in a dataset.
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


class ImpressionsDistribution:
    """
    Class for computing and storing the distribution of impressions of a dataset.
    """

    def __init__(self, impressions):
        """
        Constructor. Finds the probability distribution of the dataset.
        :param impressions: the set of impressions of the dataset.
        """
        self.impressions = impressions

    def get_user_distribution(self):
        """
        Obtains the impression distribution for the users (i.e. the number of items each user has been shown, sorted by
        descending number of times they have been recommended to them).
        """
        distribution = list(map(
            lambda user_id: self.impressions.get_num_user_impressions(user_id),
            self.impressions.get_users())
        )
        distribution.sort(reverse=True)
        return distribution

    def get_item_distribution(self):
        """
        Obtains the impression distribution for the items (i.e. the number of times each item has been shown, sorted by
        descending number of times they have been recommended).
        """
        distribution = list(map(
            lambda item_id: self.impressions.get_num_item_impressions(item_id),
            self.impressions.get_items())
        )
        distribution.sort(reverse=True)
        return distribution
