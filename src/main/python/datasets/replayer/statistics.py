"""
Class for computing the properties and statistics of the replayer dataset.
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

from src.main.python.datasets.replayer.dataset import ReplayerDataset
from src.main.python.properties.metrics.gl.item_gini_index import ItemGiniIndex
from src.main.python.properties.metrics.gl.user_gini_index import UserGiniIndex
from src.main.python.properties.metrics.individual.impression import Impression
from src.main.python.properties.metrics.individual.interaction import Interaction
from src.main.python.statistics import Statistics
from src.main.python.properties.metrics.gl.density import Density


class ReplayerStatistics(Statistics):
    """
    Class for computing the properties and statistics of the Replayer dataset.
    """

    # The names of the properties.
    NUM_USERS = "# users"
    NUM_ITEMS = "# items"
    NUM_USER_ITEM_INTER = "# user-item interactions (no reps)"
    TOTAL_INTERACTIONS = "# total interactions (with reps)"
    MIN_TIMESTAMP = "Min. timestamp"
    MAX_TIMESTAMP = "Max. timestamp"

    ITEM_DENSITY = "Density (items)"

    AVG_ITEM_PER_USER = "Average ratings per user (item)"
    AVG_USER_PER_ITEM = "Average ratings per item"

    MAX_ITEM_PER_USER = "Max ratings per user (item)"
    MAX_USER_PER_ITEM = "Max ratings per item"

    MIN_ITEM_PER_USER = "Min ratings per user (item)"
    MIN_USER_PER_ITEM = "Min ratings per item"

    NUM_IMPR = "# impressions"

    GINI_USER_ITEM = "User Gini (item)"
    GINI_ITEM = "Item Gini"

    AVG_IMPR_PER_USER = "Average impressions per user"
    MAX_IMPR_PER_USER = "Max impressions per user"
    MIN_IMPR_PER_USER = "Min impressions per user"

    AVG_IMPR_PER_ITEM = "Average impressions per item"
    MAX_IMPR_PER_ITEM = "Max impressions per item"
    MIN_IMPR_PER_ITEM = "Min impressions per item"

    def __init__(self,
                 dataset: ReplayerDataset):
        """
        Initializes and computes the statistics for the ContentWise dataset.
        :param dataset: the replayer dataset.
        """
        super().__init__()

        # Basic statistics
        self.add_stat(ReplayerStatistics.NUM_USERS, dataset.num_users())
        self.add_stat(ReplayerStatistics.NUM_ITEMS, dataset.num_items())
        self.add_stat(ReplayerStatistics.TOTAL_INTERACTIONS,
                      dataset.get_user_2_item_interactions().get_num_total_ratings())
        self.add_stat(ReplayerStatistics.NUM_IMPR, dataset.get_impressions().get_num_impressions())

        # The number of interactions
        self.add_stat(ReplayerStatistics.NUM_USER_ITEM_INTER,
                      dataset.get_user_2_item_interactions().get_num_ratings())

        # More complex

        # Density
        density = Density(dataset.get_user_2_item_interactions())
        self.add_stat(ReplayerStatistics.ITEM_DENSITY, density.compute())

        # Average numbers:
        interaction = Interaction(dataset.get_user_2_item_interactions())
        self.add_stat(ReplayerStatistics.AVG_ITEM_PER_USER, interaction.average_over_users())
        self.add_stat(ReplayerStatistics.MAX_ITEM_PER_USER, interaction.max_over_users())
        self.add_stat(ReplayerStatistics.MIN_ITEM_PER_USER, interaction.min_over_users())

        self.add_stat(ReplayerStatistics.AVG_USER_PER_ITEM, interaction.average_over_items())
        self.add_stat(ReplayerStatistics.MAX_USER_PER_ITEM, interaction.max_over_items())
        self.add_stat(ReplayerStatistics.MIN_USER_PER_ITEM, interaction.min_over_items())

        # Gini values:
        self.add_stat(ReplayerStatistics.GINI_ITEM,
                      ItemGiniIndex(dataset.get_user_2_item_interactions()).compute())
        self.add_stat(ReplayerStatistics.GINI_USER_ITEM,
                      UserGiniIndex(dataset.get_user_2_item_interactions()).compute())

        # Impression count:
        impr = Impression(dataset.get_user_2_item_interactions(), dataset.get_impressions())
        self.add_stat(ReplayerStatistics.AVG_IMPR_PER_USER, impr.average_over_users())
        self.add_stat(ReplayerStatistics.MAX_IMPR_PER_USER, impr.max_over_users())
        self.add_stat(ReplayerStatistics.MIN_IMPR_PER_USER, impr.min_over_users())

        self.add_stat(ReplayerStatistics.AVG_IMPR_PER_ITEM, impr.average_over_items())
        self.add_stat(ReplayerStatistics.MAX_IMPR_PER_ITEM, impr.max_over_items())
        self.add_stat(ReplayerStatistics.MIN_IMPR_PER_ITEM, impr.min_over_items())
