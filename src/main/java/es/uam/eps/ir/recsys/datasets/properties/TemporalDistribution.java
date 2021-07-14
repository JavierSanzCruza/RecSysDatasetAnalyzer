/*
 * Copyright (C) 2021 Information Retrieval Group at Universidad Autónoma
 * de Madrid, http://ir.ii.uam.es.
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */
package es.uam.eps.ir.recsys.datasets.properties;

import org.jooq.lambda.tuple.Tuple2;
import org.jooq.lambda.tuple.Tuple3;

import java.util.*;
import java.util.stream.Collectors;

/**
 * Class for computing and storing the popularity distribution of a dataset. It obtains a list containing the number of ratings
 * per item (it just stores these numbers, sorted from larger to smaller).
 *
 * @author Javier Sanz-Cruzado (javier.sanz-cruzado@uam.es)
 */
public class TemporalDistribution
{
    /**
     * The list storing the popularity distribution of the dataset.
     */
    private final List<Tuple3<Integer, Integer, Long>> distribution;
    private long minTimestamp;
    private long maxTimestamp;

    boolean isSorted;

    /**
     * Constructor. Initializes the temporal distribution.
     */
    public TemporalDistribution()
    {
        this.distribution = new ArrayList<>();
        this.isSorted = false;
        this.minTimestamp = Long.MAX_VALUE;
        this.maxTimestamp = Long.MIN_VALUE;
    }

    /**
     * Adds an individual time point to the series.
     * @param user      the user.
     * @param item      the item.
     * @param timestamp the moment of time when the rating is added.
     */
    public void addTimepoint(int user, int item, long timestamp)
    {
        this.distribution.add(new Tuple3<>(user, item, timestamp));
        this.isSorted = false;

        if(minTimestamp < timestamp)
        {
            minTimestamp = timestamp;
        }
        if(maxTimestamp > timestamp)
        {
            maxTimestamp = timestamp;
        }
    }

    /**
     * Obtains the distribution of the timestamps for a user.
     * @return the list containing the distribution.
     */
    public List<Tuple2<Integer, Long>> getUserDistribution()
    {
        if(!isSorted)
        {
            distribution.sort(Comparator.comparingLong(o -> o.v3));
            isSorted = true;
        }

        return distribution.stream().map(x -> new Tuple2<>(x.v1, x.v3)).collect(Collectors.toList());
    }

    /**
     * Obtains the distribution of timestamps for an item.
     * @return the list containing the distribution.
     */
    public List<Tuple2<Integer, Long>> getItemDistribution()
    {
        if(!isSorted)
        {
            distribution.sort(Comparator.comparingLong(o -> o.v3));
            isSorted = true;
        }

        return distribution.stream().map(x -> new Tuple2<>(x.v2, x.v3)).collect(Collectors.toList());
    }


}