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
from functools import reduce

from .adding_return import AddingReturn
from ..utils.optional import Optional


class RatingMatrix:
    """
    Representation of the basic rating matrix of a recommendation dataset.
    It just includes a) users, b) items and c) ratings between users and items.
    """

    def __init__(self, threshold, binarize, update):
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

    def add_user(self, user_id):
        """
        Adds a new user to the rating matrix.
        :param user_id: the identifier of the user.
        :return: true if we add the user, false otherwise.
        """
        if self.users.__contains__(user_id):
            return False
        else:
            self.users.add(user_id)
            self.user_2_item_matrix[user_id] = dict()
            return True

    def add_item(self, item_id):
        """
        Adds a new item to the rating matrix.
        :param item_id: the identifier of the item.
        :return: true if we add the item, false otherwise.
        """
        if self.items.__contains__(item_id):
            return False
        else:
            self.items.add(item_id)
            self.item_2_user_matrix[item_id] = dict()
            return True

    def rate(self, user_id, item_id, value):
        """
        Adds a new rating to the matrix.
        :param user_id: the identifier of the user.
        :param item_id: the identifier of the item.
        :param value: the value of the rating.
        :return: AddingReturn.ADDED if the rating is new, AddingReturn.UPDATED if we just updated it, AddingReturn.NONE
        if it kept the same, AddingReturn.ERROR if something failed.
        """
        if math.isnan(value):
            return AddingReturn.ERROR

        if self.users.__contains__(user_id) and self.items.__contains__(item_id):
            oldval = self.user_2_item_matrix[user_id].get(item_id, math.nan)
            val = (1.0 if value >= self.threshold else 0.0) if self.binarize else value
            rel = value >= self.threshold

            self.num_total_ratings += 1
            self.num_total_rel_ratings += 1 if rel else 0

            if math.isnan(oldval):  # The rating does not exist.
                self.user_2_item_matrix[user_id][item_id] = val
                self.item_2_user_matrix[item_id][user_id] = val
                self.num_rel_ratings += 1 if rel else 0
                self.num_ratings += 1
                return AddingReturn.ADDED
            elif self.binarize and self.update:  # The rating already exists, and we count the number of positives.
                oldrel = oldval > 0
                self.user_2_item_matrix[user_id][item_id] = val + oldval
                self.item_2_user_matrix[item_id][user_id] = val + oldval
                self.num_rel_ratings += 1 if (not oldrel and rel) else 0
                return AddingReturn.UPDATED
            elif self.update and val > oldval:
                oldrel = oldval >= self.threshold
                val = max(oldval, val)
                self.num_rel_ratings += 1 if (not oldrel and rel) else 0
                self.user_2_item_matrix[user_id][item_id] = val
                self.item_2_user_matrix[item_id][user_id] = val
                return AddingReturn.UPDATED
            else:
                return AddingReturn.NONE
        else:
            return AddingReturn.ERROR

    def get_num_ratings(self):
        """
        Obtains the number of ratings (not repeated).
        :return: the number of ratings (not repeated).
        """
        return self.num_ratings

    def get_num_user_ratings(self, user_id):
        """
        Obtains the number of ratings of a user (not repeated)
        :param user_id: the identifier of the user.
        :return: the number of ratings of the user (not repeated)
        """
        if self.user_2_item_matrix.__contains__(user_id):
            return len(self.user_2_item_matrix.get(user_id))
        return 0

    def get_num_user_rel_ratings(self, user_id):
        """
        Obtains the number of ratings of a user (not repeated)
        :param user_id: the identifier of the user.
        :return: the number of ratings of the user (not repeated)
        """
        if self.user_2_item_matrix.__contains__(user_id):
            return reduce(lambda x, y: x + 1,
                          map(lambda x: 1,
                              filter(lambda item, rating: self.is_relevant(rating),
                                     self.user_2_item_matrix.get(user_id).items())))
        return 0

    def get_num_item_ratings(self, item_id):
        """
        Obtains the number of ratings of a item (not repeated)
        :param item_id: the identifier of the item.
        :return: the number of ratings of the item (not repeated)
        """
        if self.item_2_user_matrix.__contains__(item_id):
            return len(self.item_2_user_matrix.get(item_id))
        return 0

    def get_num_item_rel_ratings(self, item_id):
        """
        Obtains the number of ratings of a user (not repeated)
        :param item_id: the identifier of the user.
        :return: the number of ratings of the user (not repeated)
        """
        if self.item_2_user_matrix.__contains__(item_id):
            return reduce(lambda x, y: x + 1,
                          map(lambda x: 1,
                              filter(lambda user, rating: self.is_relevant(rating),
                                     self.item_2_user_matrix.get(item_id).items())))
        return 0

    def get_num_rel_ratings(self):
        """
        Obtains the number of relevant ratings (not repeated).
        :return: the number of relevant ratings (not repeated).
        """
        return self.num_rel_ratings

    def get_num_total_ratings(self):
        """
        Obtains the number of ratings (with repetitions).
        :return: the number of ratings (with repetitions).
        """
        return self.num_total_ratings

    def get_num_total_rel_ratings(self):
        """
        Obtains the number of relevant ratings (with repetitions).
        :return: the number of relevant ratings (with repetitions).
        """
        return self.num_total_rel_ratings

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
        return self.users.__iter__()

    def get_items(self):
        """
        Obtains an iterator of the items in the system.
        :return: the iterator of the items in the system.
        """
        return self.items.__iter__()

    def get_rating(self, user_id, item_id):
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

    def get_user_ratings(self, user_id):
        """
        Obtains all the ratings of an individual user.
        :param user_id: the identifier of the user.
        :return: the ratings of the user
        """
        if not self.user_2_item_matrix.__contains__(user_id) or self.user_2_item_matrix.get(user_id).__len__() == 0:
            return [].__iter__()
        else:
            return self.user_2_item_matrix.get(user_id).items().__iter__()

    def get_item_ratings(self, item_id):
        """
        Obtains all the ratings given to an individual item.
        :param item_id: the identifier of the item.
        :return: the ratings given to the item.
        """
        if not self.item_2_user_matrix.__contains__(item_id) or self.item_2_user_matrix.get(item_id).__len__() == 0:
            return [].__iter__()
        else:
            return self.item_2_user_matrix.get(item_id).items().__iter__()

    def get_relevant_user_ratings(self, user_id):
        """
        Obtains all the relevant ratings of an individual user.
        :param user_id: the identifier of the user.
        :return: the relevant ratings of the user.
        """
        if not self.user_2_item_matrix.__contains__(user_id) or self.user_2_item_matrix.get(user_id).__len__() == 0:
            return [].__iter__()
        else:
            return filter(lambda x: self.is_relevant(x[1]), self.user_2_item_matrix.get(user_id).items())

    def get_relevant_item_ratings(self, item_id):
        """
        Obtains all the relevant ratings given to an individual item.
        :param item_id: the identifier of the item.
        :return: the relevant ratings of the item.
        """
        if not self.item_2_user_matrix.__contains__(item_id) or self.item_2_user_matrix.get(item_id).__len__() == 0:
            return [].__iter__()
        else:
            return filter(lambda x: self.is_relevant(x[1]), self.item_2_user_matrix.get(item_id).items())

    def is_relevant(self, value):
        """
        Checks whether a rating value is relevant for the dataset or not.
        :param value: the rating value.
        :return: whether the rating is relevant or not.
        """
        if self.binarize:
            return value > 0.0
        else:
            return value >= self.threshold
