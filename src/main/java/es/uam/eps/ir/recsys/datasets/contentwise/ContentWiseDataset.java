/*
 * Copyright (C) 2021 Information Retrieval Group at Universidad Autónoma
 * de Madrid, http://ir.ii.uam.es.
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */
package es.uam.eps.ir.recsys.datasets.contentwise;

import es.uam.eps.ir.recsys.datasets.data.Impressions;
import es.uam.eps.ir.recsys.datasets.data.RatingMatrix;
import es.uam.eps.ir.recsys.datasets.properties.TemporalDistribution;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVRecord;

import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.util.HashMap;
import java.util.Map;

/**
 * Class for reading the <a href="https://github.com/ContentWise/contentwise-impressions">ContentWise Impressions</a> dataset.
 *
 * <b>Reference: </b> F.B. Pérez Maurera, M. Ferrari Dacrema, L. Saule, M. Scriminaci and P. Cremonesi. ContentWise Impressions: An Industrial Dataset with Impressions Included. CIKM 2020.
 */
public class ContentWiseDataset
{
    /**
     * Header of the interactions file.
     */
    private final static String[] interHeaders = {"utc_ts_milliseconds", "user_id", "item_id","series_id","episode_number","series_length","item_type","recommendation_id","interaction_type","vision_factor","explicit_rating"};

    private final static String[] imprDirectHeader = {"recommendation_id","row_position","recommendation_list_length","recommended_series_list"};
    private final static String[] imprNonDirectHeader = {"user_id","row_position","recommendation_list_length","recommended_series_list"};

    private final RatingMatrix user2item;
    private final RatingMatrix user2series;
    private final RatingMatrix user2itemImpr;
    private final RatingMatrix user2seriesImpr;

    private final TemporalDistribution user2itemTS;
    private final TemporalDistribution user2seriesTS;
    private final TemporalDistribution user2itemImprTS;
    private final TemporalDistribution user2seriesImprTS;

    private final Map<Integer, ContentWiseItem> items;
    private final Map<Integer, ContentWiseSeries> series;

    private final Impressions impressions;

    /**
     * Constructor.
     * @param user2item         the interactions between users and items.
     * @param user2series       the interactions between users and series.
     * @param user2itemImpr     the interactions between users and items (with impressions)
     * @param user2seriesImpr   the interactions between users and series (with impressions)
     * @param user2itemTS       the timestamps of the interactions between users and items.
     * @param user2seriesTS     the timestamps of the interactions between users and series.
     * @param user2itemImprTS   the timestamps of the interactions between users and items (with impressions)
     * @param user2seriesImprTS the timestamps of the interactions between users and series (with impressions)
     * @param items             the items.
     * @param series            the series.
     * @param impressions       the impressions (series recommended to users).
     */
    public ContentWiseDataset(RatingMatrix user2item, RatingMatrix user2series, RatingMatrix user2itemImpr, RatingMatrix user2seriesImpr, TemporalDistribution user2itemTS, TemporalDistribution user2seriesTS, TemporalDistribution user2itemImprTS, TemporalDistribution user2seriesImprTS, Map<Integer, ContentWiseItem> items, Map<Integer, ContentWiseSeries> series, Impressions impressions)
    {
        this.user2item = user2item;
        this.user2series = user2series;
        this.user2itemImpr = user2itemImpr;
        this.user2seriesImpr = user2seriesImpr;
        this.user2itemTS = user2itemTS;
        this.user2seriesTS = user2seriesTS;
        this.user2itemImprTS = user2itemImprTS;
        this.user2seriesImprTS = user2seriesImprTS;
        this.items = items;
        this.series = series;
        this.impressions = impressions;
    }

