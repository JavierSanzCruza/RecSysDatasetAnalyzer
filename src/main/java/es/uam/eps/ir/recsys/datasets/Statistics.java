/*
 * Copyright (C) 2021 Information Retrieval Group at Universidad Autónoma
 * de Madrid, http://ir.ii.uam.es.
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */
package es.uam.eps.ir.recsys.datasets;

import org.jooq.lambda.tuple.Tuple2;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Stores the basic statistics for a dataset. This class is abstract, since each dataset
 * has its own statistics.
 *
 * @author Javier Sanz-Cruzado (javier.sanz-cruzado@uam.es)
 */
public abstract class Statistics
{
    /**
     * The set of statistics which can be represented as a double.
     */
    protected final Map<String, Double> doubleStats;
    /**
     * The set of statistics which can be represented as a long.
     */
    protected final Map<String, Long> longStats;

    /**
     * The list of statistics.
     */
    protected final List<Tuple2<String, Boolean>> list;

    /**
     * Constructor.
     */
    public Statistics()
    {
        this.longStats = new HashMap<>();
        this.doubleStats = new HashMap<>();
        this.list = new ArrayList<>();
    }

    /**
     * Adds an statistic which can be represented as a long integer.
     * @param name the name of the statistic.
     * @param value the value of the statistic.
     */
    protected void addLongStat(String name, long value)
    {
        this.longStats.put(name, value);
        this.list.add(new Tuple2<>(name, false));
    }

    /**
     * Adds an statistic which can be represented as a double.
     * @param name the name of the statistic.
     * @param value the value of the statistic.
     */
    protected void addDoubleStat(String name, double value)
    {
        this.doubleStats.put(name, value);
        this.list.add(new Tuple2<>(name, true));
    }

    /**
     * Obtains the value of an statistic which can be represented as a long integer.
     * @param name the name of the statistic.
     * @return the value if it exists, Long.MIN_VALUE otherwise.
     */
    public long getLongStat(String name)
    {
        return this.longStats.getOrDefault(name, Long.MIN_VALUE);
    }

    /**
     * Obtains the value of an statistic which can be represented as a double.
     * @param name the name of the statistic.
     * @return the value if it exists, NaN otherwise.
     */
    public double getDoubleStat(String name)
    {
        return this.doubleStats.getOrDefault(name, Double.NaN);
    }

    /**
     * Obtains the list of statistics.
     * @return the list of statistics.
     */
    public List<Tuple2<String, Boolean>> statistics()
    {
        return list;
    }


}