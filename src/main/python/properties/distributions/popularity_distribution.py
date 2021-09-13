"""
Representation of the popularity distributions of a given dataset.
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


class PopularityDistribution:
    """
    Class for computing and storing the popularity distribution of a dataset. It obtains a list containing the number
    of ratings per item (it just stores these number, sorted from larger to smaller).
    """

    def __init__(self, rating_matrix):
        """
        Constructor. Finds the probability distribution of the dataset.
        :param rating_matrix: the rating matrix of the dataset.
        """
        self.rating_matrix = rating_matrix

    def get_user_distribution(self):
        """
        Obtains the popularity distribution for the users (i.e. the number of items each user has rated, sorted by
        descending number of ratings).
        """
        distribution = list(map(
            lambda user_id: self.rating_matrix.get_user_ratings(user_id).__len__(),
            self.rating_matrix.get_users())
        )
        distribution.sort(reverse=True)
        return distribution

    def get_relevant_user_distribution(self):
        """
        Obtains the popularity distribution for the users (i.e. the number of items each user has relevantly rated,
        sorted by descending number of ratings).
        """
        distribution = list(map(
            lambda user_id: self.rating_matrix.get_relevant_user_ratings(user_id).__len__(),
            self.rating_matrix.get_users())
        )
        distribution.sort(reverse=True)
        return distribution

    def get_item_distribution(self):
        """
        Obtains the popularity distribution for the items (i.e. the number of users who have rated each item, sorted by
        descending number of ratings).
        """
        distribution = list(map(
            lambda item_id: self.rating_matrix.get_item_ratings(item_id).__len__(),
            self.rating_matrix.get_items())
        )
        distribution.sort(reverse=True)
        return distribution

    def get_relevant_item_distribution(self):
        """
        Obtains the popularity distribution for the items (i.e. the number of users who have rated each item
        as relevant, sorted by descending number of ratings).
        """
        distribution = list(map(
            lambda item_id: self.rating_matrix.get_relevant_item_ratings(item_id).__len__(),
            self.rating_matrix.get_items())
        )
        distribution.sort(reverse=True)
        return distribution
