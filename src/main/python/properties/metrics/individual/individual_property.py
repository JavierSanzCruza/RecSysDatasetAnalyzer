"""
Abstract implementation of individual properties of users / items / ratings.
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

from abc import ABC, abstractmethod
import math

class IndividualProperty(ABC):

    # Methods analyzing the whole rating matrix

    @abstractmethod
    def total(self, rating_matrix):
        """
        Finds the total value of the property over all the possible ratings
        :param rating_matrix: the rating matrix
        :return: the total value.
        """
        pass

    @abstractmethod
    def total_relevant(self, rating_matrix):
        """
        Finds the total value of the property over all the relevant ratings.
        :param rating_matrix: the rating matrix.
        :return: the total value.
        """
        pass

    @abstractmethod
    def total_filter(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                     rating_filter=lambda x: x):
        """
        Finds the total value of the property over all the relevant ratings.
        :param rating_matrix: the rating matrix.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: the total value.
        """
        pass


    @abstractmethod
    def average(self, rating_matrix):
        """
        Finds the average value of the property over all the possible ratings
        :param rating_matrix: the rating matrix
        :return: the average value.
        """
        pass

    @abstractmethod
    def average_relevant(self, rating_matrix):
        """
        Finds the average value of the property over all the relevant ratings.
        :param rating_matrix: the rating matrix.
        :return: the average value.
        """
        pass

    @abstractmethod
    def average_filter(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                       rating_filter=lambda x: x):
        """
        Finds the average value of the property over all the relevant ratings.
        :param rating_matrix: the rating matrix.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: the average value.
        """
        pass

    @abstractmethod
    def max(self, rating_matrix):
        """
        Finds the maximum value of the property over all the ratings.
        :param rating_matrix: the rating matrix.
        :return: the maximum value for the property.
        """
        pass

    @abstractmethod
    def max_relevant(self, rating_matrix):
        """
        Finds the maximum value of the property over all the relevant ratings.
        :param rating_matrix: the rating matrix.
        :return: the maximum value for the property.
        """
        pass

    @abstractmethod
    def max_filter(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x, rating_filter=lambda x: x):
        """
        Finds the maximum value of the property over a selection of ratings.
        :param rating_matrix: the rating matrix.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: the maximum value for the property.
        """
        pass

    @abstractmethod
    def min(self, rating_matrix):
        """
        Finds the minimum value of the property over all the ratings.
        :param rating_matrix: the rating matrix.
        :return: the minimum value for the property.
        """
        pass

    @abstractmethod
    def min_relevant(self, rating_matrix):
        """
        Finds the minimum value of the property over all the relevant ratings.
        :param rating_matrix: the rating matrix.
        :return: the minimum value for the property.
        """
        pass

    @abstractmethod
    def min_filter(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x, rating_filter=lambda x: x):
        """
        Finds the minimum value of the property over a selection of ratings.
        :param rating_matrix: the rating matrix.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: the minimum value for the property.
        """
        pass

    # Methods for analyzing individual users:

    @abstractmethod
    def total_users(self, rating_matrix):
        """
        Finds the total value of the property for the different users.
        :param rating_matrix: the rating matrix.
        :return: the total value for each user.
        """
        pass

    @abstractmethod
    def total_relevant_users(self, rating_matrix):
        """
        Finds the total value of the property for the different users (limited to the set of users).
        :param rating_matrix: the rating matrix.
        :return: the average value for each user.
        """
        pass

    @abstractmethod
    def total_filter_users(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                           rating_filter=lambda x: x):
        """
        Finds the total value of the property for the different users (limited to a set of ratings).
        :param rating_matrix: the rating matrix.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: the total value for each user.
        """
        pass

    @abstractmethod
    def average_users(self, rating_matrix):
        """
        Finds the average value of the property for the different users.
        :param rating_matrix: the rating matrix.
        :return: the average value for each user.
        """
        pass

    @abstractmethod
    def average_relevant_users(self, rating_matrix):
        """
        Finds the average value of the property for the different users (limited to the set of users).
        :param rating_matrix: the rating matrix.
        :return: the average value for each user.
        """
        pass

    @abstractmethod
    def average_filter_users(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                             rating_filter=lambda x: x):
        """
        Finds the average value of the property for the different users (limited to a set of ratings).
        :param rating_matrix: the rating matrix.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: the average value for each user.
        """
        pass

    @abstractmethod
    def max_users(self, rating_matrix):
        """
        Finds the maximum value of the property for the different users.
        :param rating_matrix: the rating matrix.
        :return: the maximum value of the property for each user.
        """
        pass

    @abstractmethod
    def max_relevant_users(self, rating_matrix):
        """
        Finds the maximum value of the property to the different users (restricted to the set of relevant ratings)
        :param rating_matrix: the rating matrix.
        :return: the maximum value of the property for each user.
        """
        pass

    @abstractmethod
    def max_filter_users(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                         rating_filter=lambda x: x):
        """
        Finds the maximum value of the property for a selection of users, limited to some ratings.
        :param rating_matrix: the rating matrix.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the maximum value for each user.
        """
        pass

    @abstractmethod
    def min_users(self, rating_matrix):
        """
        Finds the minimum value of the property for the different users.
        :param rating_matrix: the rating matrix.
        :return: the minimum value of the property for each user.
        """
        pass

    @abstractmethod
    def min_relevant_users(self, rating_matrix):
        """
        Finds the minimum value of the property to the different users (restricted to the set of relevant ratings)
        :param rating_matrix: the rating matrix.
        :return: the minimum value of the property for each user.
        """
        pass

    @abstractmethod
    def min_filter_users(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                         rating_filter=lambda x: x):
        """
        Finds the minimum value of the property for a selection of users, limited to some ratings.
        :param rating_matrix: the rating matrix.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the minimum value for each user.
        """
        pass

    @abstractmethod
    def average_user(self, user_id, rating_matrix, item_filter=lambda x: x, rating_filter=lambda x: x):
        """
        Finds the average value of the property for a single user, limited to some ratings.
        :param user_id: the identifier of the user.
        :param rating_matrix: the rating matrix.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the average value for each user.
        """
        pass

    @abstractmethod
    def max_user(self, user_id, rating_matrix, item_filter=lambda x: x, rating_filter=lambda x: x):
        """
        Finds the maximum value of the property for a single user, limited to some ratings.
        :param user_id: the identifier of the user.
        :param rating_matrix: the rating matrix.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the maximum value for each user.
        """

    @abstractmethod
    def min_user(self, user_id, rating_matrix, item_filter=lambda x: x, rating_filter=lambda x: x):
        """
        Finds the minimum value of the property for a single user, limited to some ratings.
        :param user_id: the identifier of the user.
        :param rating_matrix: the rating matrix.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the minimum value for each user.
        """
        pass

    @abstractmethod
    def average_over_users(self, rating_matrix):
        """
        Averages the value of the property over the users.
        :param rating_matrix: the rating matrix.
        :return: the average value over the users.
        """
        pass

    @abstractmethod
    def average_over_users_relevant(self, rating_matrix):
        """
        Averages the value of the property over the users (limited to the set of relevant ratings)
        :param rating_matrix: the rating matrix.
        :return: the average value over the users.
        """
        pass

    @abstractmethod
    def average_over_users_filter(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                                  rating_filter=lambda x: x):
        """
        Averages the value of the property over a selection of users, limiting the selection of ratings used.
        :param rating_matrix: the rating matrix.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the minimum value for each user.
        """
        pass

    # Methods for analyzing individual items:

    @abstractmethod
    def total_items(self, rating_matrix):
        """
        Finds the total value of the property for the different items.
        :param rating_matrix: the rating matrix.
        :return: the total value for each item.
        """
        pass

    @abstractmethod
    def total_relevant_items(self, rating_matrix):
        """
        Finds the total value of the property for the different items (limited to the set of relevant ratings).
        :param rating_matrix: the rating matrix.
        :return: the average value for each user.
        """
        pass

    @abstractmethod
    def total_filter_items(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                           rating_filter=lambda x: x):
        """
        Finds the total value of the property for the different items (limited to a set of ratings).
        :param rating_matrix: the rating matrix.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: the total value for each items.
        """
        pass


    @abstractmethod
    def average_items(self, rating_matrix):
        """
        Finds the average value of the property for the different items.
        :param rating_matrix: the rating matrix.
        :return: the average value for each item.
        """
        pass

    @abstractmethod
    def average_relevant_items(self, rating_matrix):
        """
        Finds the average value of the property to the different items (restricted to the set of relevant ratings)
        :param rating_matrix: the rating matrix.
        :return: the average value of the property for each item.
        """
        pass

    @abstractmethod
    def average_filter_items(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                             rating_filter=lambda x: x):
        """
        Finds the average value of the property for a selection of items, limited to some ratings.
        :param rating_matrix: the rating matrix.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the average value for each item.
        """
        pass

    @abstractmethod
    def max_items(self, rating_matrix):
        """
        Finds the maximum value of the property for the different items.
        :param rating_matrix: the rating matrix.
        :return: the maximum value for each item.
        """
        pass

    @abstractmethod
    def max_relevant_items(self, rating_matrix):
        """
        Finds the maximum value of the property to the different items (restricted to the set of relevant ratings)
        :param rating_matrix: the rating matrix.
        :return: the maximum value of the property for each item.
        """
        pass

    @abstractmethod
    def max_filter_items(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                         rating_filter=lambda x: x):
        """
        Finds the maximum value of the property for a selection of items, limited to some ratings.
        :param rating_matrix: the rating matrix.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the maximum value for each item.
        """
        pass

    def min_items(self, rating_matrix):
        """
        Finds the minimum value of the property for the different items.
        :param rating_matrix: the rating matrix.
        :return: the minimum value for each item.
        """
        pass

    @abstractmethod
    def min_relevant_items(self, rating_matrix):
        """
        Finds the minimum value of the property to the different items (restricted to the set of relevant ratings)
        :param rating_matrix: the rating matrix.
        :return: the maximum value of the property for each item.
        """
        pass

    @abstractmethod
    def min_filter_items(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                         rating_filter=lambda x: x):
        """
        Finds the minimum value of the property for a selection of items, limited to some ratings.
        :param rating_matrix: the rating matrix.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the minimum value for each item.
        """
        pass

    @abstractmethod
    def average_item(self, item_id, rating_matrix, user_filter=lambda x: x, rating_filter=lambda x: x):
        """
        Finds the average value of the property for a single item, limited to some ratings.
        :param item_id: the identifier of the item.
        :param rating_matrix: the rating matrix.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the average value for each user.
        """
        pass

    @abstractmethod
    def max_item(self, item_id, rating_matrix, user_filter=lambda x: x, rating_filter=lambda x: x):
        """
        Finds the maximum value of the property for a single item, limited to some ratings.
        :param item_id: the identifier of the item.
        :param rating_matrix: the rating matrix.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the maximum value for each user.
        """
        pass

    @abstractmethod
    def min_item(self, item_id, rating_matrix, user_filter=lambda x: x, rating_filter=lambda x: x):
        """
        Finds the minimum value of the property for a single item, limited to some ratings.
        :param item_id: the identifier of the item.
        :param rating_matrix: the rating matrix.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the minimum value for each user.
        """
        pass

    @abstractmethod
    def average_over_items(self, rating_matrix):
        """
        Averages the value of the property over the items.
        :param rating_matrix: the rating matrix.
        :return: the average value over the items.
        """
        pass

    @abstractmethod
    def average_over_items_relevant(self, rating_matrix):
        """
        Averages the value of the property over the items (limited to the set of relevant ratings)
        :param rating_matrix: the rating matrix.
        :return: the average value over the items.
        """
        pass

    @abstractmethod
    def average_over_items_filter(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                                  rating_filter=lambda x: x):
        """
        Averages the value of the property over a selection of items, limiting the selection of ratings used.
        :param rating_matrix: the rating matrix.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the minimum value for each items.
        """
        pass
