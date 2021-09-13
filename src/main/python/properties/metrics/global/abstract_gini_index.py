"""
Implementation of the Gini index of a list of values.
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

from abc import abstractmethod

from src.main.python.data import RatingMatrix
from src.main.python.properties.distributions.popularity_distribution import PopularityDistribution
from .global_property import GlobalProperty


class AbstractGiniIndex(GlobalProperty):
    """
    Abstract implementation of a metric that uses the Gini index for computing how balanced is the distribution of
    ratings over users / items in the dataset.
    """

    def compute(self, rating_matrix):
        pop = PopularityDistribution(rating_matrix)
        return self.compute_index(pop)

    def compute_relevant(self, rating_matrix):
        pop = PopularityDistribution(rating_matrix)
        return self.compute_relevant_index(pop)

    def compute_filter(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                       rating_filter=lambda x: x):
        # First, we find the auxiliary matrix.
        aux_matrix = RatingMatrix()
        for item in filter(item_filter, rating_matrix.get_items()):
            aux_matrix.add_item(item)

        for user in filter(user_filter, rating_matrix.get_users()):
            aux_matrix.add_user(user)
            f = filter(lambda x: item_filter(x[0]) and rating_filter((user, x[0], x[1])),
                       rating_matrix.get_user_ratings(user))
            for x in f:
                aux_matrix.rate(user, x[0], x[1])

        return self.compute(aux_matrix)

    @abstractmethod
    def compute_index(self, pop):
        """
        Given a popularity distribution, it computes the Gini index.
        """
        pass

    @abstractmethod
    def compute_relevant_index(self, pop):
        """
        Given a popularity distribution, it computes the Gini index, related to the relevant ratings.
        """
        pass
