"""
Representation of the ContentWise dataset.
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

from src.main.python.data import RatingMatrix, Impressions, AddingReturn
from src.main.python.datasets.contentwise.item import ContentWiseItem
from src.main.python.datasets.contentwise.item_type import ContentWiseItemType
from src.main.python.datasets.contentwise.series import ContentWiseSeries
from src.main.python.properties.distributions.temporal_distribution import TemporalDistribution
import typing

import csv


class ContentWiseDataset:
    """
    Representation of the ContentWise dataset.

    Paper: Fernando B. Pérez Maurera, Maurizio Ferrari Dacrema, Lorenzo Saule, Mario Scriminaci, and Paolo Cremonesi.
    2020. ContentWise Impressions: An Industrial Dataset with Impressions Included.
    In Proceedings of the 29th ACM International Conference on Information & Knowledge Management (CIKM '20).
    Association for Computing Machinery, New York, NY, USA, 3093–3100. DOI:https://doi.org/10.1145/3340531.341277

    URL: https://github.com/ContentWise/contentwise-impressions
    """

    def __init__(self,
                 user_2_item: RatingMatrix,
                 user_2_series: RatingMatrix,
                 user_2_item_impr: RatingMatrix,
                 user_2_series_impr: RatingMatrix,
                 user_2_item_ts: TemporalDistribution,
                 user_2_series_ts: TemporalDistribution,
                 user_2_item_impr_ts: TemporalDistribution,
                 user_2_series_impr_ts: TemporalDistribution,
                 items: typing.Dict[int, ContentWiseItem],
                 series: typing.Dict[int, ContentWiseSeries],
                 impressions: Impressions):
        """
        Initializes the dataset.
        :param user_2_item: the rating matrix relating users to items.
        :param user_2_series: the rating matrix relating users to series.
        :param user_2_item_impr: the user-item rating matrix, limited to those ratings coming from impressions.
        :param user_2_series_impr: the user-series rating matrix, limited to those ratings coming from impressions.
        :param user_2_item_ts: the temporal distribution of user-item interactions.
        :param user_2_series_ts: the temporal distribution of user-series interactions.
        :param user_2_item_impr_ts: the temporal distribution of user-item interactions, limited to those ratings
                                    coming from impressions.
        :param user_2_series_impr_ts: the temporal distribution of user-series interactions, limited to those ratings
                                      coming from impressions.
        :param items: a dictionary containing information about the items.
        :param series: a dictionary containing information about the series.
        :param impressions: the impressions of the different users (stores the series shown to the different users).
        """

        self.user_2_item = user_2_item
        self.user_2_series = user_2_series
        self.user_2_item_impr = user_2_item_impr
        self.user_2_series_impr = user_2_series_impr
        self.user_2_item_ts = user_2_item_ts
        self.user_2_series_ts = user_2_series_ts
        self.user_2_item_impr_ts = user_2_item_impr_ts
        self.user_2_series_impr_ts = user_2_series_impr_ts
        self.items = items
        self.series = series
        self.impressions = impressions

    @staticmethod
    def load(interactions_file: str,
             impressions_direct_link_file: str,
             impressions_no_direct_link_file: str):
        """
        Loads the dataset from files.
        :param interactions_file: the file containing the interactions between users and items/series.
        :param impressions_direct_link_file: impressions related to a recommendation.
        :param impressions_no_direct_link_file: impressions not related to a recommendation.
        :return: the fully loaded ContentWise dataset.
        """

        items = typing.Dict[int, ContentWiseItem]()
        series = typing.Dict[int, ContentWiseSeries]()

        user_2_item = RatingMatrix(0.0, True, True)
        user_2_series = RatingMatrix(0.0, True, True)
        user_2_item_impr = RatingMatrix(0.0, True, True)
        user_2_series_impr = RatingMatrix(0.0, True, True)

        user_2_item_ts = TemporalDistribution()
        user_2_series_ts = TemporalDistribution()
        user_2_item_impr_ts = TemporalDistribution()
        user_2_series_impr_ts = TemporalDistribution()

        rec_2_user = dict()
        impr = Impressions()

        with open(interactions_file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for record in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    ts = int(record["utc_ts_milliseconds"])
                    user = int(record["user_id"])
                    item = int(record["item_id"])
                    series_id = int(record["series_id"])
                    episode = int(record["episode_number"])
                    length = int(record["series_length"])
                    item_type = ContentWiseItemType.from_value(int(record["item_type"]))
                    rec_id = int(record["recommendation_id"])

                    from_impr = rec_id >= 0

                    # In this loader, we assume that all the interactions are positive feedback.
                    # STEP 1: We add the a) user and b) item to their indexes
                    items[item] = ContentWiseItem(item, series_id, episode, item_type)
                    series[series_id] = ContentWiseSeries(series_id, length)

                    user_2_item.add_user(user)
                    user_2_item.add_item(item)
                    user_2_item_impr.add_user(user)
                    user_2_item_impr.add_item(item)

                    user_2_series.add_user(user)
                    user_2_series.add_item(series_id)
                    user_2_series_impr.add_user(user)
                    user_2_series_impr.add_item(series_id)

                    impr.add_user(user)
                    impr.add_item(item)

                    ret_item = user_2_item.rate(user, item, 1.0)
                    ret_series = user_2_series.rate(user, series_id, 1.0)
                    if ret_item == AddingReturn.ADDED:
                        user_2_item_ts = user_2_item_ts.add_timepoint(user, item, ts)
                    if ret_series == AddingReturn.ADDED:
                        user_2_series_ts = user_2_series_ts.add_timepoint(user, series_id, ts)

                    if from_impr:
                        rec_2_user[rec_id] = user
                        ret_item = user_2_item_impr.rate(user, item, 1.0)
                        ret_series = user_2_series_impr.rate(user, series_id, 1.0)
                        if ret_item:
                            user_2_item_impr_ts.add_timepoint(user, item, ts)
                        if ret_series:
                            user_2_series_impr_ts.add_timepoint(user, series_id, ts)

        # Read the impressions with interactions
        with open(impressions_direct_link_file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for record in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    rec_id = int(record["recommendation_id"])
                    listed_impr = str(record["recommended_series_list"])

                    actual_list = listed_impr[1:len(listed_impr) - 1]
                    impressions = actual_list.split("\\P{Alpha}+")
                    for impression in impressions:
                        series_id = int(impression)
                        impr.add_impression(rec_2_user[rec_id], series_id)

        # Read the impressions without interactions
        with open(impressions_no_direct_link_file, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for record in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    user = record["user_id"]
                    listed_impr = str(record["recommended_series_list"])

                    actual_list = list[1:len(listed_impr) - 1]
                    impressions = actual_list.split("\\P{Alpha}+")
                    for impression in impressions:
                        impr.add_impression(user, int(impression))

        return ContentWiseDataset(user_2_item, user_2_series, user_2_item_impr, user_2_series_impr, user_2_item_ts,
                                  user_2_series_ts, user_2_item_impr_ts, user_2_series_impr_ts,
                                  items, series, impr)

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

    def num_series(self):
        """
        Obtains the number of series in the dataset.
        :return: the number of series in the dataset.
        """
        return self.user_2_series.get_num_items()

    def get_user_2_item_interactions(self):
        """
        Obtains the user-item rating matrix.
        :return: the user-item rating matrix.
        """
        return self.user_2_item

    def get_user_2_series_interactions(self):
        """
        Obtains the user-series rating matrix.
        :return: the user-series rating matrix.
        """
        return self.user_2_series

    def get_user_2_item_interactions_from_impressions(self):
        """
        Obtains the user-item rating matrix, limited to those ratings coming from impressions.
        :return: the user-item rating matrix, limited to those ratings coming from impressions.
        """
        return self.user_2_item_impr

    def get_user_2_series_interactions_from_impressions(self):
        """
        Obtains the user-series rating matrix, limited to those ratings coming from impressions.
        :return: the user-series rating matrix, limited to those ratings coming from impressions.
        """
        return self.user_2_series_impr

    def get_impressions(self):
        """
        Obtains the impressions of series to the users.
        :return: the impressions of series to the users.
        """
        return self.impressions

    def get_user_2_item_interactions_temporal_distribution(self):
        """
        Obtains the temporal distribution of user-item ratings.
        :return: the temporal distribution of user-item ratings.
        """
        return self.user_2_item_ts

    def get_user_2_series_interactions_temporal_distribution(self):
        """
        Obtains the temporal distribution of user-series ratings.
        :return: the temporal distribution of user-series ratings.
        """
        return self.user_2_series_ts

    def get_user_2_item_interactions_from_impressions_temporal_distribution(self):
        """
        Obtains the temporal distribution of user-item interactions, limited to ratings coming from impressions.
        :return: the temporal distribution of user-item interactions, limited to ratings coming from impressions.
        """
        return self.user_2_item_impr_ts

    def get_user_2_series_interactions_from_impressions_temporal_distribution(self):
        """
        Obtains the temporal distribution of user-series interactions, limited to ratings coming from impressions.
        :return: the temporal distribution of user-series interactions, limited to ratings coming from impressions.
        """
        return self.user_2_series_impr_ts
