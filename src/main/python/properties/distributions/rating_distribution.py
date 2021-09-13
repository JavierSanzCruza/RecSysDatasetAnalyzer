"""
Representation of the rating distributions of a given dataset.
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


class RatingDistribution:
    """
    Class for determining how many ratings have been issued for each different value.
    """

    def __init__(self, rating_matrix):
        """
        Constructor. Finds the probability distribution of the dataset.
        :param rating_matrix: the rating matrix of the dataset.
        """
        self.rating_matrix = rating_matrix

    def get_distribution(self):
        """
        Obtains the popularity distribution for the users (i.e. the number of items each user has rated, sorted by
        descending number of ratings).
        """

        values = dict()

        for user in self.rating_matrix.get_users():
            for item, rating in self.rating_matrix.get_user_ratings(user):
                if values.__contains__(rating):
                    values[rating] += 1
                else:
                    values[rating] = 1

        return values
