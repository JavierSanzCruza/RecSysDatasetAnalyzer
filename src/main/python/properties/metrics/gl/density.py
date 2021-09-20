"""
Implementation of the density of a rating matrix.
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

from src.main.python.data.filters import UserFilter, RatingFilter, ItemFilter
from .global_property import GlobalProperty
import math
import typing


class Density(GlobalProperty):
    """
    Class for computing the density of a dataset.
    """
    def compute(self,
                relevant: bool = False,
                user_filter: typing.Callable[[int], bool] = None,
                item_filter: typing.Callable[[int], bool] = None,
                rating_filter: typing.Callable[[int, int, float], bool] = None
                ) -> float:

        if user_filter is None and item_filter is None and rating_filter is None:
            num_users = self.rating_matrix.get_num_users()
            num_items = self.rating_matrix.get_num_items()
            num_ratings = self.rating_matrix.get_num_ratings(relevant)

            return float(num_ratings) / float(num_users * num_items)
        else:
            if user_filter is None:
                user_filter = UserFilter.default
            if item_filter is None:
                item_filter = ItemFilter.default
            if rating_filter is None:
                rating_filter = RatingFilter.default

        users = list(filter(user_filter, self.rating_matrix.get_users()))
        items = list(filter(item_filter, self.rating_matrix.get_items()))

        num_users = len(users)
        num_items = len(items)

        if num_users == 0 or num_items == 0:
            return math.nan

        total = sum(sum(1.0 for item, rating in self.rating_matrix.get_user_ratings(user, relevant) if
                        item_filter(item) and rating_filter(user, item, rating))
                    for user in users)

        return float(total) / float(num_users * num_items)
