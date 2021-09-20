"""
Representation of the basic rating matrix of a recommendation dataset.
It just includes a) users, b) items and c) ratings between users and items.
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

from .adding_return import AddingReturn
from .filters import UserFilter, ItemFilter, RatingFilter
from ..utils.optional import Optional


class RatingMatrix:
    """
    Representation of the basic rating matrix of a recommendation dataset.
    It just includes a) users, b) items and c) ratings between users and items.
    """

    def __init__(self,
                 threshold: float,
                 binarize: bool,
                 update: bool):
        """
        Initializes the rating matrix.
        :param threshold: the relevance threshold of the ratings.
        :param binarize: true if we want to store binarized ratings, false otherwise.
        :param update:  true if a) we want to add the number of relevant ratings to a user (when binarizing) or
                        b) we want to take the maximum possible value for a rating (when we do not binarize).
                        False otherwise.
        """
        self.users = set()
        self.items = set()

        self.user_2_item_matrix = dict()
        self.item_2_user_matrix = dict()

        self.num_ratings = 0
        self.num_rel_ratings = 0

        self.num_total_ratings = 0
        self.num_total_rel_ratings = 0

        self.threshold = threshold
        self.binarize = binarize
        self.update = update

    def add_user(self,
                 user: int):
        """
        Adds a new user to the rating matrix.
        :param user: the identifier of the user.
        :return: true if we add the user, false otherwise.
        """
        if self.users.__contains__(user):
            return False
        else:
            self.users.add(user)
            self.user_2_item_matrix[user] = dict()
            return True

    def add_item(self,
                 item: int):
        """
        Adds a new item to the rating matrix.
        :param item: the identifier of the item.
        :return: true if we add the item, false otherwise.
        """
        if self.items.__contains__(item):
            return False
        else:
            self.items.add(item)
            self.item_2_user_matrix[item] = dict()
            return True

    def rate(self,
             user: int,
             item: int,
             rating: float):
        """
        Adds a new rating to the matrix.
        :param user: the identifier of the user.
        :param item: the identifier of the item.
        :param rating: the value of the rating.
        :return: AddingReturn.ADDED if the rating is new, AddingReturn.UPDATED if we just updated it, AddingReturn.NONE
        if it kept the same, AddingReturn.ERROR if something failed.
        """
        if math.isnan(rating):
            return AddingReturn.ERROR

        if self.users.__contains__(user) and self.items.__contains__(item):
            oldval = self.user_2_item_matrix[user].get(item, math.nan)
            val = (1.0 if rating >= self.threshold else 0.0) if self.binarize else rating
            rel = rating >= self.threshold

            self.num_total_ratings += 1
            self.num_total_rel_ratings += 1 if rel else 0

            if math.isnan(oldval):  # The rating does not exist.
                self.user_2_item_matrix[user][item] = val
                self.item_2_user_matrix[item][user] = val
                self.num_rel_ratings += 1 if rel else 0
                self.num_ratings += 1
                return AddingReturn.ADDED
            elif self.binarize and self.update:  # The rating already exists, and we count the number of positives.
                oldrel = oldval > 0
                self.user_2_item_matrix[user][item] = val + oldval
                self.item_2_user_matrix[item][user] = val + oldval
                self.num_rel_ratings += 1 if (not oldrel and rel) else 0
                return AddingReturn.UPDATED
            elif self.update and val > oldval:
                oldrel = oldval >= self.threshold
                val = max(oldval, val)
                self.num_rel_ratings += 1 if (not oldrel and rel) else 0
                self.user_2_item_matrix[user][item] = val
                self.item_2_user_matrix[item][user] = val
                return AddingReturn.UPDATED
            else:
                return AddingReturn.NONE
        else:
            return AddingReturn.ERROR

    def get_num_ratings(self,
                        relevant: bool = False):
        """
        Obtains the number of ratings (not repeated).
        :param relevant: True if we want to retrieve the number of relevant ratings, False otherwise
        :return: the number of ratings (not repeated).
        """
        return self.num_rel_ratings if relevant else self.num_ratings

    def get_num_total_ratings(self,
                              relevant: bool = False):
        """
        Obtains the number of ratings (with repetitions).
        :return: the number of ratings (with repetitions).
        """
        return self.num_total_rel_ratings if relevant else self.num_total_ratings

    def get_num_user_ratings(self,
                             user: int,
                             relevant: bool = False):
        """
        Obtains the number of ratings of a user (not repeated)
        :param user: the identifier of the user.
        :param relevant: True if we want to retrieve the number of relevant ratings.
        :return: the number of ratings of the user (not repeated)
        """

        if self.user_2_item_matrix.__contains__(user):
            if relevant:
                sum((1.0 for item, rating in self.user_2_item_matrix.get(user).items() if self.is_relevant(rating)))
            else:
                return len(self.user_2_item_matrix.get(user).items())
        return 0

    def get_num_item_ratings(self,
                             item: int,
                             relevant: bool = False):
        """
        Obtains the number of ratings of a item (not repeated)
        :param item: the identifier of the item.
        :param relevant: True if we want to retrieve the number of relevant ratings.
        :return: the number of ratings of the item (not repeated)
        """

        if self.item_2_user_matrix.__contains__(item):
            if relevant:
                sum((1.0 for item, rating in self.item_2_user_matrix.get(item).items() if self.is_relevant(rating)))
            else:
                return len(self.item_2_user_matrix.get(item).items())
        return 0

    def get_num_users(self):
        """
        Obtains the number of users in the dataset.
        :return: the number of users in the dataset.
        """
        return self.users.__len__()

    def get_num_items(self):
        """
        Obtains the number of items in the dataset.
        :return: the number of items in the dataset.
        """
        return self.items.__len__()

    def get_users(self):
        """
        Obtains an iterator of the users in the system.
        :return: the iterator of the users in the system.
        """
        return (user for user in self.get_users())

    def get_items(self):
        """
        Obtains an iterator of the items in the system.
        :return: the iterator of the items in the system.
        """
        return (item for item in self.get_items())

    def get_rating(self,
                   user_id: int,
                   item_id: int):
        """
        Obtains an individual rating.
        :param user_id: the identifier of the user
        :param item_id: the identifier of the item
        :return: the individual rating if exists, an empty object otherwise.
        """
        if self.user_2_item_matrix.__contains__(user_id) and self.user_2_item_matrix.get(user_id).__contains__(item_id):
            return Optional.of(self.user_2_item_matrix.get(user_id).get(item_id))
        else:
            return Optional.empty()

    def get_user_ratings(self,
                         user: int,
                         relevant: bool = False):
        """
        Obtains all the ratings of an individual user.
        :param user: the identifier of the user.
        :param relevant: True if we want to retrieve the relevant ratings, False if we want to retrieve all.
        :return: the ratings of the user
        """

        if relevant:
            return ((item, rating) for item, rating in self.user_2_item_matrix.get(user, []).items()
                    if self.is_relevant(rating))
        else:
            return ((item, rating) for item, rating in self.user_2_item_matrix.get(user, []).items())

    def get_item_ratings(self,
                         item: int,
                         relevant: bool = False):
        """
        Obtains all the ratings given to an individual item.
        :param item: the identifier of the item.
        :param relevant: True if we want to retrieve the relevant ratings, False if we want to retrieve all.
        :return: the ratings given to the item.
        """

        if relevant:
            return ((user, rating) for user, rating in self.item_2_user_matrix.get(item, []).items()
                    if self.is_relevant(rating))
        else:
            return ((user, rating) for user, rating in self.item_2_user_matrix.get(item, []).items())

    def is_relevant(self, value):
        """
        Checks whether a rating value is relevant for the dataset or not.
        :param value: the rating value.
        :return: whether the rating is relevant or not.
        """
        return value > 0.0 if self.binarize else value >= self.threshold

    def filter(self,
               user_filter: typing.Callable[[int], bool] = None,
               item_filter: typing.Callable[[int], bool] = None,
               rating_filter: typing.Callable[[int, int, float], bool] = None
               ):
        """
        Obtains a proxy rating matrix containing only a fraction of the ratings.
        :param user_filter: (OPTIONAL) a filter for selecting the users to keep. By default, no filter is applied.
        :param item_filter: (OPTIONAL) a filter for selecting the items to keep. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) a filter for selecting the ratings to keep. By default, no filter is applied.
        :returns: a rating matrix containing the selected ratings.
        """

        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if rating_filter is None:
            rating_filter = RatingFilter.default()

        if self.binarize:
            aux_matrix = RatingMatrix(0.5, False, False)
        else:
            aux_matrix = RatingMatrix(self.threshold, False, False)

        for item in filter(item_filter, self.get_items()):
            aux_matrix.add_item(item)
        for user in filter(user_filter, self.get_users()):
            aux_matrix.add_user(user)
            for item, rating in self.get_user_ratings(user, False):
                if item_filter(item) and rating_filter(user, item, rating):
                    aux_matrix.rate(user, item, rating)

        return aux_matrix
