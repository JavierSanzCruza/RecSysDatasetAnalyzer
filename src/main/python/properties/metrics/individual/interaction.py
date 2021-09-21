"""
Implementation of the properties of users / items / dataset according to interactions.
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
import typing

from src.main.python.data.filters import UserFilter, ItemFilter, RatingFilter
from src.main.python.properties.metrics.individual.individual_property import IndividualProperty


class Interaction(IndividualProperty):
    """
    Class for counting the number of interactions of user and items.
    """
    def total(self,
              relevant: bool = False,
              user_filter: typing.Callable[[int], bool] = None,
              item_filter: typing.Callable[[int], bool] = None,
              rating_filter: typing.Callable[[int, int, float], bool] = None
              ):

        # Case 1: no filter is applied. In this case, it is just the number of ratings in the matrix.
        if user_filter is None and item_filter is None and rating_filter is None:
            return self.rating_matrix.get_num_ratings(relevant)
        # Case 2: we do apply filters, so the amount of ratings is not as easy to find:
        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        return sum((sum(1.0 for item, rating in self.rating_matrix.get_user_ratings(user, relevant)
                        if item_filter(item) and rating_filter(user, item, rating))
                    for user in self.rating_matrix.get_users() if user_filter(user)))

    def average(self,
                relevant: bool = False,
                user_filter: typing.Callable[[int], bool] = None,
                item_filter: typing.Callable[[int], bool] = None,
                rating_filter: typing.Callable[[int, int, float], bool] = None
                ):

        # Case 1: no filter is applied. In this case, it is just the number of ratings in the matrix.
        if user_filter is None and item_filter is None and rating_filter is None:
            if relevant:
                return 1.0 if self.rating_matrix.num_rel_ratings() > 0 else math.nan
            else:
                return 1.0 if self.rating_matrix.num_ratings() > 0 else math.nan

        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        for user in self.rating_matrix.get_users():
            if user_filter(user):
                for item, rating in self.rating_matrix.get_user_ratings(user, relevant):
                    if item_filter(item) and rating_filter(user, item, rating):
                        return 1.0
        return math.nan

    def max(self,
            relevant: bool = False,
            user_filter: typing.Callable[[int], bool] = None,
            item_filter: typing.Callable[[int], bool] = None,
            rating_filter: typing.Callable[[int, int, float], bool] = None
            ):

        return self.average(relevant=relevant, user_filter=user_filter, item_filter=item_filter,
                            rating_filter=rating_filter)

    def min(self,
            relevant: bool = False,
            user_filter: typing.Callable[[int], bool] = None,
            item_filter: typing.Callable[[int], bool] = None,
            rating_filter: typing.Callable[[int, int, float], bool] = None
            ):

        return self.average(relevant=relevant, user_filter=user_filter, item_filter=item_filter,
                            rating_filter=rating_filter)

    def total_users(self,
                    relevant: bool = False,
                    user_filter: typing.Callable[[int], bool] = None,
                    item_filter: typing.Callable[[int], bool] = None,
                    rating_filter: typing.Callable[[int, int, float], bool] = None):
        """
        For each user, finds the number of ratings (in the selection) added to the system.
        """
        values = dict()
        if user_filter is None:
            user_filter = UserFilter.default()

        if item_filter is None and rating_filter is None:
            for user in self.rating_matrix.get_users():
                if user_filter(user):
                    values[user] += len(self.rating_matrix.get_user_ratings(user, relevant).items())
        else:
            if item_filter is None:
                item_filter = ItemFilter.default()
            if rating_filter is None:
                rating_filter = RatingFilter.default()

            for user in self.rating_matrix.get_users():
                if user_filter(user):
                    values[user] = sum(1.0 for item, rating in self.rating_matrix.get_user_ratings(user, relevant)
                                       if item_filter(item) and rating_filter(user, item, rating))

    def average_users(self,
                      relevant: bool = False,
                      user_filter: typing.Callable[[int], bool] = None,
                      item_filter: typing.Callable[[int], bool] = None,
                      rating_filter: typing.Callable[[int, int, float], bool] = None
                      ):
        """
        For each user value of the ratings he/she introduced in the system.
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
                values[user] = math.nan
                for item, rating in self.rating_matrix.get_user_ratings(user, relevant):
                    if item_filter(item) and rating_filter(user, item, rating):
                        values[user] = 1.0
                        break
        return values

    def max_users(self,
                  relevant: bool = False,
                  user_filter: typing.Callable[[int], bool] = None,
                  item_filter: typing.Callable[[int], bool] = None,
                  rating_filter: typing.Callable[[int, int, float], bool] = None
                  ):
        return self.average_users(relevant=relevant, user_filter=user_filter, item_filter=item_filter,
                                  rating_filter=rating_filter)

    def min_users(self,
                  relevant: bool = False,
                  user_filter: typing.Callable[[int], bool] = None,
                  item_filter: typing.Callable[[int], bool] = None,
                  rating_filter: typing.Callable[[int, int, float], bool] = None
                  ):
        return self.average_users(relevant=relevant, user_filter=user_filter, item_filter=item_filter,
                                  rating_filter=rating_filter)

    def total_user(self,
                   user: int,
                   relevant: bool = False,
                   item_filter: typing.Callable[[int], bool] = None,
                   rating_filter: typing.Callable[[int, int, float], bool] = None
                   ):
        """
        Finds the sum of the ratings introduced in the system by a user.
        """

        if not self.rating_matrix.get_users().__contains__(user):
            return math.nan
        elif item_filter is None and rating_filter is None:
            return self.rating_matrix.get_num_user_ratings(user, relevant)
        else:
            if item_filter is None:
                item_filter = ItemFilter.default()
            if rating_filter is None:
                rating_filter = RatingFilter.default()

            return sum(1.0 for item, rating in self.rating_matrix.get_user_ratings(user, relevant)
                       if item_filter(item) and rating_filter(user, item, rating))

    def average_user(self,
                     user: int,
                     relevant: bool = False,
                     item_filter: typing.Callable[[int], bool] = None,
                     rating_filter: typing.Callable[[int, int, float], bool] = None
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
            for item, rating in self.rating_matrix.get_user_ratings(user, relevant):
                if item_filter(item) and rating_filter(user, item, rating):
                    return 1.0
            return math.nan

    def max_user(self,
                 user: int,
                 relevant: bool = False,
                 item_filter: typing.Callable[[int], bool] = None,
                 rating_filter: typing.Callable[[int, int, float], bool] = None
                 ):
        """
        Finds the sum of the ratings introduced in the system by a user.
        """
        return self.average_user(user, relevant=relevant, item_filter=item_filter, rating_filter=rating_filter)

    def min_user(self,
                 user: int,
                 relevant: bool = False,
                 item_filter: typing.Callable[[int], bool] = None,
                 rating_filter: typing.Callable[[int, int, float], bool] = None
                 ):
        """
        Finds the sum of the ratings introduced in the system by a user.
        """
        return self.average_user(user, relevant=relevant, item_filter=item_filter, rating_filter=rating_filter)

    def average_over_users(self,
                           relevant: bool = False,
                           user_filter: typing.Callable[[int], bool] = None,
                           item_filter: typing.Callable[[int], bool] = None,
                           rating_filter: typing.Callable[[int, int, float], bool] = None
                           ):

        if user_filter is None and item_filter is None and rating_filter is None:
            return float(self.rating_matrix.get_num_ratings(relevant)) / float(self.rating_matrix.get_num_users())

        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        count = 0.0
        total = 0.0
        for user in self.rating_matrix.get_users():
            if user_filter(user):
                count += 1.0
                total += sum(1.0 for item, rating in self.rating_matrix.get_user_ratings(user, relevant)
                             if item_filter(item) and rating_filter(user, item, rating))
        return total / count

    def max_over_users(self,
                       relevant: bool = False,
                       user_filter: typing.Callable[[int], bool] = None,
                       item_filter: typing.Callable[[int], bool] = None,
                       rating_filter: typing.Callable[[int, int, float], bool] = None
                       ):

        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        maximum = -math.inf
        for user in self.rating_matrix.get_users():
            if user_filter(user):
                score = sum(1.0 for item, rating in self.rating_matrix.get_user_ratings(user, relevant)
                            if item_filter(item) and rating_filter(user, item, rating))
                if score > maximum:
                    maximum = score

    def min_over_users(self,
                       relevant: bool = False,
                       user_filter: typing.Callable[[int], bool] = None,
                       item_filter: typing.Callable[[int], bool] = None,
                       rating_filter: typing.Callable[[int, int, float], bool] = None
                       ):

        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        minimum = math.inf
        for user in self.rating_matrix.get_users():
            if user_filter(user):
                score = sum(1.0 for item, rating in self.rating_matrix.get_user_ratings(user, relevant)
                            if item_filter(item) and rating_filter(user, item, rating))
                if score < minimum:
                    minimum = score

    def total_items(self,
                    relevant: bool = False,
                    user_filter: typing.Callable[[int], bool] = None,
                    item_filter: typing.Callable[[int], bool] = None,
                    rating_filter: typing.Callable[[int, int, float], bool] = None):
        """
        For each user, finds the number of ratings (in the selection) added to the system.
        """
        values = dict()
        if item_filter is None:
            item_filter = ItemFilter.default()

        if user_filter is None and rating_filter is None:
            for item in self.rating_matrix.get_items():
                if item_filter(item):
                    values[item] += len(self.rating_matrix.get_item_ratings(item, relevant).items())

        else:
            if user_filter is None:
                user_filter = UserFilter.default()
            if rating_filter is None:
                rating_filter = RatingFilter.default()

            for item in self.rating_matrix.get_items():
                if item_filter(item):
                    values[item] = sum(1.0 for user, rating in self.rating_matrix.get_item_ratings(item, relevant)
                                       if user_filter(user) and rating_filter(user, item, rating))

    def average_items(self,
                      relevant: bool = False,
                      user_filter: typing.Callable[[int], bool] = None,
                      item_filter: typing.Callable[[int], bool] = None,
                      rating_filter: typing.Callable[[int, int, float], bool] = None
                      ):
        """
        For each user value of the ratings he/she introduced in the system.
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
                values[item] = math.nan
                for user, rating in self.rating_matrix.get_item_ratings(item, relevant):
                    if user_filter(user) and rating_filter(user, item, rating):
                        values[item] = 1.0
                        break
        return values

    def max_items(self,
                  relevant: bool = False,
                  user_filter: typing.Callable[[int], bool] = None,
                  item_filter: typing.Callable[[int], bool] = None,
                  rating_filter: typing.Callable[[int, int, float], bool] = None
                  ):
        return self.average_items(relevant=relevant, user_filter=user_filter, item_filter=item_filter,
                                  rating_filter=rating_filter)

    def min_items(self,
                  relevant: bool = False,
                  user_filter: typing.Callable[[int], bool] = None,
                  item_filter: typing.Callable[[int], bool] = None,
                  rating_filter: typing.Callable[[int, int, float], bool] = None
                  ):
        return self.average_items(relevant=relevant, user_filter=user_filter, item_filter=item_filter,
                                  rating_filter=rating_filter)

    def total_item(self,
                   item: int,
                   relevant: bool = False,
                   user_filter: typing.Callable[[int], bool] = None,
                   rating_filter: typing.Callable[[int, int, float], bool] = None
                   ):
        """
        Finds the sum of the ratings introduced in the system by a user.
        """

        if not self.rating_matrix.get_items().__contains__(item):
            return math.nan
        elif user_filter is None and rating_filter is None:
            return self.rating_matrix.get_num_item_ratings(item, relevant)
        else:
            if user_filter is None:
                user_filter = UserFilter.default()
            if rating_filter is None:
                rating_filter = RatingFilter.default()

            return sum(1.0 for user, rating in self.rating_matrix.get_item_ratings(item, relevant)
                       if user_filter(user) and rating_filter(user, item, rating))

    def average_item(self,
                     item: int,
                     relevant: bool = False,
                     user_filter: typing.Callable[[int], bool] = None,
                     rating_filter: typing.Callable[[int, int, float], bool] = None
                     ):
        """
        Finds the sum of the ratings introduced in the system by a user.
        """
        if user_filter is None:
            user_filter = UserFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        if not self.rating_matrix.get_items().__contains__(item):
            return math.nan
        else:
            for user, rating in self.rating_matrix.get_item_ratings(item, relevant):
                if user_filter(user) and rating_filter(user, item, rating):
                    return 1.0
            return math.nan

    def max_item(self,
                 item: int,
                 relevant: bool = False,
                 user_filter: typing.Callable[[int], bool] = None,
                 rating_filter: typing.Callable[[int, int, float], bool] = None
                 ):
        """
        Finds the sum of the ratings introduced in the system by a user.
        """
        return self.average_item(item, relevant=relevant, user_filter=user_filter, rating_filter=rating_filter)

    def min_item(self,
                 item: int,
                 relevant: bool = False,
                 user_filter: typing.Callable[[int], bool] = None,
                 rating_filter: typing.Callable[[int, int, float], bool] = None
                 ):
        """
        Finds the sum of the ratings introduced in the system by a user.
        """
        return self.average_item(item, relevant=relevant, user_filter=user_filter, rating_filter=rating_filter)

    def average_over_items(self,
                           relevant: bool = False,
                           user_filter: typing.Callable[[int], bool] = None,
                           item_filter: typing.Callable[[int], bool] = None,
                           rating_filter: typing.Callable[[int, int, float], bool] = None
                           ):

        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        count = 0.0
        total = 0.0

        for item in self.rating_matrix.get_items():
            if item_filter(item):
                count += 1.0
                total += sum(1.0 for user, rating in self.rating_matrix.get_item_ratings(item, relevant)
                             if user_filter(user) and rating_filter(user, item, rating))
        return total / count

    def max_over_items(self,
                       relevant: bool = False,
                       user_filter: typing.Callable[[int], bool] = None,
                       item_filter: typing.Callable[[int], bool] = None,
                       rating_filter: typing.Callable[[int, int, float], bool] = None
                       ):

        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        return max((sum(1.0 for user, rating in self.rating_matrix.get_item_ratings(item, relevant)
                        if user_filter(user) and rating_filter(user, item, rating))
                    for item in self.rating_matrix.get_items() if item_filter(item)))

    def min_over_items(self,
                       relevant: bool = False,
                       user_filter: typing.Callable[[int], bool] = None,
                       item_filter: typing.Callable[[int], bool] = None,
                       rating_filter: typing.Callable[[int, int, float], bool] = None
                       ):

        if user_filter is None and item_filter is None and rating_filter is None:
            return float(self.rating_matrix.get_num_ratings(relevant)) / float(self.rating_matrix.get_num_items())

        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        return min((sum(1.0 for user, rating in self.rating_matrix.get_item_ratings(item, relevant)
                        if user_filter(user) and rating_filter(user, item, rating))
                    for item in self.rating_matrix.get_items() if item_filter(item)))
