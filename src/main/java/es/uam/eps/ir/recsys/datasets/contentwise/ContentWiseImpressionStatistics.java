/*
 * Copyright (C) 2021 Information Retrieval Group at Universidad Autónoma
 * de Madrid, http://ir.ii.uam.es.
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */
package es.uam.eps.ir.recsys.datasets.contentwise;

import es.uam.eps.ir.recsys.datasets.Statistics;
import es.uam.eps.ir.recsys.datasets.properties.*;

/**
 * Statistics for the ContentWise impressions dataset.
 *
 * @author Javier Sanz-Cruzado (javier.sanz-cruzado@uam.es)
 */
public class ContentWiseImpressionStatistics extends Statistics
{
    private final static String NUM_USERS = "# users";
    private final static String NUM_ITEMS = "# items";
    private final static String NUM_SERIES = "# series";
    private final static String NUM_USER_ITEM_INTER = "# user-item interactions (no reps)";
    private final static String NUM_USER_SERIES_INTER = "# user-series interactions (no reps)";
    private final static String NUM_USER_ITEM_INTER_FROM_IMPR = "# user-item interactions from impressions (no reps)";
    private final static String NUM_USER_SERIES_INTER_FROM_IMPR = "# user-series interactions from impressions (no reps)";
    private final static String TOTAL_INTERACTIONS = "# total interactions (with reps)";
    private final static String TOTAL_INTERACTIONS_FROM_IMPR = "# total interactions from impressions (with reps)";
    private final static String MIN_TIMESTAMP = "Min. timestamp";
    private final static String MAX_TIMESTAMP = "Max. timestamp";

    private final static String ITEM_DENSITY = "Density (items)";
    private final static String SERIES_DENSITY = "Density (series)";
    private final static String ITEM_IMPR_DENSITY = "Density (items, with impressions)";
    private final static String SERIES_IMPR_DENSITY = "Density (series, with impressions)";

    private final static String AVG_ITEM_PER_USER = "Average ratings per user (item)";
    private final static String AVG_SERIES_PER_USER = "Average ratings per user (series)";
    private final static String AVG_USER_PER_ITEM = "Average ratings per item";
    private final static String AVG_USER_PER_SERIES = "Average ratings per series";

    private final static String AVG_ITEM_PER_USER_IMPR = "Average ratings per user (item, with impressions)";
    private final static String AVG_SERIES_PER_USER_IMPR = "Average ratings per user (series, with impressions)";
    private final static String AVG_USER_PER_ITEM_IMPR = "Average ratings per item (with impressions)";
    private final static String AVG_USER_PER_SERIES_IMPR = "Average ratings per series (with impressions)";

    private final static String MIN_ITEM_PER_USER = "Min ratings per user (item)";
    private final static String MIN_SERIES_PER_USER = "Min ratings per user (series)";
    private final static String MIN_USER_PER_ITEM = "Min ratings per item";
    private final static String MIN_USER_PER_SERIES = "Min ratings per series";

    private final static String MIN_ITEM_PER_USER_IMPR = "Min ratings per user (item, with impressions)";
    private final static String MIN_SERIES_PER_USER_IMPR = "Min ratings per user (series, with impressions)";
    private final static String MIN_USER_PER_ITEM_IMPR = "Min ratings per item (with impressions)";
    private final static String MIN_USER_PER_SERIES_IMPR = "Min ratings per series (with impressions)";

    private final static String MAX_ITEM_PER_USER = "Max ratings per user (item)";
    private final static String MAX_SERIES_PER_USER = "Max ratings per user (series)";
    private final static String MAX_USER_PER_ITEM = "Max ratings per item";
    private final static String MAX_USER_PER_SERIES = "Max ratings per series";

    private final static String MAX_ITEM_PER_USER_IMPR = "Max ratings per user (item, with impressions)";
    private final static String MAX_SERIES_PER_USER_IMPR = "Max ratings per user (series, with impressions)";
    private final static String MAX_USER_PER_ITEM_IMPR = "Max ratings per item (with impressions)";
    private final static String MAX_USER_PER_SERIES_IMPR = "Max ratings per series (with impressions)";