    /**
     * Loads the ContentWise Impressions dataset from a file, and stores the most important values.
     * @param interactionsFile              the interactions file.
     * @param impressionsDirectLinkFile     the file containing the impressions with interactions.
     * @param impressionsNoDirectLinkFile   the file containing the impressions without interactions.
     * @return the ContentWise Impressions dataset loaded into memory.
     */
    public static ContentWiseDataset load(String interactionsFile, String impressionsDirectLinkFile, String impressionsNoDirectLinkFile) throws IOException
    {
        Map<Integer, ContentWiseItem> items = new HashMap<>();
        Map<Integer, ContentWiseSeries> series = new HashMap<>();

        RatingMatrix user2item = new RatingMatrix(0, true, true);
        RatingMatrix user2series = new RatingMatrix(0, true, true);
        RatingMatrix user2itemImpr = new RatingMatrix(0, true, true);
        RatingMatrix user2seriesImpr = new RatingMatrix(0, true, true);

        TemporalDistribution user2itemTS = new TemporalDistribution();
        TemporalDistribution user2seriesTS = new TemporalDistribution();
        TemporalDistribution user2itemImprTS = new TemporalDistribution();
        TemporalDistribution user2seriesImprTS = new TemporalDistribution();

        Map<Integer, Integer> rec2user = new HashMap<>();
        Impressions impr = new Impressions();

        // As a first step, we add the information about the interactions
        try(Reader in = new FileReader(interactionsFile))
        {
            Iterable<CSVRecord> records = CSVFormat.DEFAULT.withHeader(interHeaders).withFirstRecordAsHeader().parse(in);
            for(CSVRecord record : records)
            {
                long ts = Long.parseLong(record.get("utc_ts_milliseconds"));
                int userId = Integer.parseInt(record.get("user_id"));
                int itemId = Integer.parseInt(record.get("item_id"));
                int seriesId = Integer.parseInt(record.get("series_id"));
                int episodeNumber = Integer.parseInt(record.get("episode_number"));
                int seriesLength = Integer.parseInt(record.get("series_length"));
                ContentWiseItemType type = ContentWiseItemType.from(Integer.parseInt(record.get("item_type")));

                int recId = Integer.parseInt(record.get("recommendation_id"));

                boolean fromImpr = recId >= 0;

                // In this loader, we assume that all interactions are positive feedback.

                // STEP 1: We add the a) user b) item and c) series to their indexes
                items.put(itemId, new ContentWiseItem(itemId, seriesId, episodeNumber, type));
                series.put(seriesId, new ContentWiseSeries(seriesId, seriesLength));

                user2item.addUser(userId);
                user2item.addItem(itemId);
                user2itemImpr.addUser(userId);
                user2itemImpr.addItem(itemId);
                user2series.addUser(userId);
                user2series.addItem(seriesId);
                user2seriesImpr.addUser(userId);
                user2seriesImpr.addItem(seriesId);

                impr.addUser(userId);
                impr.addItem(seriesId);

                user2item.addRating(userId, itemId, 1.0);
                user2series.addRating(userId, seriesId, 1.0);
                user2itemTS.addTimepoint(userId, itemId, ts);
                user2seriesTS.addTimepoint(userId, seriesId, ts);

                if (fromImpr)
                {
                    rec2user.put(recId, userId);
                    user2item.addRating(userId, itemId, 1.0);
                    user2series.addRating(userId, seriesId, 1.0);
                    user2itemTS.addTimepoint(userId, itemId, ts);
                    user2seriesTS.addTimepoint(userId, seriesId, ts);
                }
            }
        }

        // Read the impressions with interactions.
        try(Reader in = new FileReader(impressionsDirectLinkFile))
        {
            Iterable<CSVRecord> records = CSVFormat.DEFAULT.withHeader(imprDirectHeader).withFirstRecordAsHeader().parse(in);
            for(CSVRecord record : records)
            {
                int recId = Integer.parseInt(record.get("recommendation_id"));
                String list = record.get("recommended_series_list");

                String actualList = list.substring(1,list.length()-1);
                String[] impressions = actualList.split("\\P{Alpha}+");
                for(String impression : impressions)
                {
                    int seriesId = Integer.parseInt(impression);
                    impr.addImpression(rec2user.get(recId), seriesId);
                }
            }
        }

        // Read the impressions without interactions.
        try(Reader in = new FileReader(impressionsDirectLinkFile))
        {
            Iterable<CSVRecord> records = CSVFormat.DEFAULT.withHeader(impressionsNoDirectLinkFile).withFirstRecordAsHeader().parse(in);
            for(CSVRecord record : records)
            {
                int userId = Integer.parseInt(record.get("user_id"));
                String list = record.get("recommended_series_list");

                String actualList = list.substring(1,list.length()-1);
                String[] impressions = actualList.split("\\P{Alpha}+");
                for(String impression : impressions)
                {
                    int seriesId = Integer.parseInt(impression);
                    impr.addImpression(userId, seriesId);
                }
            }
        }

        return new ContentWiseDataset(user2item, user2series, user2itemImpr, user2seriesImpr, user2itemTS, user2seriesTS, user2itemImprTS, user2seriesImprTS, items, series, impr);
    }

    public long numUsers()
    {
        return this.user2item.getNumUsers();
    }

    public long numItems()
    {
        return this.user2item.getNumItems();
    }

    public long numSeries()
    {
        return this.user2series.getNumItems();
    }

    public RatingMatrix getUser2ItemInteractions()
    {
        return this.user2item;
    }

    public RatingMatrix getUser2SeriesInteractions()
    {
        return this.user2series;
    }

    public RatingMatrix getUser2ItemInteractionsFromImpressions()
    {
        return this.user2itemImpr;
    }

    public RatingMatrix getUser2SeriesInteractionsFromImpressions()
    {
        return this.user2seriesImpr;
    }

    public Impressions getImpressions()
    {
        return this.impressions;
    }


    public TemporalDistribution getUser2ItemTemporalDistrib()
    {
        return this.user2itemTS;
    }

    public TemporalDistribution getUser2SeriesTemporalDistrib()
    {
        return this.user2seriesTS;
    }

    public TemporalDistribution getUser2ItemWithImpressionsTemporalDistrib()
    {
        return this.user2itemImprTS;
    }

    public TemporalDistribution getUser2SeriesWithImpressionsTemporalDistrib()
    {
        return this.user2seriesImprTS;
    }
}