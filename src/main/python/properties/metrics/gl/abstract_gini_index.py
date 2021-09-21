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

from src.main.python.data.filters import RatingFilter, ItemFilter, UserFilter
from src.main.python.properties.distributions.popularity_distribution import PopularityDistribution
from .global_property import GlobalProperty

import typing


class AbstractGiniIndex(GlobalProperty):
    """
    Abstract implementation of a metric that uses the Gini index for computing how balanced is the distribution of
    ratings over users / items in the dataset.
    """

    def compute(self,
                relevant: bool = False,
                user_filter: typing.Callable[[int], bool] = None,
                item_filter: typing.Callable[[int], bool] = None,
                rating_filter: typing.Callable[[int, int, float], bool] = None
                ) -> float:
        if user_filter is None and item_filter is None and rating_filter is None:
            pop = PopularityDistribution(self.rating_matrix)
            return self.compute_relevant_index(pop) if relevant else self.compute_index(pop)
        else:
            if user_filter is None:
                user_filter = UserFilter.default
            if item_filter is None:
                item_filter = ItemFilter.default
            if rating_filter is None:
                rating_filter = RatingFilter.default

            aux_matrix = self.rating_matrix.filter(user_filter=user_filter, item_filter=item_filter,
                                                   rating_filter=rating_filter)
            pop = PopularityDistribution(aux_matrix)
            return self.compute_index(pop, relevant)

    @abstractmethod
    def compute_index(self,
                      pop: PopularityDistribution,
                      relevant: bool = False) -> float:
        """
        Given a popularity distribution, it computes the Gini index.
        :param pop: the popularity distribution.
        :param relevant: (OPTIONAL) True if we limit ourselves to the relevant distribution, False otherwise.
        :return: the value of the Gini index for the distribution.
        """
        pass
