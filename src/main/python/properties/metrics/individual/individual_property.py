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

import typing

from src.main.python.data import RatingMatrix


class IndividualProperty(ABC):
    """
    Abstract class implementing individual properties of users, items and ratings.
    """

    def __init__(self, rating_matrix: RatingMatrix):
        """
        Constructor.
        :param rating_matrix: the rating matrix over which the metric is computed.
        """
        self.rating_matrix = rating_matrix

    # Methods analyzing the whole rating matrix

    @abstractmethod
    def total(self,
              relevant: bool = False,
              user_filter: typing.Callable[[int], bool] = None,
              item_filter: typing.Callable[[int], bool] = None,
              rating_filter: typing.Callable[[int, int, float], bool] = None
              ) -> float:
        """
        Finds the total value of the property over all the relevant ratings.
        :param relevant: True if we only consider relevant ratings, false otherwise.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: the total value.
        """
        pass

    @abstractmethod
    def average(self,
                relevant: bool = False,
                user_filter: typing.Callable[[int], bool] = None,
                item_filter: typing.Callable[[int], bool] = None,
                rating_filter: typing.Callable[[int, int, float], bool] = None
                ) -> float:
        """
        Finds the average value of the property over all the relevant ratings.
        :param relevant: True if we only consider relevant ratings, false otherwise.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: the average value.
        """
        pass

    @abstractmethod
    def max(self,
            relevant: bool = False,
            user_filter: typing.Callable[[int], bool] = None,
            item_filter: typing.Callable[[int], bool] = None,
            rating_filter: typing.Callable[[int, int, float], bool] = None
            ) -> float:
        """
        Finds the maximum value of the property over all the relevant ratings.
        :param relevant: True if we only consider relevant ratings, false otherwise.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: the maximum value.
        """
        pass

    @abstractmethod
    def min(self,
            relevant: bool = False,
            user_filter: typing.Callable[[int], bool] = None,
            item_filter: typing.Callable[[int], bool] = None,
            rating_filter: typing.Callable[[int, int, float], bool] = None
            ) -> float:
        """
        Finds the minimum value of the property over all the relevant ratings.
        :param relevant: True if we only consider relevant ratings, false otherwise.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: the minimum value.
        """
        pass

    # Methods for analyzing individual users:

    @abstractmethod
    def total_users(self,
                    relevant: bool = False,
                    user_filter: typing.Callable[[int], bool] = None,
                    item_filter: typing.Callable[[int], bool] = None,
                    rating_filter: typing.Callable[[int, int, float], bool] = None
                    ) -> typing.Dict[int, float]:
        """
        Finds the total value of the property for the different users.
        :param relevant: True if we only consider relevant ratings, false otherwise.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: a map containing the total value of the property for each selected user.
        """
        pass

    @abstractmethod
    def average_users(self,
                      relevant: bool = False,
                      user_filter: typing.Callable[[int], bool] = None,
                      item_filter: typing.Callable[[int], bool] = None,
                      rating_filter: typing.Callable[[int, int, float], bool] = None
                      ) -> typing.Dict[int, float]:
        """
        Finds the average value of the property for the different users.
        :param relevant: True if we only consider relevant ratings, false otherwise.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: a map containing the average value of the property for each selected user.
        """
        pass

    @abstractmethod
    def max_users(self,
                  relevant: bool = False,
                  user_filter: typing.Callable[[int], bool] = None,
                  item_filter: typing.Callable[[int], bool] = None,
                  rating_filter: typing.Callable[[int, int, float], bool] = None
                  ) -> typing.Dict[int, float]:
        """
        Finds the maximum value of the property for the different users.
        :param relevant: True if we only consider relevant ratings, false otherwise.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: a map containing the maximum value of the property for each selected user.
        """
        pass

    @abstractmethod
    def min_users(self,
                  relevant: bool = False,
                  user_filter: typing.Callable[[int], bool] = None,
                  item_filter: typing.Callable[[int], bool] = None,
                  rating_filter: typing.Callable[[int, int, float], bool] = None
                  ) -> typing.Dict[int, float]:
        """
        Finds the minimum value of the property for the different users.
        :param relevant: True if we only consider relevant ratings, false otherwise.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: a map containing the minimum value of the property for each selected user.
        """
        pass

    @abstractmethod
    def total_user(self,
                   user: int,
                   relevant: bool = False,
                   item_filter: typing.Callable[[int], bool] = None,
                   rating_filter: typing.Callable[[int, int, float], bool] = None
                   ) -> float:
        """
        Finds the total value of the property for a single user, limited to some ratings.
        :param user: the identifier of the user.
        :param relevant: True if we only consider relevant ratings, false otherwise.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the total value for the user.
        """
        pass

    @abstractmethod
    def average_user(self,
                     user: int,
                     relevant: bool = False,
                     item_filter: typing.Callable[[int], bool] = None,
                     rating_filter: typing.Callable[[int, int, float], bool] = None
                     ) -> float:
        """
        Finds the average value of the property for a single user, limited to some ratings.
        :param user: the identifier of the user.
        :param relevant: True if we only consider relevant ratings, false otherwise.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the average value for the user.
        """
        pass

    @abstractmethod
    def max_user(self,
                 user: int,
                 relevant: bool = False,
                 item_filter: typing.Callable[[int], bool] = None,
                 rating_filter: typing.Callable[[int, int, float], bool] = None
                 ) -> float:
        """
        Finds the maximum value of the property for a single user, limited to some ratings.
        :param user: the identifier of the user.
        :param relevant: True if we only consider relevant ratings, false otherwise.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the maximum value for the user.
        """

    @abstractmethod
    def min_user(self,
                 user: int,
                 relevant: bool = False,
                 item_filter: typing.Callable[[int], bool] = None,
                 rating_filter: typing.Callable[[int, int, float], bool] = None
                 ) -> float:
        """
        Finds the minimum value of the property for a single user, limited to some ratings.
        :param user: the identifier of the user.
        :param relevant: True if we only consider relevant ratings, false otherwise.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the minimum value for the user.
        """
        pass

    @abstractmethod
    def average_over_users(self,
                           relevant: bool = False,
                           user_filter: typing.Callable[[int], bool] = None,
                           item_filter: typing.Callable[[int], bool] = None,
                           rating_filter: typing.Callable[[int, int, float], bool] = None
                           ) -> float:
        """
        Averages the value of the property over the users.
        :param relevant: True if we only consider relevant ratings, False otherwise.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: the average value over the users.
        """
        pass

    @abstractmethod
    def max_over_users(self,
                       relevant: bool = False,
                       user_filter: typing.Callable[[int], bool] = None,
                       item_filter: typing.Callable[[int], bool] = None,
                       rating_filter: typing.Callable[[int, int, float], bool] = None
                       ) -> float:
        """
        Obtains the maximum value of the property over the users.
        :param relevant: True if we only consider relevant ratings, False otherwise.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: the maximum value over the users.
        """
        pass

    @abstractmethod
    def min_over_users(self,
                       relevant: bool = False,
                       user_filter: typing.Callable[[int], bool] = None,
                       item_filter: typing.Callable[[int], bool] = None,
                       rating_filter: typing.Callable[[int, int, float], bool] = None
                       ) -> float:
        """
        Obtains the minimum value of the property over the users.
        :param relevant: True if we only consider relevant ratings, False otherwise.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: the minimum value over the users.
        """
        pass

    # Methods for analyzing individual items:

    @abstractmethod
    def total_items(self,
                    relevant: bool = False,
                    user_filter: typing.Callable[[int], bool] = None,
                    item_filter: typing.Callable[[int], bool] = None,
                    rating_filter: typing.Callable[[int, int, float], bool] = None
                    ) -> typing.Dict[int, float]:
        """
        Finds the total value of the property for the different items.
        :param relevant: True if we only consider relevant ratings, false otherwise.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: a map containing the total value of the property for each selected item.
        """
        pass

    @abstractmethod
    def average_items(self,
                      relevant: bool = False,
                      user_filter: typing.Callable[[int], bool] = None,
                      item_filter: typing.Callable[[int], bool] = None,
                      rating_filter: typing.Callable[[int, int, float], bool] = None
                      ) -> typing.Dict[int, float]:
        """
        Finds the average value of the property for the different items.
        :param relevant: True if we only consider relevant ratings, false otherwise.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: a map containing the average value of the property for each selected item.
        """
        pass

    @abstractmethod
    def max_items(self,
                  relevant: bool = False,
                  user_filter: typing.Callable[[int], bool] = None,
                  item_filter: typing.Callable[[int], bool] = None,
                  rating_filter: typing.Callable[[int, int, float], bool] = None
                  ) -> typing.Dict[int, float]:
        """
        Finds the maximum value of the property for the different items.
        :param relevant: True if we only consider relevant ratings, false otherwise.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: a map containing the maximum value of the property for each selected item.
        """
        pass

    @abstractmethod
    def min_items(self,
                  relevant: bool = False,
                  user_filter: typing.Callable[[int], bool] = None,
                  item_filter: typing.Callable[[int], bool] = None,
                  rating_filter: typing.Callable[[int, int, float], bool] = None
                  ) -> typing.Dict[int, float]:
        """
        Finds the minimum value of the property for the different items.
        :param relevant: True if we only consider relevant ratings, false otherwise.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: a map containing the minimum value of the property for each selected item.
        """
        pass

    @abstractmethod
    def total_item(self,
                   item: int,
                   relevant: bool = False,
                   user_filter: typing.Callable[[int], bool] = None,
                   rating_filter: typing.Callable[[int, int, float], bool] = None
                   ) -> float:
        """
        Finds the total value of the property for a single item, limited to some ratings.
        :param item: the identifier of the item.
        :param relevant: True if we only consider relevant ratings, false otherwise.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the total value for the item.
        """
        pass

    @abstractmethod
    def average_item(self,
                     item: int,
                     relevant: bool = False,
                     user_filter: typing.Callable[[int], bool] = None,
                     rating_filter: typing.Callable[[int, int, float], bool] = None
                     ) -> float:
        """
        Finds the average value of the property for a single item, limited to some ratings.
        :param item: the identifier of the item.
        :param relevant: True if we only consider relevant ratings, false otherwise.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the average value for the item.
        """
        pass

    @abstractmethod
    def max_item(self,
                 item: int,
                 relevant: bool = False,
                 user_filter: typing.Callable[[int], bool] = None,
                 rating_filter: typing.Callable[[int, int, float], bool] = None
                 ) -> float:
        """
        Finds the maximum value of the property for a single item, limited to some ratings.
        :param item: the identifier of the item.
        :param relevant: True if we only consider relevant ratings, false otherwise.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the maximum value for the item.
        """

    @abstractmethod
    def min_item(self,
                 item: int,
                 relevant: bool = False,
                 user_filter: typing.Callable[[int], bool] = None,
                 rating_filter: typing.Callable[[int, int, float], bool] = None
                 ) -> float:
        """
        Finds the minimum value of the property for a single item, limited to some ratings.
        :param item: the identifier of the item.
        :param relevant: True if we only consider relevant ratings, false otherwise.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        :return: the minimum value for the item.
        """

    @abstractmethod
    def average_over_items(self,
                           relevant: bool = False,
                           user_filter: typing.Callable[[int], bool] = None,
                           item_filter: typing.Callable[[int], bool] = None,
                           rating_filter: typing.Callable[[int, int, float], bool] = None
                           ) -> float:
        """
        Averages the value of the property over the items.
        :param relevant: True if we only consider relevant ratings, False otherwise.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: the average value over the items.
        """
        pass

    @abstractmethod
    def max_over_items(self,
                       relevant: bool = False,
                       user_filter: typing.Callable[[int], bool] = None,
                       item_filter: typing.Callable[[int], bool] = None,
                       rating_filter: typing.Callable[[int, int, float], bool] = None
                       ) -> float:
        """
        Obtains the maximum value of the property over the items.
        :param relevant: True if we only consider relevant ratings, False otherwise.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: the maximum value over the items.
        """
        pass

    @abstractmethod
    def min_over_items(self,
                       relevant: bool = False,
                       user_filter: typing.Callable[[int], bool] = None,
                       item_filter: typing.Callable[[int], bool] = None,
                       rating_filter: typing.Callable[[int, int, float], bool] = None
                       ) -> float:
        """
        Obtains the minimum value of the property over the items.
        :param relevant: True if we only consider relevant ratings, False otherwise.
        :param user_filter: (OPTIONAL) filter for the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for the ratings. By default, no filter is applied.
        :return: the minimum value over the items.
        """
        pass
