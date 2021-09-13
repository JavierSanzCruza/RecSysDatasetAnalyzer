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

from .global_property import GlobalProperty
import math


class Density(GlobalProperty):

    def compute(self, rating_matrix):
        num_users = rating_matrix.get_num_users()
        num_items = rating_matrix.get_num_items()
        num_ratings = rating_matrix.get_num_ratings()

        return float(num_ratings)/float(num_users*num_items)

    def compute_relevant(self, rating_matrix):
        num_users = rating_matrix.get_num_users()
        num_items = rating_matrix.get_num_items()
        num_ratings = rating_matrix.get_num_rel_ratings()

        return float(num_ratings)/float(num_users*num_items)

    def compute_filter(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x, rating_filter=lambda x: x):
        users = list(filter(user_filter, rating_matrix.get_users()))
        items = list(filter(item_filter, rating_matrix.get_items()))

        num_users = len(users)
        num_items = len(items)
        num_ratings = 0

        if num_users == 0 or num_items == 0:
            return math.nan

        for user in users:
            user_ratings = rating_matrix.get_user_ratings(user)
            f = filter(lambda y: item_filter(y[0]) and rating_filter((user, y[0], y[1])), user_ratings)
            for x in f:
                num_ratings += 1

        return float(num_ratings) / float(num_users * num_items)
