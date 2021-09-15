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

from functools import reduce

from src.main.python.properties.metrics.individual.individual_property import IndividualProperty

import math


class Interaction(IndividualProperty):

    def total(self, rating_matrix):
        return sum(map(lambda user: len(rating_matrix.get_user_ratings(user)), rating_matrix.get_users()))

    def total_relevant(self, rating_matrix):
        return sum(map(lambda user: len(rating_matrix.get_user_rel_ratings(user)), rating_matrix.get_users()))

    def total_filter(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x, rating_filter=lambda x: x):
        summation = 0
        for user in filter(user_filter, rating_matrix.get_users):
            for item, rating in rating_matrix.get_user_ratings(user):
                if item_filter(item) and rating_filter((user, item, rating)):
                    summation += 1
        return float(summation)

    def average(self, rating_matrix):
        return 1.0 if rating_matrix.get_num_ratings() > 0 else math.nan

    def average_relevant(self, rating_matrix):
        return 1.0 if rating_matrix.get_num_rel_ratings() > 0 else math.nan

    def average_filter(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                       rating_filter=lambda x: x):
        for user in filter(user_filter, rating_matrix.get_users):
            for item, rating in rating_matrix.get_user_ratings(user):
                if item_filter(item) and rating_filter((user, item, rating)):
                    return 1.0
        return math.nan

    def max(self, rating_matrix):
        return self.average(rating_matrix)

    def max_relevant(self, rating_matrix):
        return self.average_relevant(rating_matrix)

    def max_filter(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x, rating_filter=lambda x: x):
        return self.average_filter(rating_matrix, user_filter=user_filter, item_filter=item_filter,
                                   rating_filter=rating_filter)

    def min(self, rating_matrix):
        return self.average(rating_matrix)

    def min_relevant(self, rating_matrix):
        return self.average_relevant(rating_matrix)

    def min_filter(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x, rating_filter=lambda x: x):
        return self.average_filter(rating_matrix, user_filter=user_filter, item_filter=item_filter,
                                   rating_filter=rating_filter)

    def total_users(self, rating_matrix):
        value = dict()
        for user in rating_matrix.get_users():
            value[user] = sum(map(lambda x: 1, rating_matrix.get_user_ratings(user)))
        return value

    def total_relevant_users(self, rating_matrix):
        value = dict()
        for user in rating_matrix.get_users():
            value[user] = sum(map(lambda x: 1, rating_matrix.get_user_rel_ratings(user)))
        return value

    def total_filter_users(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                           rating_filter=lambda x: x):
        value = dict()
        for user in filter(user_filter, rating_matrix.get_users()):
            value[user] = reduce(lambda x, y: x + 1,
                                 filter(lambda x: item_filter(x[0]) and rating_filter((user, x[0], x[1])),
                                        rating_matrix.get_user_ratings(user))
                                 )
        return value

    def average_users(self, rating_matrix):
        value = dict()
        for user in rating_matrix.get_users():
            value[user] = 1.0 if rating_matrix.get_num_user_ratings(user) > 0 else 0.0
        return value

    def average_relevant_users(self, rating_matrix):
        value = dict()
        for user in rating_matrix.get_users():
            value[user] = 1.0 if rating_matrix.get_num_user_rel_ratings(user) > 0 else 0.0
        return value

    def average_filter_users(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                             rating_filter=lambda x: x):
        value = dict()
        for user in filter(user_filter, rating_matrix.get_users()):
            for item, rating in rating_matrix.get_user_ratings(user):
                if item_filter(item) and rating_filter((user, item, rating)):
                    value[user] = 1.0
                    break
            if not value.__contains__(user):
                value[user] = 0.0
        return value

    def max_users(self, rating_matrix):
        return self.average_users(rating_matrix)

    def max_relevant_users(self, rating_matrix):
        return self.average_relevant_users(rating_matrix)

    def max_filter_users(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                         rating_filter=lambda x: x):
        return self.average_filter_users(rating_matrix, user_filter=user_filter, item_filter=item_filter,
                                         rating_filter=rating_filter)

    def min_users(self, rating_matrix):
        return self.average_users(rating_matrix)

    def min_relevant_users(self, rating_matrix):
        return self.average_relevant_users(rating_matrix)

    def min_filter_users(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                         rating_filter=lambda x: x):
        return self.average_filter_users(rating_matrix, user_filter=user_filter, item_filter=item_filter,
                                         rating_filter=rating_filter)

    def average_user(self, user_id, rating_matrix, item_filter=lambda x: x, rating_filter=lambda x: x):
        if not rating_matrix.get_users().__contains__(user_id):
            return math.nan
        else:
            for item, rating in rating_matrix.get_user_ratings(user_id):
                if item_filter(item) and rating_filter((user_id, item, rating)):
                    return 1.0
            return 0.0

    def max_user(self, user_id, rating_matrix, item_filter=lambda x: x, rating_filter=lambda x: x):
        return self.average_user(user_id, rating_matrix, item_filter=item_filter, rating_filter=rating_filter)

    def min_user(self, user_id, rating_matrix, item_filter=lambda x: x, rating_filter=lambda x: x):
        return self.average_user(user_id, rating_matrix, item_filter=item_filter, rating_filter=rating_filter)

    def average_over_users(self, rating_matrix):
        return float(rating_matrix.get_num_ratings()) / float(rating_matrix.get_num_users())

    def average_over_users_relevant(self, rating_matrix):
        return float(rating_matrix.get_num_rel_ratings()) / float(rating_matrix.get_num_users())

    def average_over_users_filter(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                                  rating_filter=lambda x: x):
        summation = 0
        count = 0
        for user in filter(user_filter, rating_matrix.get_users):
            for item, rating in rating_matrix.get_user_ratings(user):
                if item_filter(item) and rating_filter((user, item, rating)):
                    summation += 1
            count += 1
        return float(summation) / float(count)

    def total_items(self, rating_matrix):
        value = dict()
        for item in rating_matrix.get_items():
            value[item] = sum(map(lambda x: 1, rating_matrix.get_item_ratings(item)))
        return value

    def total_relevant_items(self, rating_matrix):
        value = dict()
        for item in rating_matrix.get_items():
            value[item] = sum(map(lambda x: 1, rating_matrix.get_item_rel_ratings(item)))
        return value

    def total_filter_items(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                           rating_filter=lambda x: x):
        value = dict()
        for item in filter(item_filter, rating_matrix.get_items()):
            value[item] = reduce(lambda x, y: x + 1,
                                 filter(lambda user, rating: user_filter(user) and rating_filter((user, item, rating)),
                                        rating_matrix.get_item_ratings(item))
                                 )
        return value

    def average_items(self, rating_matrix):
        value = dict()
        for item in rating_matrix.get_items():
            value[item] = 1.0 if rating_matrix.get_num_item_ratings(item) > 0 else 0.0
        return value

    def average_relevant_items(self, rating_matrix):
        value = dict()
        for item in rating_matrix.get_items():
            value[item] = 1.0 if rating_matrix.get_num_item_rel_ratings(item) > 0 else 0.0
        return value

    def average_filter_items(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                             rating_filter=lambda x: x):
        value = dict()
        for item in filter(item_filter, rating_matrix.get_items()):
            for user, rating in rating_matrix.get_item_ratings(item):
                if user_filter(user) and rating_filter((user, item, rating)):
                    value[item] = 1.0
                    break
            if not value.__contains__(item):
                value[item] = 0.0
        return value

    def max_items(self, rating_matrix):
        return self.average_items(rating_matrix)

    def max_relevant_items(self, rating_matrix):
        return self.average_relevant_items(rating_matrix)

    def max_filter_items(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                         rating_filter=lambda x: x):
        return self.average_filter_items(self, rating_matrix, user_filter=user_filter, item_filter=item_filter,
                                         rating_filter=rating_filter)

    def min_items(self, rating_matrix):
        return self.average_items(rating_matrix)

    def min_relevant_items(self, rating_matrix):
        return self.average_relevant_items(rating_matrix)

    def min_filter_items(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                         rating_filter=lambda x: x):
        return self.average_filter_items(self, rating_matrix, user_filter=user_filter, item_filter=item_filter,
                                         rating_filter=rating_filter)

    def average_item(self, item_id, rating_matrix, user_filter=lambda x: x, rating_filter=lambda x: x):
        if not rating_matrix.get_items().__contains__(item_id):
            return math.nan
        else:
            for user, rating in rating_matrix.get_item_ratings(item_id):
                if user_filter(user) and rating_filter((user, item_id, rating)):
                    return 1.0
            return 0.0

    def max_item(self, item_id, rating_matrix, user_filter=lambda x: x, rating_filter=lambda x: x):
        return self.average_item(item_id, rating_matrix, user_filter=user_filter, rating_filter=rating_filter)

    def min_item(self, item_id, rating_matrix, user_filter=lambda x: x, rating_filter=lambda x: x):
        return self.average_item(item_id, rating_matrix, user_filter=user_filter, rating_filter=rating_filter)

    def average_over_items(self, rating_matrix):
        return float(rating_matrix.get_num_ratings()) / float(rating_matrix.get_num_items())

    def average_over_items_relevant(self, rating_matrix):
        return float(rating_matrix.get_num_rel_ratings()) / float(rating_matrix.get_num_users())

    def average_over_items_filter(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x,
                                  rating_filter=lambda x: x):
        summation = 0
        count = 0
        for item in filter(item_filter, rating_matrix.get_items):
            for user, rating in rating_matrix.get_item_ratings(item):
                if user_filter(user) and rating_filter((user, item, rating)):
                    summation += 1
            count += 1
        return float(summation) / float(count)
