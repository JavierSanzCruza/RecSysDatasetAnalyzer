"""
Script for analyzing different datasets.
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
import sys

from src.main.python.datasets.contentwise.dataset import ContentWiseDataset
from src.main.python.datasets.contentwise.statistics import ContentWiseStatistics
from src.main.python.datasets.replayer.dataset import ReplayerDataset
from src.main.python.datasets.replayer.statistics import ReplayerStatistics
from src.main.python.inputoutput.impressions import ImpressionDistributionWriter
from src.main.python.inputoutput.pop import PopularityDistributionWriter
from src.main.python.inputoutput.statistics import StatisticsWriter
from src.main.python.inputoutput.temporal import TemporalDistributionWriter
from src.main.python.properties.distributions.impression_distribution import ImpressionsDistribution
from src.main.python.properties.distributions.popularity_distribution import PopularityDistribution

import time

CONTENTWISE = "ContentWise"
REPLAYER = "Replayer"

dataset = sys.argv[1]

if dataset == CONTENTWISE:
    time_a = time.time()
    inter = sys.argv[2]
    impr_direct = sys.argv[3]
    impr_no_direct = sys.argv[4]

    # Step 1: read the dataset.
    data = ContentWiseDataset.load(inter, impr_direct, impr_no_direct)
    time_b = time.time()
    print("Data read (" + str(time_b - time_a) + "s.)")

    # Step 2: find the statistics
    stats = ContentWiseStatistics(data)
    StatisticsWriter.write(stats, sys.argv[5] + "stats.txt")
    time_b = time.time()
    print("Stats computed (" + str(time_b - time_a) + "s.)")

    # Step 3: print the popularity distributions
    pop = PopularityDistribution(data.get_user_2_item_interactions())
    PopularityDistributionWriter.write(pop, sys.argv[5] + "pop-user-item.txt")
    pop = PopularityDistribution(data.get_user_2_series_interactions())
    PopularityDistributionWriter.write(pop, sys.argv[5] + "pop-user-series.txt")
    pop = PopularityDistribution(data.get_user_2_item_interactions_from_impressions())
    PopularityDistributionWriter.write(pop, sys.argv[5] + "pop-user-item-impr.txt")
    pop = PopularityDistribution(data.get_user_2_series_interactions())
    PopularityDistributionWriter.write(pop, sys.argv[5] + "pop-user-series-impr.txt")
    time_b = time.time()
    print("Popularity distributions computed (" + str(time_b - time_a) + "s.)")

    # Step 4: print the distributions for the impressions:
    impr = ImpressionsDistribution(data.get_impressions())
    ImpressionDistributionWriter.write_user_distribution(impr, "impr-user.txt")
    ImpressionDistributionWriter.write_item_distribution(impr, "impr-series.txt")
    time_b = time.time()
    print("Impressions distributions computed (" + str(time_b - time_a) + "s.)")

    # Step 5: print the temporal distribution for users, items and series
    temp = data.get_user_2_item_interactions_temporal_distribution()
    TemporalDistributionWriter.write_user_distribution(temp, sys.argv[5] + "time-users.txt")
    TemporalDistributionWriter.write_item_distribution(temp, sys.argv[5] + "time-items.txt")
    temp = data.get_user_2_series_interactions_temporal_distribution()
    TemporalDistributionWriter.write_item_distribution(temp, sys.argv[5] + "time-series.txt")
    temp = data.get_user_2_item_interactions_from_impressions_temporal_distribution()
    TemporalDistributionWriter.write_user_distribution(temp, sys.argv[5] + "time-users-impressions.txt")
    TemporalDistributionWriter.write_item_distribution(temp, sys.argv[5] + "time-items-impressions.txt")
    temp = data.get_user_2_series_interactions_from_impressions_temporal_distribution()
    TemporalDistributionWriter.write_item_distribution(temp, sys.argv[5] + "time-series-impressions.txt")

    temp = data.get_user_2_item_interactions_temporal_distribution()
    TemporalDistributionWriter.write_user_distribution(temp, sys.argv[5] + "time-users-inv.txt", natural_order=False)
    TemporalDistributionWriter.write_item_distribution(temp, sys.argv[5] + "time-items-inv.txt", natural_order=False)
    temp = data.get_user_2_series_interactions_temporal_distribution()
    TemporalDistributionWriter.write_item_distribution(temp, sys.argv[5] + "time-series-inv.txt", natural_order=False)
    temp = data.get_user_2_item_interactions_from_impressions_temporal_distribution()
    TemporalDistributionWriter.write_user_distribution(temp, sys.argv[5] + "time-users-impressions-inv.txt",
                                                       natural_order=False)
    TemporalDistributionWriter.write_item_distribution(temp, sys.argv[5] + "time-items-impressions-inv.txt",
                                                       natural_order=False)
    temp = data.get_user_2_series_interactions_from_impressions_temporal_distribution()
    TemporalDistributionWriter.write_item_distribution(temp, sys.argv[5] + "time-series-impressions-inv.txt",
                                                       natural_order=False)

    time_b = time.time()
    print("Temporal distributions computed (" + str(time_b - time_a) + "s.)")
elif dataset == REPLAYER:
    time_a = time.time()

    inter = sys.argv[2]
    min_ratings = int(sys.argv[4] if len(sys.argv) > 4 else 0)

    # Step 1: read the dataset.
    data = ReplayerDataset.load_yahoo_r6b(inter, min_interactions_per_user=min_ratings)
    time_b = time.time()
    print("Data read (" + str(time_b - time_a) + "s.)")

    # Step 2: find the statistics
    stats = ReplayerStatistics(data)
    StatisticsWriter.write(stats, sys.argv[3] + "stats.txt")
    time_b = time.time()
    print("Stats computed (" + str(time_b - time_a) + "s.)")

    # Step 3: print the popularity distributions
    pop = PopularityDistribution(data.get_user_2_item_interactions())
    PopularityDistributionWriter.write(pop, sys.argv[3] + "pop-user-item.txt")


    time_b = time.time()
    print("Popularity distributions computed (" + str(time_b - time_a) + "s.)")

    # Step 4: print the distributions for the impressions:
    impr = ImpressionsDistribution(data.get_impressions())
    ImpressionDistributionWriter.write_user_distribution(impr, "impr-user.txt")
    ImpressionDistributionWriter.write_item_distribution(impr, "impr-items.txt")
    time_b = time.time()
    print("Impressions distributions computed (" + str(time_b - time_a) + "s.)")

    # Step 5: print the temporal distribution for users, items and series
    temp = data.get_user_2_item_interactions_temporal_distribution()
    TemporalDistributionWriter.write_user_distribution(temp, sys.argv[3] + "time-users.txt")
    TemporalDistributionWriter.write_item_distribution(temp, sys.argv[3] + "time-items.txt")

    time_b = time.time()
    print("Temporal distributions computed (" + str(time_b - time_a) + "s.)")
else:
    print("ERROR: The dataset you are trying to analyze is not correct.")
