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


from src.main.python.properties.metrics.individual.individual_property import IndividualProperty

import math


class Rating(IndividualProperty):

    def average(self, rating_matrix):
        summation = 0
        for user in rating_matrix.get_users():
            for item, rating in rating_matrix.get_user_ratings(user):
                summation += rating
        return float(summation) / float(rating_matrix.get_num_ratings())

    def average_relevant(self, rating_matrix):
        summation = 0
        for user in rating_matrix.get_users():
            for item, rating in rating_matrix.get_user_ratings(user):
                summation += rating
        return float(summation) / float(rating_matrix.get_num_rel_ratings())

    def average_filter(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                       rating_filter=lambda x: x):
        summation = 0
        count = 0
        for user in filter(user_filter, rating_matrix.get_users):
            for item, rating in rating_matrix.get_user_ratings(user):
                if item_filter(item) and rating_filter((user, item, rating)):
                    summation += rating
                    count += 1
        return float(summation) / float(count)

    def max(self, rating_matrix):
        maximum = -math.inf
        for user in rating_matrix.get_users():
            for item, rating in rating_matrix.get_user_ratings(user):
                if rating > maximum:
                    maximum = rating
        return maximum

    def max_relevant(self, rating_matrix):
        maximum = -math.inf
        for user in rating_matrix.get_users():
            for item, rating in rating_matrix.get_user_rel_ratings(user):
                if rating > maximum:
                    maximum = rating
        return maximum

    def max_filter(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x, rating_filter=lambda x: x):
        maximum = -math.inf
        for user in filter(user_filter, rating_matrix.get_users):
            for item, rating in rating_matrix.get_user_ratings(user):
                if item_filter(item) and rating_filter((user, item, rating)):
                    if rating > maximum:
                        maximum = rating
        return maximum

    def min(self, rating_matrix):
        minimum = math.inf
        for user in rating_matrix.get_users():
            for item, rating in rating_matrix.get_user_ratings(user):
                if rating < minimum:
                    minimum = rating
        return minimum

    def min_relevant(self, rating_matrix):
        minimum = -math.inf
        for user in rating_matrix.get_users():
            for item, rating in rating_matrix.get_user_rel_ratings(user):
                if rating < minimum:
                    minimum = rating
        return minimum

    def min_filter(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x, rating_filter=lambda x: x):
        minimum = -math.inf
        for user in filter(user_filter, rating_matrix.get_users()):
            for item, rating in rating_matrix.get_user_ratings(user):
                if item_filter(item) and rating_filter((user, item, rating)):
                    if rating < minimum:
                        minimum = rating
        return minimum

    @staticmethod
    def average_list(values):
        """
        Averages the values of a list.
        :param values: the list
        :return: the average value of the list
        """

        aux = 0.0
        count = 0.0

        for item, rating in values:
            aux += rating
            count += 1.0
        return aux / count if count > 0 else 0

    @staticmethod
    def max_list(values):
        """
        Averages the values of a list.
        :param values: the list
        :return: the average value of the list
        """
        return max(map(lambda x: x[1], values))

    @staticmethod
    def min_list(values):
        """
        Averages the values of a list.
        :param values: the list
        :return: the average value of the list
        """
        return min(map(lambda x: x[1], values))

    def average_users(self, rating_matrix):
        value = dict()
        for user in rating_matrix.get_users():
            value[user] = Rating.average_list(rating_matrix.get_user_ratings(user))
        return value

    def average_relevant_users(self, rating_matrix):
        value = dict()
        for user in rating_matrix.get_users():
            value[user] = Rating.average_list(rating_matrix.get_user_rel_ratings(user))
        return value

    def average_filter_users(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                             rating_filter=lambda x: x):
        value = dict()
        for user in filter(user_filter, rating_matrix.get_users()):
            value[user] = Rating.average_list(
                filter(lambda x: item_filter(x[0]) and rating_filter((user, x[0], x[1])),
                       rating_matrix.get_user_ratings(user))
            )
        return value

    def max_users(self, rating_matrix):
        value = dict()
        for user in rating_matrix.get_users():
            value[user] = Rating.max_list(rating_matrix.get_user_ratings(user))
        return value

    def max_relevant_users(self, rating_matrix):
        value = dict()
        for user in rating_matrix.get_users():
            value[user] = Rating.max_list(rating_matrix.get_user_rel_ratings(user))
        return value

    def max_filter_users(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                         rating_filter=lambda x: x):
        value = dict()
        for user in filter(user_filter, rating_matrix.get_users()):
            value[user] = Rating.max_list(
                filter(lambda x: item_filter(x[0]) and rating_filter((user, x[0], x[1])),
                       rating_matrix.get_user_ratings(user))
            )
        return value

    def min_users(self, rating_matrix):
        value = dict()
        for user in rating_matrix.get_users():
            value[user] = Rating.min_list(rating_matrix.get_user_ratings(user))
        return value

    def min_relevant_users(self, rating_matrix):
        value = dict()
        for user in rating_matrix.get_users():
            value[user] = Rating.min_list(rating_matrix.get_user_rel_ratings(user))
        return value

    def min_filter_users(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                         rating_filter=lambda x: x):
        value = dict()
        for user in filter(user_filter, rating_matrix.get_users()):
            value[user] = Rating.min_list(
                filter(lambda x: item_filter(x[0]) and rating_filter((user, x[0], x[1])),
                       rating_matrix.get_user_ratings(user))
            )
        return value

    def average_items(self, rating_matrix):
        value = dict()
        for item in rating_matrix.get_items():
            value[item] = Rating.average_list(rating_matrix.get_item_ratings(item))
        return value

    def average_relevant_items(self, rating_matrix):
        value = dict()
        for item in rating_matrix.get_items():
            value[item] = Rating.average_list(rating_matrix.get_item_rel_ratings(item))
        return value

    def average_filter_items(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                             rating_filter=lambda x: x):
        value = dict()
        for item in filter(item_filter, rating_matrix.get_items()):
            value[item] = Rating.average_list(
                filter(lambda x: item_filter(x[0]) and rating_filter((item, x[0], x[1])),
                       rating_matrix.get_item_ratings(item))
            )
        return value

    def max_items(self, rating_matrix):
        value = dict()
        for item in rating_matrix.get_items():
            value[item] = Rating.max_list(rating_matrix.get_item_ratings(item))
        return value

    def max_relevant_items(self, rating_matrix):
        value = dict()
        for item in rating_matrix.get_items():
            value[item] = Rating.max_list(rating_matrix.get_item_rel_ratings(item))
        return value

    def max_filter_items(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                         rating_filter=lambda x: x):
        value = dict()
        for item in filter(item_filter, rating_matrix.get_items()):
            value[item] = Rating.max_list(
                filter(lambda x: item_filter(x[0]) and rating_filter((item, x[0], x[1])),
                       rating_matrix.get_item_ratings(item))
            )
        return value

    def min_items(self, rating_matrix):
        value = dict()
        for item in rating_matrix.get_items():
            value[item] = Rating.min_list(rating_matrix.get_item_ratings(item))
        return value

    def min_relevant_items(self, rating_matrix):
        value = dict()
        for item in rating_matrix.get_items():
            value[item] = Rating.min_list(rating_matrix.get_item_rel_ratings(item))
        return value

    def min_filter_items(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                         rating_filter=lambda x: x):
        value = dict()
        for item in filter(item_filter, rating_matrix.get_items()):
            value[item] = Rating.min_list(
                filter(lambda x: item_filter(x[0]) and rating_filter((item, x[0], x[1])),
                       rating_matrix.get_item_ratings(item))
            )
        return value
