"""
Class for computing the properties and statistics of the ContentWise dataset.
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

from src.main.python.datasets.contentwise.dataset import ContentWiseDataset
from src.main.python.properties.metrics.gl.item_gini_index import ItemGiniIndex
from src.main.python.properties.metrics.gl.user_gini_index import UserGiniIndex
from src.main.python.properties.metrics.individual.impression import Impression
from src.main.python.properties.metrics.individual.interaction import Interaction
from src.main.python.statistics import Statistics
from src.main.python.properties.metrics.gl.density import Density


class ContentWiseStatistics(Statistics):
    """
    Class for computing the properties and statistics of the ContentWise dataset.
    """

    # The names of the properties.
    NUM_USERS = "# users"
    NUM_ITEMS = "# items"
    NUM_SERIES = "# series"
    NUM_USER_ITEM_INTER = "# user-item interactions (no reps)"
    NUM_USER_SERIES_INTER = "# user-series interactions (no reps)"
    NUM_USER_ITEM_INTER_FROM_IMPR = "# user-item interactions from impressions (no reps)"
    NUM_USER_SERIES_INTER_FROM_IMPR = "# user-series interactions from impressions (no reps)"
    TOTAL_INTERACTIONS = "# total interactions (with reps)"
    TOTAL_INTERACTIONS_FROM_IMPR = "# total interactions from impressions (with reps)"
    MIN_TIMESTAMP = "Min. timestamp"
    MAX_TIMESTAMP = "Max. timestamp"

    ITEM_DENSITY = "Density (items)"
    SERIES_DENSITY = "Density (series)"
    ITEM_IMPR_DENSITY = "Density (items, from impressions)"
    SERIES_IMPR_DENSITY = "Density (series, from impressions)"

    AVG_ITEM_PER_USER = "Average ratings per user (item)"
    AVG_SERIES_PER_USER = "Average ratings per user (series)"
    AVG_USER_PER_ITEM = "Average ratings per item"
    AVG_USER_PER_SERIES = "Average ratings per series"

    AVG_ITEM_PER_USER_IMPR = "Average ratings per user (item, from impressions)"
    AVG_SERIES_PER_USER_IMPR = "Average ratings per user (series, from impressions)"
    AVG_USER_PER_ITEM_IMPR = "Average ratings per item (from impressions)"
    AVG_USER_PER_SERIES_IMPR = "Average ratings per series (from impressions)"

    MAX_ITEM_PER_USER = "Max ratings per user (item)"
    MAX_SERIES_PER_USER = "Max ratings per user (series)"
    MAX_USER_PER_ITEM = "Max ratings per item"
    MAX_USER_PER_SERIES = "Max ratings per series"

    MAX_ITEM_PER_USER_IMPR = "Max ratings per user (item, from impressions)"
    MAX_SERIES_PER_USER_IMPR = "Max ratings per user (series, from impressions)"
    MAX_USER_PER_ITEM_IMPR = "Max ratings per item (from impressions)"
    MAX_USER_PER_SERIES_IMPR = "Max ratings per series (from impressions)"

    MIN_ITEM_PER_USER = "Min ratings per user (item)"
    MIN_SERIES_PER_USER = "Min ratings per user (series)"
    MIN_USER_PER_ITEM = "Min ratings per item"
    MIN_USER_PER_SERIES = "Min ratings per series"

    MIN_ITEM_PER_USER_IMPR = "Min ratings per user (item, from impressions)"
    MIN_SERIES_PER_USER_IMPR = "Min ratings per user (series, from impressions)"
    MIN_USER_PER_ITEM_IMPR = "Min ratings per item (from impressions)"
    MIN_USER_PER_SERIES_IMPR = "Min ratings per series (from impressions)"

    NUM_IMPR = "# impressions"

    GINI_USER_ITEM = "User Gini (item)"
    GINI_ITEM = "Item Gini"
    GINI_USER_SERIES = "User Gini (series)"
    GINI_SERIES = "Series Gini"
    GINI_USER_ITEM_IMPR = "User Gini (item, from impressions)"
    GINI_USER_SERIES_IMPR = "User Gini (series, from impressions)"
    GINI_ITEM_IMPR = "Item Gini (from impressions)"
    GINI_SERIES_IMPR = "Series Gini (from impressions)"

    AVG_IMPR_PER_USER = "Average impressions per user"
    MAX_IMPR_PER_USER = "Max impressions per user"
    MIN_IMPR_PER_USER = "Min impressions per user"

    AVG_IMPR_PER_SERIES = "Average impressions per series"
    MAX_IMPR_PER_SERIES = "Max impressions per series"
    MIN_IMPR_PER_SERIES = "Min impressions per series"

    def __init__(self,
                 dataset: ContentWiseDataset):
        """
        Initializes and computes the statistics for the ContentWise dataset.
        :param dataset: the ContentWise dataset.
        """
        super().__init__()

        # Basic statistics
        self.add_stat(ContentWiseStatistics.NUM_USERS, dataset.num_users())
        self.add_stat(ContentWiseStatistics.NUM_ITEMS, dataset.num_items())
        self.add_stat(ContentWiseStatistics.NUM_SERIES, dataset.num_series())
        self.add_stat(ContentWiseStatistics.TOTAL_INTERACTIONS,
                      dataset.get_user_2_item_interactions().get_num_total_ratings())
        self.add_stat(ContentWiseStatistics.NUM_IMPR, dataset.get_impressions().get_num_impressions())
        self.add_stat(ContentWiseStatistics.TOTAL_INTERACTIONS_FROM_IMPR,
                      dataset.get_user_2_item_interactions_from_impressions().get_num_total_ratings())

        # The number of interactions
        self.add_stat(ContentWiseStatistics.NUM_USER_ITEM_INTER,
                      dataset.get_user_2_item_interactions().get_num_ratings())
        self.add_stat(ContentWiseStatistics.NUM_USER_SERIES_INTER,
                      dataset.get_user_2_series_interactions().get_num_ratings())
        self.add_stat(ContentWiseStatistics.NUM_USER_ITEM_INTER_FROM_IMPR,
                      dataset.get_user_2_item_interactions_from_impressions().get_num_ratings())
        self.add_stat(ContentWiseStatistics.NUM_USER_SERIES_INTER_FROM_IMPR,
                      dataset.get_user_2_series_interactions_from_impressions().get_num_ratings())

        # More complex

        # Density
        density = Density(dataset.get_user_2_item_interactions())
        self.add_stat(ContentWiseStatistics.ITEM_DENSITY, density.compute())
        density = Density(dataset.get_user_2_series_interactions())
        self.add_stat(ContentWiseStatistics.SERIES_DENSITY, density.compute())
        density = Density(dataset.get_user_2_item_interactions_from_impressions())
        self.add_stat(ContentWiseStatistics.ITEM_IMPR_DENSITY, density.compute())
        density = Density(dataset.get_user_2_series_interactions_from_impressions())
        self.add_stat(ContentWiseStatistics.SERIES_IMPR_DENSITY, density.compute())

        # Average numbers:
        interaction = Interaction(dataset.get_user_2_item_interactions())
        self.add_stat(ContentWiseStatistics.AVG_ITEM_PER_USER, interaction.average_over_users())
        self.add_stat(ContentWiseStatistics.MAX_ITEM_PER_USER, interaction.max_over_users())
        self.add_stat(ContentWiseStatistics.MIN_ITEM_PER_USER, interaction.min_over_users())

        self.add_stat(ContentWiseStatistics.AVG_USER_PER_ITEM, interaction.average_over_items())
        self.add_stat(ContentWiseStatistics.MAX_USER_PER_ITEM, interaction.max_over_items())
        self.add_stat(ContentWiseStatistics.MIN_USER_PER_ITEM, interaction.min_over_items())

        interaction = Interaction(dataset.get_user_2_series_interactions())
        self.add_stat(ContentWiseStatistics.AVG_SERIES_PER_USER, interaction.average_over_users())
        self.add_stat(ContentWiseStatistics.MAX_SERIES_PER_USER, interaction.max_over_users())
        self.add_stat(ContentWiseStatistics.MIN_SERIES_PER_USER, interaction.min_over_users())

        self.add_stat(ContentWiseStatistics.AVG_USER_PER_SERIES, interaction.average_over_items())
        self.add_stat(ContentWiseStatistics.MAX_USER_PER_SERIES, interaction.max_over_items())
        self.add_stat(ContentWiseStatistics.MIN_USER_PER_SERIES, interaction.min_over_items())

        interaction = Interaction(dataset.get_user_2_item_interactions_from_impressions())
        self.add_stat(ContentWiseStatistics.AVG_ITEM_PER_USER_IMPR, interaction.average_over_users())
        self.add_stat(ContentWiseStatistics.MAX_ITEM_PER_USER_IMPR, interaction.max_over_users())
        self.add_stat(ContentWiseStatistics.MIN_ITEM_PER_USER_IMPR, interaction.min_over_users())

        self.add_stat(ContentWiseStatistics.AVG_USER_PER_ITEM_IMPR, interaction.average_over_items())
        self.add_stat(ContentWiseStatistics.MAX_USER_PER_ITEM_IMPR, interaction.max_over_items())
        self.add_stat(ContentWiseStatistics.MIN_USER_PER_ITEM_IMPR, interaction.min_over_items())

        interaction = Interaction(dataset.get_user_2_series_interactions_from_impressions())
        self.add_stat(ContentWiseStatistics.AVG_SERIES_PER_USER_IMPR, interaction.average_over_users())
        self.add_stat(ContentWiseStatistics.MAX_SERIES_PER_USER_IMPR, interaction.max_over_users())
        self.add_stat(ContentWiseStatistics.MIN_SERIES_PER_USER_IMPR, interaction.min_over_users())

        self.add_stat(ContentWiseStatistics.AVG_USER_PER_SERIES_IMPR, interaction.average_over_items())
        self.add_stat(ContentWiseStatistics.MAX_USER_PER_SERIES_IMPR, interaction.max_over_items())
        self.add_stat(ContentWiseStatistics.MIN_USER_PER_SERIES_IMPR, interaction.min_over_items())

        # Gini values:
        self.add_stat(ContentWiseStatistics.GINI_ITEM,
                      ItemGiniIndex(dataset.get_user_2_item_interactions()).compute())
        self.add_stat(ContentWiseStatistics.GINI_SERIES,
                      ItemGiniIndex(dataset.get_user_2_series_interactions()).compute())
        self.add_stat(ContentWiseStatistics.GINI_ITEM_IMPR,
                      ItemGiniIndex(dataset.get_user_2_item_interactions_from_impressions()).compute())
        self.add_stat(ContentWiseStatistics.GINI_SERIES_IMPR,
                      ItemGiniIndex(dataset.get_user_2_series_interactions_from_impressions()).compute())

        self.add_stat(ContentWiseStatistics.GINI_USER_ITEM,
                      UserGiniIndex(dataset.get_user_2_item_interactions()).compute())
        self.add_stat(ContentWiseStatistics.GINI_USER_SERIES,
                      UserGiniIndex(dataset.get_user_2_series_interactions()).compute())
        self.add_stat(ContentWiseStatistics.GINI_USER_ITEM_IMPR,
                      UserGiniIndex(dataset.get_user_2_item_interactions_from_impressions()).compute())
        self.add_stat(ContentWiseStatistics.GINI_USER_SERIES_IMPR,
                      UserGiniIndex(dataset.get_user_2_series_interactions_from_impressions()).compute())

        # Impression count:
        impr = Impression(dataset.get_user_2_series_interactions(), dataset.get_impressions())
        self.add_stat(ContentWiseStatistics.AVG_IMPR_PER_USER, impr.average_over_users())
        self.add_stat(ContentWiseStatistics.MAX_IMPR_PER_USER, impr.max_over_users())
        self.add_stat(ContentWiseStatistics.MIN_IMPR_PER_USER, impr.min_over_users())

        self.add_stat(ContentWiseStatistics.AVG_IMPR_PER_SERIES, impr.average_over_items())
        self.add_stat(ContentWiseStatistics.MAX_IMPR_PER_SERIES, impr.max_over_items())
        self.add_stat(ContentWiseStatistics.MIN_IMPR_PER_SERIES, impr.min_over_items())
