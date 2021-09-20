"""
Implementation of the properties of users / items / dataset according to ratings.
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

import numpy as np

from src.main.python.data import Impressions, RatingMatrix
from src.main.python.data.filters import *


class Impression:
    """
    Implementation of the properties of users and items according to impressions
    """

    def __init__(self, rating_matrix: RatingMatrix, impressions: Impressions):
        """
        Constructor.
        :param rating_matrix: the rating matrix.
        :param impressions: the impressions.
        """
        super().__init__(rating_matrix)
        self.impressions = impressions

    def total(self,
              user_filter: typing.Callable[[int], bool] = None,
              item_filter: typing.Callable[[int], bool] = None,
              impressions_filter: typing.Callable[[int, int], bool] = None
              ):
        """
        Finds the total number of impressions.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: the total number of impressions.
        """

        # Case 1: no filter is applied. In this case, it is just the number of ratings in the matrix.
        if user_filter is None and item_filter is None and impressions_filter is None:
            return self.impressions.num_impressions()
        # Case 2: we do apply filters, so the amount of ratings is not as easy to find:
        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if impressions_filter is None:
            impressions_filter = ImpressionsFilter.default()

        return sum((sum(1.0 for item, rating in self.impressions.get_user_impressions(user)
                        if item_filter(item) and impressions_filter(user, item))
                    for user in self.impressions.get_users() if user_filter(user)))

    def average(self,
                user_filter: typing.Callable[[int], bool] = None,
                item_filter: typing.Callable[[int], bool] = None,
                impressions_filter: typing.Callable[[int, int], bool] = None
                ):
        """
        Finds the average number of impressions.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: the average number of impressions.
        """
        # Case 1: no filter is applied. In this case, it is just the number of ratings in the matrix.
        if user_filter is None and item_filter is None and impressions_filter is None:
            return 1.0 if self.impressions.num_impressions() > 0 else math.nan

        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if impressions_filter is None:
            impressions_filter = ImpressionsFilter.default()

        for user in self.impressions.get_users():
            if user_filter(user):
                for item, rating in self.impressions.get_user_impressions(user):
                    if item_filter(item) and impressions_filter(user, item):
                        return 1.0
        return math.nan

    def max(self,
            user_filter: typing.Callable[[int], bool] = None,
            item_filter: typing.Callable[[int], bool] = None,
            impressions_filter: typing.Callable[[int, int], bool] = None
            ):
        """
        Finds the maximum number of impressions.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: the maximum number of impressions.
        """
        return self.average(user_filter=user_filter, item_filter=item_filter, impressions_filter=impressions_filter)

    def min(self,
            user_filter: typing.Callable[[int], bool] = None,
            item_filter: typing.Callable[[int], bool] = None,
            impressions_filter: typing.Callable[[int, int], bool] = None
            ):
        """
        Finds the minimum number of impressions.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: the minimum number of impressions.
        """
        return self.average(user_filter=user_filter, item_filter=item_filter, impressions_filter=impressions_filter)

    def total_users(self,
                    user_filter: typing.Callable[[int], bool] = None,
                    item_filter: typing.Callable[[int], bool] = None,
                    impressions_filter: typing.Callable[[int, int], bool] = None):
        """
        For each user, finds the total number of impressions.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: a dictionary containing the total number of impressions of each user.
        """
        values = dict()
        if user_filter is None:
            user_filter = UserFilter.default()

        if item_filter is None and impressions_filter is None:
            for user in self.impressions.get_users():
                if user_filter(user):
                    values[user] += len(self.impressions.get_user_impressions(user).items())
        else:
            if item_filter is None:
                item_filter = ItemFilter.default()
            if impressions_filter is None:
                impressions_filter = ImpressionsFilter.default()

            for user in self.impressions.get_users():
                if user_filter(user):
                    values[user] = sum(1.0 for item, rating in self.impressions.get_user_impressions(user)
                                       if item_filter(item) and impressions_filter(user, item))

    def average_users(self,
                      user_filter: typing.Callable[[int], bool] = None,
                      item_filter: typing.Callable[[int], bool] = None,
                      impressions_filter: typing.Callable[[int, int], bool] = None
                      ):
        """
        For each user, finds the average number of impressions.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: a dictionary containing the average number of impressions of each user.
        """
        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if impressions_filter is None:
            impressions_filter = ImpressionsFilter.default()

        values = dict()
        for user in self.impressions.get_users():
            if user_filter(user):
                values[user] = math.nan
                for item, rating in self.impressions.get_user_impressions(user):
                    if item_filter(item) and impressions_filter(user, item):
                        values[user] = 1.0
                        break
        return values

    def max_users(self,
                  user_filter: typing.Callable[[int], bool] = None,
                  item_filter: typing.Callable[[int], bool] = None,
                  impressions_filter: typing.Callable[[int, int], bool] = None
                  ):
        """
        For each user, finds the maximum number of impressions.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: a dictionary containing the maximum number of impressions of each user.
        """
        return self.average_users(user_filter=user_filter, item_filter=item_filter,
                                  impressions_filter=impressions_filter)

    def min_users(self,
                  user_filter: typing.Callable[[int], bool] = None,
                  item_filter: typing.Callable[[int], bool] = None,
                  impressions_filter: typing.Callable[[int, int], bool] = None
                  ):
        """
        For each user, finds the minimum number of impressions.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: a dictionary containing the minimum number of impressions of each user.
        """
        return self.average_users(user_filter=user_filter, item_filter=item_filter,
                                  impressions_filter=impressions_filter)

    def total_user(self,
                   user: int,
                   item_filter: typing.Callable[[int], bool] = None,
                   impressions_filter: typing.Callable[[int, int], bool] = None
                   ):
        """
        For a single user, finds the total number of impressions.
        :param user: identifier of the user.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: the total number of impressions of the user.
        """

        if not self.impressions.get_users().__contains__(user):
            return math.nan
        elif item_filter is None and impressions_filter is None:
            return self.impressions.get_num_user_impressions(user)
        else:
            if item_filter is None:
                item_filter = ItemFilter.default()
            if impressions_filter is None:
                impressions_filter = ImpressionsFilter.default()

            return sum(1.0 for item, rating in self.impressions.get_user_impressions(user)
                       if item_filter(item) and impressions_filter(user, item))

    def average_user(self,
                     user: int,
                     item_filter: typing.Callable[[int], bool] = None,
                     impressions_filter: typing.Callable[[int, int], bool] = None
                     ):
        """
        For a single user, finds the average number of impressions.
        :param user: identifier of the user.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: the average number of impressions of the user.
        """
        if item_filter is None:
            item_filter = ItemFilter.default()
        if impressions_filter is None:
            impressions_filter = ImpressionsFilter.default()

        if not self.impressions.get_users().__contains__(user):
            return math.nan
        else:
            for item, rating in self.impressions.get_user_impressions(user):
                if item_filter(item) and impressions_filter(user, item):
                    return 1.0
            return math.nan

    def max_user(self,
                 user: int,
                 item_filter: typing.Callable[[int], bool] = None,
                 impressions_filter: typing.Callable[[int, int], bool] = None
                 ):
        """
        For a single user, finds the maximum number of impressions.
        :param user: identifier of the user.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: the maximum number of impressions of the user.
        """
        return self.average_user(user, item_filter=item_filter, impressions_filter=impressions_filter)

    def min_user(self,
                 user: int,
                 item_filter: typing.Callable[[int], bool] = None,
                 impressions_filter: typing.Callable[[int, int], bool] = None
                 ):
        """
        For a single user, finds the minimum number of impressions.
        :param user: identifier of the user.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: the minimum number of impressions of the user.
        """
        return self.average_user(user, item_filter=item_filter, impressions_filter=impressions_filter)

    def average_over_users(self,
                           user_filter: typing.Callable[[int], bool] = None,
                           item_filter: typing.Callable[[int], bool] = None,
                           impressions_filter: typing.Callable[[int, int], bool] = None
                           ):
        """
        Finds the number of impressions averaged over the users.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: the number of impressions averaged over the users.
        """
        if user_filter is None and item_filter is None and impressions_filter is None:
            return float(self.impressions.get_num_impressions()) / float(self.impressions.get_num_users())

        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if impressions_filter is None:
            impressions_filter = ImpressionsFilter.default()

        return np.average((sum(1.0 for item, rating in self.impressions.get_user_impressions(user)
                               if item_filter(item) and impressions_filter(user, item))
                           for user in self.impressions.get_users() if user_filter(user)))

    def max_over_users(self,
                       user_filter: typing.Callable[[int], bool] = None,
                       item_filter: typing.Callable[[int], bool] = None,
                       impressions_filter: typing.Callable[[int, int], bool] = None
                       ):
        """
        Finds the maximum number of impressions across the users.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: the maximum number of impressions across the users.
        """
        return max((sum(1.0 for item, rating in self.impressions.get_user_impressions(user)
                        if item_filter and impressions_filter(user, item))
                    for user in self.impressions.get_users() if user_filter(user)))

    def min_over_users(self,
                       user_filter: typing.Callable[[int], bool] = None,
                       item_filter: typing.Callable[[int], bool] = None,
                       impressions_filter: typing.Callable[[int, int], bool] = None
                       ):
        """
        Finds the minimum number of impressions across the users.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: the minimum number of impressions across the users.
        """
        return min((sum(1.0 for item, rating in self.impressions.get_user_impressions(user)
                        if item_filter and impressions_filter(user, item))
                    for user in self.impressions.get_users() if user_filter(user)))

    def total_items(self,
                    user_filter: typing.Callable[[int], bool] = None,
                    item_filter: typing.Callable[[int], bool] = None,
                    impressions_filter: typing.Callable[[int, int], bool] = None):
        """
        For each item, finds the total number of impressions.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: a dictionary containing the total number of impressions of each item.
        """
        values = dict()
        if item_filter is None:
            item_filter = ItemFilter.default()

        if user_filter is None and impressions_filter is None:
            for item in self.impressions.get_items():
                if item_filter(item):
                    values[item] += len(self.impressions.get_item_impressions(item).items())

        else:
            if user_filter is None:
                user_filter = UserFilter.default()
            if impressions_filter is None:
                impressions_filter = ImpressionsFilter.default()

            for item in self.impressions.get_items():
                if item_filter(item):
                    values[item] = sum(1.0 for user, rating in self.impressions.get_item_impressions(item)
                                       if user_filter(user) and impressions_filter(user, item))

    def average_items(self,
                      user_filter: typing.Callable[[int], bool] = None,
                      item_filter: typing.Callable[[int], bool] = None,
                      impressions_filter: typing.Callable[[int, int], bool] = None
                      ):
        """
        For each item, finds the average number of impressions.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: a dictionary containing the average number of impressions of each item.
        """
        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if impressions_filter is None:
            impressions_filter = ImpressionsFilter.default()

        values = dict()
        for item in self.impressions.get_items():
            if item_filter(item):
                values[item] = math.nan
                for user, rating in self.impressions.get_item_impressions(item):
                    if user_filter(user) and impressions_filter(user, item):
                        values[item] = 1.0
                        break
        return values

    def max_items(self,
                  user_filter: typing.Callable[[int], bool] = None,
                  item_filter: typing.Callable[[int], bool] = None,
                  impressions_filter: typing.Callable[[int, int], bool] = None
                  ):
        """
        For each item, finds the maximum number of impressions.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: a dictionary containing the maximum number of impressions of each item.
        """
        return self.average_items(user_filter=user_filter, item_filter=item_filter,
                                  impressions_filter=impressions_filter)

    def min_items(self,
                  user_filter: typing.Callable[[int], bool] = None,
                  item_filter: typing.Callable[[int], bool] = None,
                  impressions_filter: typing.Callable[[int, int], bool] = None
                  ):
        """
        For each item, finds the minimum number of impressions.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: a dictionary containing the minimum number of impressions of each item.
        """
        return self.average_items(user_filter=user_filter, item_filter=item_filter,
                                  impressions_filter=impressions_filter)

    def total_item(self,
                   item: int,
                   user_filter: typing.Callable[[int], bool] = None,
                   impressions_filter: typing.Callable[[int, int], bool] = None
                   ):
        """
        For a single item, finds the total number of impressions.
        :param item: the identifier of the item.
        :param user_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: the total number of impressions of the item.
        """

        if not self.impressions.get_items().__contains__(item):
            return math.nan
        elif user_filter is None and impressions_filter is None:
            return self.impressions.get_num_item_impressions(item)
        else:
            if user_filter is None:
                user_filter = UserFilter.default()
            if impressions_filter is None:
                impressions_filter = ImpressionsFilter.default()

            return sum(1.0 for user, rating in self.impressions.get_item_impressions(item)
                       if user_filter(user) and impressions_filter(user, item))

    def average_item(self,
                     item: int,
                     user_filter: typing.Callable[[int], bool] = None,
                     impressions_filter: typing.Callable[[int, int], bool] = None
                     ):
        """
        For a single item, finds the average number of impressions.
        :param item: the identifier of the item.
        :param user_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: the average number of impressions of the item.
        """
        if user_filter is None:
            user_filter = UserFilter.default()
        if impressions_filter is None:
            impressions_filter = ImpressionsFilter.default()

        if not self.impressions.get_items().__contains__(item):
            return math.nan
        else:
            for user, rating in self.impressions.get_item_impressions(item):
                if user_filter(user) and impressions_filter(user, item):
                    return 1.0
            return math.nan

    def max_item(self,
                 item: int,
                 user_filter: typing.Callable[[int], bool] = None,
                 impressions_filter: typing.Callable[[int, int], bool] = None
                 ):
        """
        For a single item, finds the maximum number of impressions.
        :param item: the identifier of the item.
        :param user_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: the maximum number of impressions of the item.
        """
        return self.average_item(item, user_filter=user_filter, impressions_filter=impressions_filter)

    def min_item(self,
                 item: int,
                 user_filter: typing.Callable[[int], bool] = None,
                 impressions_filter: typing.Callable[[int, int], bool] = None
                 ):
        """
        For a single item, finds the minimum number of impressions.
        :param item: the identifier of the item.
        :param user_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: the minimum number of impressions of the item.
        """
        return self.average_item(item, user_filter=user_filter, impressions_filter=impressions_filter)

    def average_over_items(self,
                           user_filter: typing.Callable[[int], bool] = None,
                           item_filter: typing.Callable[[int], bool] = None,
                           impressions_filter: typing.Callable[[int, int], bool] = None
                           ):
        """
        Finds the number of impressions averaged over the items.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: the number of impressions averaged over the items.
        """
        if user_filter is None and item_filter is None and impressions_filter is None:
            return float(self.impressions.get_num_impressions()) / float(self.impressions.get_num_items())

        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if impressions_filter is None:
            impressions_filter = ImpressionsFilter.default()

        return np.average((sum(1.0 for user, rating in self.impressions.get_item_impressions(item)
                               if user_filter(user) and impressions_filter(user, item))
                           for item in self.impressions.get_items() if item_filter(item)))

    def max_over_items(self,
                       user_filter: typing.Callable[[int], bool] = None,
                       item_filter: typing.Callable[[int], bool] = None,
                       impressions_filter: typing.Callable[[int, int], bool] = None
                       ):
        """
        Finds the maximum number of impressions across the items.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: the maximum number of impressions across the items.
        """
        return max((sum(1.0 for user, rating in self.impressions.get_item_impressions(item)
                        if user_filter(user) and impressions_filter(user, item))
                    for item in self.impressions.get_items() if item_filter(item)))

    def min_over_items(self,
                       user_filter: typing.Callable[[int], bool] = None,
                       item_filter: typing.Callable[[int], bool] = None,
                       impressions_filter: typing.Callable[[int, int], bool] = None
                       ):
        """
        Finds the minimum number of impressions across the items.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) filter for selecting the impressions. By default, no filter is applied.
        :return: the minimum number of impressions across the items.
        """
        return min((sum(1.0 for user, rating in self.impressions.get_item_impressions(item)
                        if user_filter(user) and impressions_filter(user, item))
                    for item in self.impressions.get_items() if item_filter(item)))
