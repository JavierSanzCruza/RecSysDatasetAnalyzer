"""
Representation of the replayer dataset given by Yahoo.
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

from src.main.python.data import RatingMatrix, Impressions
from src.main.python.properties.distributions.temporal_distribution import TemporalDistribution

from os import listdir
from os.path import isfile, join


class ReplayerDataset:
    """
    Representation of the replayer dataset given by Yahoo (Yahoo R6B dataset)
    """

    def __init__(self,
                 user_2_item: RatingMatrix,
                 user_2_item_ts: TemporalDistribution,
                 impressions: Impressions):
        """
        Initialization of the dataset.
        :param user_2_item: the user-item interaction matrix.
        :param user_2_item_ts: the temporal distribution of the user-item interactions.
        :param impressions: the items shown to the users in the dataset.
        """
        self.user_2_item = user_2_item
        self.user_2_item_ts = user_2_item_ts
        self.impressions = impressions

    @staticmethod
    def load_yahoo_r6b(interactions_folder: str,
                       min_interactions_per_user: int = 0):
        """
        Loads the Yahoo! R6B dataset.
        :param interactions_folder: a directory containing the different files.
        :return: the fully loaded dataset.
        """
        user_2_item = RatingMatrix(0.0, True, True)
        user_2_item_ts = TemporalDistribution()
        impr = Impressions()
        items = dict()
        users = dict()

        user_count = dict()

        files = [f for f in listdir(interactions_folder) if
                 isfile(join(interactions_folder, f)) and not f == "README.txt"]

        for file in files:
            f = open(join(interactions_folder, file), mode='r')
            for record in f:
                splitted = record.split(" ")
                timestamp = int(splitted[0])
                item = splitted[1]
                rating = float(splitted[2])

                item_list = list()
                is_current_user = False
                is_empty_user = True
                user = list()
                for i in range(0, 135):
                    user.append('0')
                for i in range(3, len(splitted)):
                    if splitted[i] == "|user":
                        is_current_user = True
                    elif splitted[i].startswith('|'):
                        is_current_user = False
                        item_id = splitted[i][1:len(splitted[i]) - 1]
                        item_list.append(item_id)
                    elif is_current_user:
                        idx = int(splitted[i])
                        if idx > 1:
                            is_empty_user = False
                            user[idx - 2] = '1'

                # If we can identify the user from its features:
                if not is_empty_user:
                    # First, we store the user.
                    user_str = ''.join(user)

                    if not users.__contains__(user_str):
                        user_id = len(users)
                        users[user_str] = user_id
                        user_2_item.add_user(user_id)
                        impr.add_user(user_id)
                        user_count[user_id] = 1
                    else:
                        user_id = users[user_str]
                        user_count[user_id] += 1

                    # Then, we store the item.
                    if not items.__contains__(item):
                        item_id = len(items)
                        items[item] = item_id
                        user_2_item.add_item(item_id)
                        impr.add_item(item_id)
                    else:
                        item_id = items[item]

                    user_2_item.rate(user_id, item_id, rating)
                    user_2_item_ts.add_timepoint(user_id, item_id, timestamp)

                    # Now, we add the impressions:
                    for item_str in item_list:
                        if not items.__contains__(item_str):
                            item_id = len(items)
                            items[item_str] = item_id
                            user_2_item.add_item(item_id)
                            impr.add_item(item_id)
                        else:
                            item_id = items[item_str]
                        impr.add_impression(user_id, item_id)

        # Now, we check whether we want to limit the dataset to those users with, at least, X impressions,
        # and filter the dataset appropriately.
        if min_interactions_per_user <= 0:
            return ReplayerDataset(user_2_item, user_2_item_ts, impr)
        else:
            aux_dataset = user_2_item.filter(user_filter=lambda u: user_count[u] >= min_interactions_per_user)
            aux_dataset_ts = user_2_item_ts.filter(user_filter=lambda u: user_count[u] >= min_interactions_per_user)
            aux_impr = impr.filter(user_filter=lambda u: user_count[u] >= min_interactions_per_user)
            return ReplayerDataset(aux_dataset, aux_dataset_ts, aux_impr)

    def num_users(self):
        """
        Obtains the number of users in the dataset.
        :return: the number of users in the dataset.
        """
        return self.user_2_item.get_num_users()

    def num_items(self):
        """
        Obtains the number of items in the dataset.
        :return: the number of items in the dataset.
        """
        return self.user_2_item.get_num_items()

    def get_user_2_item_interactions(self):
        """
        Obtains the user-item interactions in the dataset.
        :return: the user-item rating matrix.
        """
        return self.user_2_item

    def get_impressions(self):
        """
        Obtains the user impressions in the dataset.
        :return: the user impressions in the dataset.
        """
        return self.impressions

    def get_user_2_item_interactions_temporal_distribution(self):
        """
        Obtains the temporal distribution of the user-item interactions.
        :return: the temporal distribution of the user-item interactions.
        """
        return self.user_2_item_ts
