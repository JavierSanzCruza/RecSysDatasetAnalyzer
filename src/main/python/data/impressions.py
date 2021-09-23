"""
Representation of the impressions included in a dataset.
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

import typing

from .adding_return import AddingReturn
from .filters import UserFilter, ItemFilter, RatingFilter, ImpressionsFilter


class Impressions:
    """
    Class that represents the impressions, i.e. the set of items which have been shown to a user.
    """

    def __init__(self):
        """
        Initializes the impressions in the system.
        """
        self.user_impressions = dict()
        self.item_impressions = dict()
        self.num_impressions = 0

    def add_user(self, user_id):
        """
        Adds a new user to the rating matrix.
        :param user_id: the identifier of the user.
        :return: true if we add the user, false otherwise.
        """
        if self.user_impressions.keys().__contains__(user_id):
            return False
        else:
            self.user_impressions[user_id] = set()
            return True

    def add_item(self, item_id):
        """
        Adds a new item to the rating matrix
        :param item_id: the identifier of the item.
        :return: true if we add the item, false otherwise.
        """
        if self.item_impressions.keys().__contains__(item_id):
            return False
        else:
            self.item_impressions[item_id] = set()
            return True

    def add_impression(self, user_id, item_id):
        """
        Adds a new impression
        :param user_id: the identifier of the user.
        :param item_id: the identifier of the item.
        :return: AddingReturn.ADDED if the impression is new, AddingReturn.NONE if it already existed,
                 AddingReturn.ERROR if something failed.
        """

        if self.user_impressions.keys().__contains__(user_id) and self.item_impressions.keys().__contains__(item_id):
            if self.user_impressions[user_id].__contains__(item_id):
                return AddingReturn.NONE
            else:
                self.user_impressions[user_id].add(item_id)
                self.item_impressions[item_id].add(user_id)
                self.num_impressions += 1
                return AddingReturn.ADDED
        return AddingReturn.ERROR

    def get_users(self):
        """
        Obtains the set of users.
        :return: the set of users.
        """
        return (x for x in self.user_impressions.keys())

    def get_items(self):
        """
        Obtains the set of items.
        :return: the set of items.
        """
        return (x for x in self.item_impressions.keys())

    def get_user_impressions(self, user_id):
        """
        Obtains the set of impressions for a user.
        :param user_id: the identifier of the user.
        :return: an iterator of the impressions for the user.
        """
        return (x for x in self.user_impressions.get(user_id, set()))

    def get_item_impressions(self, item_id):
        """
        Obtains the set of users including an item in their impressions.
        :param item_id: the identifier of the item.
        :return: an iterator of the impressed users.
        """
        return (x for x in self.item_impressions.get(item_id, set()))

    def get_num_impressions(self):
        """
        Obtains the number of impressions.
        :return: the number of impressions.
        """
        return self.num_impressions

    def get_num_users(self):
        """
        Obtains the number of users.
        :return: the number of users.
        """
        return len(self.user_impressions.keys())

    def get_num_items(self):
        """
        Obtains the number of items.
        :return: the number of items.
        """
        return len(self.item_impressions.keys())

    def get_num_user_impressions(self, user):
        """
        Obtains the number of impressions for a user.
        :param user: the identifier of the user.
        :return: the number of impressions for the user.
        """
        return len(self.user_impressions.get(user, []))

    def get_num_item_impressions(self, item):
        """
        Obtains the number of impressions in which an item appears.
        :param item: the item identifier.
        :return: the number of impressions in which the item appears.
        """
        return len(self.item_impressions.get(item, []))

    def filter(self,
               user_filter: typing.Callable[[int], bool] = None,
               item_filter: typing.Callable[[int], bool] = None,
               impressions_filter: typing.Callable[[int, int], bool] = None
               ):
        """
        Obtains a proxy rating matrix containing only a fraction of the ratings.
        :param user_filter: (OPTIONAL) a filter for selecting the users to keep. By default, no filter is applied.
        :param item_filter: (OPTIONAL) a filter for selecting the items to keep. By default, no filter is applied.
        :param impressions_filter: (OPTIONAL) a filter for selecting the impressions to keep.
                                    By default, no filter is applied.
        :returns: a rating matrix containing the selected ratings.
        """

        if user_filter is None:
            user_filter = UserFilter.default()
        if item_filter is None:
            item_filter = ItemFilter.default()
        if impressions_filter is None:
            impressions_filter = ImpressionsFilter.default()

        aux_matrix = Impressions()

        for item in filter(item_filter, self.get_items()):
            aux_matrix.add_item(item)
        for user in filter(user_filter, self.get_users()):
            aux_matrix.add_user(user)
            for item in self.get_user_impressions(user):
                if item_filter(item) and impressions_filter(user, item):
                    aux_matrix.add_impression(user, item)

        return aux_matrix