    private final static String NUM_IMPR = "Num. impressions";

    public final static String GINI_USER_ITEM = "User Gini (item)";
    public final static String GINI_ITEM = "Item Gini";
    public final static String GINI_USER_SERIES = "User Gini (series)";
    public final static String GINI_SERIES = "Series Gini";
    public final static String GINI_USER_ITEM_IMPR = "User Gini (item, with impressions)";
    public final static String GINI_ITEM_IMPR = "Item Gini (with impressions)";
    public final static String GINI_USER_SERIES_IMPR = "User Gini (series, with impressions)";
    public final static String GINI_SERIES_IMPR = "Series Gini (with impressions)";

    private final static String AVG_IMPR_PER_USER = "Average impressions per user";
    private final static String MIN_IMPR_PER_USER = "Minimum impressions per user";
    private final static String MAX_IMPR_PER_USER = "Maximum impressions per user";
    private final static String AVG_IMPR_PER_SERIES = "Average impressions per series";
    private final static String MIN_IMPR_PER_SERIES = "Minimum impressions per series";
    private final static String MAX_IMPR_PER_SERIES = "Maximum impressions per series";

    public ContentWiseImpressionStatistics(ContentWiseDataset dataset)
    {
        // Basic statistics.
        this.addLongStat(NUM_USERS, dataset.numUsers());
        this.addLongStat(NUM_ITEMS, dataset.numItems());
        this.addLongStat(NUM_SERIES, dataset.numSeries());

        // The number of interactions:
        this.addLongStat(NUM_USER_ITEM_INTER, dataset.getUser2ItemInteractions().getNumRatings());
        this.addLongStat(NUM_USER_SERIES_INTER, dataset.getUser2SeriesInteractions().getNumRatings());
        this.addLongStat(NUM_USER_ITEM_INTER_FROM_IMPR, dataset.getUser2ItemInteractionsFromImpressions().getNumRatings());
        this.addLongStat(NUM_USER_SERIES_INTER_FROM_IMPR, dataset.getUser2SeriesInteractionsFromImpressions().getNumRatings());

        this.addLongStat(TOTAL_INTERACTIONS, dataset.getUser2ItemInteractions().getNumTotalRatings());
        this.addLongStat(TOTAL_INTERACTIONS_FROM_IMPR, dataset.getUser2ItemInteractionsFromImpressions().getNumTotalRatings());

        // The number of impressions
        this.addLongStat(NUM_IMPR, dataset.getImpressions().getNumImpressions());

        // The average number of impressions per user / series


        // More complex:

        // Density
        Density user2itemDensity = new Density(dataset.getUser2ItemInteractions());
        this.addDoubleStat(ITEM_DENSITY, user2itemDensity.density());
        Density user2seriesDensity = new Density(dataset.getUser2SeriesInteractions());
        this.addDoubleStat(SERIES_DENSITY, user2seriesDensity.density());
        Density user2itemImprDensity = new Density(dataset.getUser2ItemInteractions());
        this.addDoubleStat(ITEM_IMPR_DENSITY, user2itemImprDensity.density());
        Density user2seriesImprDensity = new Density(dataset.getUser2SeriesInteractions());
        this.addDoubleStat(SERIES_IMPR_DENSITY, user2seriesImprDensity.density());

        // Average numbers
        InteractionCount avgcount = new InteractionCount(dataset.getUser2ItemInteractions());
        this.addDoubleStat(AVG_ITEM_PER_USER, avgcount.averageCountUsers());
        this.addDoubleStat(MIN_ITEM_PER_USER, avgcount.minCountUsers());
        this.addDoubleStat(MAX_ITEM_PER_USER, avgcount.maxCountUsers());

        this.addDoubleStat(AVG_USER_PER_ITEM, avgcount.averageCountItems());
        this.addDoubleStat(MIN_USER_PER_ITEM, avgcount.minCountItems());
        this.addDoubleStat(MAX_USER_PER_ITEM, avgcount.maxCountItems());

        avgcount = new InteractionCount(dataset.getUser2SeriesInteractions());
        this.addDoubleStat(AVG_SERIES_PER_USER, avgcount.averageCountUsers());
        this.addDoubleStat(MIN_SERIES_PER_USER, avgcount.minCountUsers());
        this.addDoubleStat(MAX_SERIES_PER_USER, avgcount.maxCountUsers());

        this.addDoubleStat(AVG_USER_PER_SERIES, avgcount.averageCountItems());
        this.addDoubleStat(MIN_USER_PER_SERIES, avgcount.minCountItems());
        this.addDoubleStat(MAX_USER_PER_SERIES, avgcount.maxCountItems());

        avgcount = new InteractionCount(dataset.getUser2ItemInteractionsFromImpressions());
        this.addDoubleStat(AVG_ITEM_PER_USER_IMPR, avgcount.averageCountUsers());
        this.addDoubleStat(MIN_ITEM_PER_USER_IMPR, avgcount.minCountUsers());
        this.addDoubleStat(MAX_ITEM_PER_USER_IMPR, avgcount.maxCountUsers());

        this.addDoubleStat(AVG_USER_PER_ITEM_IMPR, avgcount.averageCountItems());
        this.addDoubleStat(MIN_USER_PER_ITEM_IMPR, avgcount.minCountItems());
        this.addDoubleStat(MAX_USER_PER_ITEM_IMPR, avgcount.maxCountItems());

        avgcount = new InteractionCount(dataset.getUser2SeriesInteractionsFromImpressions());
        this.addDoubleStat(AVG_SERIES_PER_USER_IMPR, avgcount.averageCountUsers());
        this.addDoubleStat(MIN_SERIES_PER_USER_IMPR, avgcount.minCountUsers());
        this.addDoubleStat(MAX_SERIES_PER_USER_IMPR, avgcount.maxCountUsers());

        this.addDoubleStat(AVG_USER_PER_SERIES_IMPR, avgcount.averageCountItems());
        this.addDoubleStat(MIN_USER_PER_SERIES_IMPR, avgcount.minCountItems());
        this.addDoubleStat(MAX_USER_PER_SERIES_IMPR, avgcount.maxCountItems());


        // Item Gini values:
        GiniIndex giniIndex = new GiniIndex(dataset.getUser2ItemInteractions());
        this.addDoubleStat(GINI_USER_ITEM, giniIndex.userGini());
        this.addDoubleStat(GINI_ITEM, giniIndex.itemGini());

        giniIndex = new GiniIndex(dataset.getUser2SeriesInteractions());
        this.addDoubleStat(GINI_USER_SERIES, giniIndex.userGini());
        this.addDoubleStat(GINI_SERIES, giniIndex.itemGini());

        giniIndex = new GiniIndex(dataset.getUser2ItemInteractionsFromImpressions());
        this.addDoubleStat(GINI_USER_ITEM_IMPR, giniIndex.userGini());
        this.addDoubleStat(GINI_ITEM_IMPR, giniIndex.itemGini());

        giniIndex = new GiniIndex(dataset.getUser2SeriesInteractionsFromImpressions());
        this.addDoubleStat(GINI_USER_SERIES_IMPR, giniIndex.userGini());
        this.addDoubleStat(GINI_SERIES_IMPR, giniIndex.itemGini());

        ImpressionCount imprCount = new ImpressionCount(dataset.getImpressions());
        this.addDoubleStat(AVG_IMPR_PER_USER, imprCount.averageCountUsers());
        this.addDoubleStat(MIN_IMPR_PER_USER, imprCount.minCountUsers());
        this.addDoubleStat(MAX_IMPR_PER_USER, imprCount.maxCountUsers());

        this.addDoubleStat(AVG_IMPR_PER_SERIES, imprCount.averageCountItems());
        this.addDoubleStat(MIN_IMPR_PER_SERIES, imprCount.minCountItems());
        this.addDoubleStat(MAX_IMPR_PER_SERIES, imprCount.maxCountItems());

    }
}