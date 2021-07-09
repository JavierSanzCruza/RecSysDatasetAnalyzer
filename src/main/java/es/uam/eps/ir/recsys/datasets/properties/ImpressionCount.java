/*
 * Copyright (C) 2021 Information Retrieval Group at Universidad Autónoma
 * de Madrid, http://ir.ii.uam.es.
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */
package es.uam.eps.ir.recsys.datasets.properties;

import es.uam.eps.ir.recsys.datasets.data.Impressions;

import java.util.OptionalDouble;

/**
 * Computes the average number of impressions (per user / item) in a dataset.
 *
 * @author Javier Sanz-Cruzado (javier.sanz-cruzado@uam.es)
 */
public class ImpressionCount
{
    /**
     * The set of impressions.
     */
    private final Impressions impressions;

    /**
     * Constructor.
     * @param impressions the set of impressions.
     */
    public ImpressionCount(Impressions impressions)
    {
        this.impressions = impressions;
    }

    /**
     * Computes the average number of impressions per user.
     * @return the average number of impressions per user.
     */
    public double averageCountUsers()
    {
        return (this.impressions.getNumImpressions())/(this.impressions.getNumUsers()+0.0);
    }

    /**
     * Computes the average number of impressions per item.
     * @return the average number of impressions per item.
     */
    public double averageCountItems()
    {
        return (this.impressions.getNumImpressions())/(this.impressions.getNumItems()+0.0);
    }

    /**
     * Computes the maximum number of impressions per user.
     * @return the maximum number of impressions per user.
     */
    public double maxCountUsers()
    {
        OptionalDouble opt =  this.impressions.getUsers().mapToDouble(user -> impressions.getUserImpressions(user).count() + 0.0).max();
        if(opt.isPresent()) return opt.getAsDouble();
        else return 0.0;
    }

    /**
     * Computes the minimum number of impressions per user.
     * @return the minimum number of impressions per user.
     */
    public double minCountUsers()
    {
        OptionalDouble opt =  this.impressions.getUsers().mapToDouble(user -> impressions.getUserImpressions(user).count() + 0.0).min();
        if(opt.isPresent()) return opt.getAsDouble();
        else return 0.0;
    }

    /**
     * Computes the maximum number of impressions per item.
     * @return the maximum number of impressions per item.
     */
    public double maxCountItems()
    {
        OptionalDouble opt =  this.impressions.getItems().mapToDouble(item -> impressions.getItemImpressions(item).count() + 0.0).max();
        if(opt.isPresent()) return opt.getAsDouble();
        else return 0.0;
    }

    /**
     * Computes the minimum number of impressions per item.
     * @return the minimum number of impressions per item.
     */
    public double minCountItems()
    {
        OptionalDouble opt =  this.impressions.getItems().mapToDouble(item -> impressions.getItemImpressions(item).count() + 0.0).min();
        if(opt.isPresent()) return opt.getAsDouble();
        else return 0.0;
    }
}