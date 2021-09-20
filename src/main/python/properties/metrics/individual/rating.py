"""
Implementation of properties of users / items / dataset related to the different ratings in the rating matrix.
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

from src.main.python.properties.metrics.individual.individual_property import IndividualProperty
from src.main.python.data.filters import *

import math
import typing
import numpy as np


class Rating(IndividualProperty):
    """
    Implementation of properties of users / items / dataset related to the different ratings in the rating matrix.
    """

    def total(self,
              relevant: bool = False,
              user_filter: typing.Callable[[typing.Any], bool] = None,
              item_filter: typing.Callable[[typing.Any], bool] = None,
              rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
              ):
        """
        Computes the sum of the selected ratings of the matrix.
        """
        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        return sum((sum(rating for item, rating in self.rating_matrix.get_user_ratings(user, relevant)
                        if item_filter(item) and rating_filter(user, item, rating))
                    for user in self.rating_matrix.get_users() if user_filter(user)))

    def average(self,
                relevant: bool = False,
                user_filter: typing.Callable[[typing.Any], bool] = None,
                item_filter: typing.Callable[[typing.Any], bool] = None,
                rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                ):
        """
        Computes the average value of the ratings in the rating matrix.
        """

        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        total = 0.0
        count = 0.0
        for user in self.rating_matrix.get_users():
            if user_filter(user):
                for item, rating in self.rating_matrix.get_user_ratings(user, relevant):
                    if item_filter(item) and rating_filter(user, item, rating):
                        total += rating
                        count += 1.0

        return total / count

    def max(self,
            relevant: bool = False,
            user_filter: typing.Callable[[typing.Any], bool] = None,
            item_filter: typing.Callable[[typing.Any], bool] = None,
            rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
            ):
        """
        Computes the maximum value of the ratings of the matrix.
        """
        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        return max((max(rating for item, rating in self.rating_matrix.get_user_ratings(user, relevant)
                        if item_filter(item) and rating_filter(user, item, rating))
                    for user in self.rating_matrix.get_users() if user_filter(user)))

    def min(self,
            relevant: bool = False,
            user_filter: typing.Callable[[typing.Any], bool] = None,
            item_filter: typing.Callable[[typing.Any], bool] = None,
            rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
            ):
        """
        Computes the minimum value of the ratings of the matrix.
        """

        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        return min((min(rating for item, rating in self.rating_matrix.get_user_ratings(user, relevant)
                        if item_filter(item) and rating_filter(user, item, rating))
                    for user in self.rating_matrix.get_users() if user_filter(user)))

    # Methods for computing the values for the different users

    def total_users(self,
                    relevant: bool = False,
                    user_filter: typing.Callable[[typing.Any], bool] = None,
                    item_filter: typing.Callable[[typing.Any], bool] = None,
                    rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None):
        """
        For each user, finds the sum of his/her ratings in the system.
        """
        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        values = dict()
        for user in self.rating_matrix.get_users():
            if user_filter(user):
                values[user] = sum(rating for item, rating in self.rating_matrix.get_user_ratings(user, relevant)
                                   if item_filter(item) and rating_filter(user, item, rating))
        return values

    def average_users(self,
                      relevant: bool = False,
                      user_filter: typing.Callable[[typing.Any], bool] = None,
                      item_filter: typing.Callable[[typing.Any], bool] = None,
                      rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                      ):
        """
        For each user, finds the average value of the ratings he/she introduced in the system.
        """
        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        values = dict()
        for user in self.rating_matrix.get_users():
            if user_filter(user):
                values[user] = np.average(
                    (rating for item, rating in self.rating_matrix.get_user_ratings(user, relevant)
                     if item_filter(item) and rating_filter(user, item, rating)
                     ))

        return values

    def max_users(self,
                  relevant: bool = False,
                  user_filter: typing.Callable[[typing.Any], bool] = None,
                  item_filter: typing.Callable[[typing.Any], bool] = None,
                  rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                  ):
        """
        For each user, finds the maximum value of the ratings he/she introduced in the system.
        """
        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        values = dict()
        for user in self.rating_matrix.get_users():
            if user_filter(user):
                values[user] = max(
                    (rating for item, rating in self.rating_matrix.get_user_ratings(user, relevant)
                     if item_filter(item) and rating_filter(user, item, rating)
                     ))

        return values

    def min_users(self,
                  relevant: bool = False,
                  user_filter: typing.Callable[[typing.Any], bool] = None,
                  item_filter: typing.Callable[[typing.Any], bool] = None,
                  rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                  ):
        """
        For each user, finds the minimum value of the ratings he/she introduced in the system.
        """
        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        values = dict()
        for user in self.rating_matrix.get_users():
            if user_filter(user):
                values[user] = min(
                    (rating for item, rating in self.rating_matrix.get_user_ratings(user, relevant)
                     if item_filter(item) and rating_filter(user, item, rating)
                     ))

        return values

    def total_user(self,
                   user: typing.Any,
                   relevant: bool = False,
                   item_filter: typing.Callable[[typing.Any], bool] = None,
                   rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                   ):
        """
        Finds the sum of the ratings introduced in the system by a user.
        """
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        if not self.rating_matrix.get_users().__contains__(user):
            return math.nan
        else:
            return sum(rating for item, rating in self.rating_matrix.get_user_ratings(user, relevant)
                       if item_filter(item) and rating_filter(user, item, rating))

    def average_user(self,
                     user: typing.Any,
                     relevant: bool = False,
                     item_filter: typing.Callable[[typing.Any], bool] = None,
                     rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                     ):
        """
        Finds the sum of the ratings introduced in the system by a user.
        """
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        if not self.rating_matrix.get_users().__contains__(user):
            return math.nan
        else:
            return np.average(rating for item, rating in self.rating_matrix.get_user_ratings(user, relevant)
                              if item_filter(item) and rating_filter(user, item, rating))

    def max_user(self,
                 user: typing.Any,
                 relevant: bool = False,
                 item_filter: typing.Callable[[typing.Any], bool] = None,
                 rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                 ):
        """
        Finds the sum of the ratings introduced in the system by a user.
        """
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        if not self.rating_matrix.get_users().__contains__(user):
            return math.nan
        else:
            return max(rating for item, rating in self.rating_matrix.get_user_ratings(user, relevant)
                       if item_filter(item) and rating_filter(user, item, rating))

    def min_user(self,
                 user: typing.Any,
                 relevant: bool = False,
                 item_filter: typing.Callable[[typing.Any], bool] = None,
                 rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                 ):
        """
        Finds the sum of the ratings introduced in the system by a user.
        """
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        if not self.rating_matrix.get_users().__contains__(user):
            return math.nan
        else:
            return min(rating for item, rating in self.rating_matrix.get_user_ratings(user, relevant)
                       if item_filter(item) and rating_filter(user, item, rating))

    def average_over_users(self,
                           relevant: bool = False,
                           user_filter: typing.Callable[[typing.Any], bool] = None,
                           item_filter: typing.Callable[[typing.Any], bool] = None,
                           rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                           ):
        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        return np.average((sum(rating for item, rating in self.rating_matrix.get_user_ratings(user, relevant)
                               if item_filter(item) and rating_filter(user, item, rating))
                           for user in self.rating_matrix.get_users() if user_filter(user)))

    def max_over_users(self,
                       relevant: bool = False,
                       user_filter: typing.Callable[[typing.Any], bool] = None,
                       item_filter: typing.Callable[[typing.Any], bool] = None,
                       rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                       ):
        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        return max((sum(rating for item, rating in self.rating_matrix.get_user_ratings(user, relevant)
                        if item_filter(item) and rating_filter(user, item, rating))
                    for user in self.rating_matrix.get_users() if user_filter(user)))

    def min_over_users(self,
                       relevant: bool = False,
                       user_filter: typing.Callable[[typing.Any], bool] = None,
                       item_filter: typing.Callable[[typing.Any], bool] = None,
                       rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                       ):
        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        return min((sum(rating for item, rating in self.rating_matrix.get_user_ratings(user, relevant)
                        if item_filter(item) and rating_filter(user, item, rating))
                    for user in self.rating_matrix.get_users() if user_filter(user)))

    # Methods for computing the values for the different users

    def total_items(self,
                    relevant: bool = False,
                    user_filter: typing.Callable[[typing.Any], bool] = None,
                    item_filter: typing.Callable[[typing.Any], bool] = None,
                    rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None):
        """
        For each user, finds the sum of his/her ratings in the system.
        """
        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        values = dict()
        for item in self.rating_matrix.get_items():
            if item_filter(item):
                values[item] = sum(rating for user, rating in self.rating_matrix.get_item_ratings(item, relevant)
                                   if user_filter(user) and rating_filter(user, item, rating))
        return values

    def average_items(self,
                      relevant: bool = False,
                      user_filter: typing.Callable[[typing.Any], bool] = None,
                      item_filter: typing.Callable[[typing.Any], bool] = None,
                      rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                      ):
        """
        For each user, finds the average value of the ratings he/she introduced in the system.
        """
        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        values = dict()
        for item in self.rating_matrix.get_items():
            if item_filter(item):
                values[item] = np.average(
                    (rating for user, rating in self.rating_matrix.get_item_ratings(item, relevant)
                     if user_filter(user) and rating_filter(user, item, rating)
                     ))

        return values

    def max_items(self,
                  relevant: bool = False,
                  user_filter: typing.Callable[[typing.Any], bool] = None,
                  item_filter: typing.Callable[[typing.Any], bool] = None,
                  rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                  ):
        """
        For each user, finds the maximum value of the ratings he/she introduced in the system.
        """
        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        values = dict()
        for item in self.rating_matrix.get_items():
            if item_filter(item):
                values[item] = max(
                    (rating for user, rating in self.rating_matrix.get_item_ratings(item, relevant)
                     if user_filter(user) and rating_filter(user, item, rating)
                     ))

        return values

    def min_items(self,
                  relevant: bool = False,
                  user_filter: typing.Callable[[typing.Any], bool] = None,
                  item_filter: typing.Callable[[typing.Any], bool] = None,
                  rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                  ):
        """
        For each user, finds the maximum value of the ratings he/she introduced in the system.
        """
        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        values = dict()
        for item in self.rating_matrix.get_items():
            if item_filter(item):
                values[item] = min(
                    (rating for user, rating in self.rating_matrix.get_item_ratings(item, relevant)
                     if user_filter(user) and rating_filter(user, item, rating)
                     ))

        return values

    def total_item(self,
                   item: typing.Any,
                   relevant: bool = False,
                   user_filter: typing.Callable[[typing.Any], bool] = None,
                   rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                   ):
        """
        Finds the sum of the ratings introduced in the system by a user.
        """
        if user_filter is None:
            user_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        if not self.rating_matrix.get_items().__contains__(item):
            return math.nan
        else:
            return sum(rating for user, rating in self.rating_matrix.get_item_ratings(item, relevant)
                       if user_filter(user) and rating_filter(user, item, rating))

    def average_item(self,
                     item: typing.Any,
                     relevant: bool = False,
                     user_filter: typing.Callable[[typing.Any], bool] = None,
                     rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                     ):
        """
        Finds the sum of the ratings introduced in the system by a user.
        """
        if user_filter is None:
            user_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        if not self.rating_matrix.get_items().__contains__(item):
            return math.nan
        else:
            return np.average(rating for user, rating in self.rating_matrix.get_item_ratings(item, relevant)
                              if user_filter(user) and rating_filter(user, item, rating))

    def max_item(self,
                 item: typing.Any,
                 relevant: bool = False,
                 user_filter: typing.Callable[[typing.Any], bool] = None,
                 rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                 ):
        """
        Finds the sum of the ratings introduced in the system by a user.
        """
        if user_filter is None:
            user_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        if not self.rating_matrix.get_items().__contains__(item):
            return math.nan
        else:
            return max(rating for user, rating in self.rating_matrix.get_item_ratings(item, relevant)
                       if user_filter(user) and rating_filter(user, item, rating))

    def min_item(self,
                 item: typing.Any,
                 relevant: bool = False,
                 user_filter: typing.Callable[[typing.Any], bool] = None,
                 rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                 ):
        """
        Finds the sum of the ratings introduced in the system by a user.
        """
        if user_filter is None:
            user_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        if not self.rating_matrix.get_items().__contains__(item):
            return math.nan
        else:
            return min(rating for user, rating in self.rating_matrix.get_item_ratings(item, relevant)
                       if user_filter(user) and rating_filter(user, item, rating))

    def average_over_items(self,
                           relevant: bool = False,
                           user_filter: typing.Callable[[typing.Any], bool] = None,
                           item_filter: typing.Callable[[typing.Any], bool] = None,
                           rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                           ):
        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        return np.average((sum(rating for user, rating in self.rating_matrix.get_item_ratings(item, relevant)
                               if user_filter(user) and rating_filter(user, item, rating))
                           for item in self.rating_matrix.get_items() if item_filter(item)))

    def max_over_items(self,
                       relevant: bool = False,
                       user_filter: typing.Callable[[typing.Any], bool] = None,
                       item_filter: typing.Callable[[typing.Any], bool] = None,
                       rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                       ):
        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        return max((sum(rating for user, rating in self.rating_matrix.get_item_ratings(item, relevant)
                        if user_filter(user) and rating_filter(user, item, rating))
                    for item in self.rating_matrix.get_items() if item_filter(item)))

    def min_over_items(self,
                       relevant: bool = False,
                       user_filter: typing.Callable[[typing.Any], bool] = None,
                       item_filter: typing.Callable[[typing.Any], bool] = None,
                       rating_filter: typing.Callable[[typing.Any, typing.Any, float], bool] = None
                       ):
        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        return min((sum(rating for user, rating in self.rating_matrix.get_item_ratings(item, relevant)
                        if user_filter(user) and rating_filter(user, item, rating))
                    for item in self.rating_matrix.get_items() if item_filter(item)))
