/*
 * Copyright (C) 2021 Information Retrieval Group at Universidad Autónoma
 * de Madrid, http://ir.ii.uam.es.
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */
package es.uam.eps.ir.recsys.datasets.properties;

import es.uam.eps.ir.recsys.datasets.data.RatingMatrix;

import java.util.List;

/**
 * Finds the Gini index of the items in a dataset.
 */
public class GiniIndex
{
    /**
     * The rating matrix.
     */
    private final RatingMatrix ratingMatrix;

    /**
     * The Gini index of the items in a dataset.
     * @param ratingMatrix the rating matrix.
     */
    public GiniIndex(RatingMatrix ratingMatrix)
    {
        this.ratingMatrix = ratingMatrix;
    }

    /**
     * Finds the Gini index of the users.
     * @return the Gini index of the users.
     */
    public double userGini()
    {
        PopularityDistribution popularityDistribution = new PopularityDistribution(ratingMatrix);
        List<Long> pops = popularityDistribution.getUserDistribution();
        return computeGini(pops);
    }

    /**
     * Finds the Gini index of the items (only considers relevant ratings).
     * @return the Gini index of the items.
     */
    public double userRelGini()
    {
        PopularityDistribution popularityDistribution = new PopularityDistribution(ratingMatrix);
        List<Long> pops = popularityDistribution.getRelevantUserDistribution();
        return computeGini(pops);
    }

    /**
     * Finds the Gini index of the items.
     * @return the Gini index of the items.
     */
    public double itemGini()
    {
        PopularityDistribution popularityDistribution = new PopularityDistribution(ratingMatrix);
        List<Long> pops = popularityDistribution.getItemDistribution();
        return computeGini(pops);
    }

    /**
     * Finds the Gini index of the items (only considers relevant ratings).
     * @return the Gini index of the items.
     */
    public double itemRelGini()
    {
        PopularityDistribution popularityDistribution = new PopularityDistribution(ratingMatrix);
        List<Long> pops = popularityDistribution.getRelevantItemDistribution();
        return computeGini(pops);
    }

    /**
     * Computes the Gini index.
     * @param pops the list of popularity values.
     * @return the value of the Gini index.
     */
    public double computeGini(List<Long> pops)
    {
        double gini = 0.0;
        int size = pops.size();
        double sum = pops.stream().mapToDouble(x -> x).sum();
        for(int i = 0; i < pops.size(); ++i)
        {
            double val = (2.0*(size-i) - size - 1.0)*pops.get(i);
            val /= sum;
            gini += val;
        }

        return gini / (size - 1.0);
    }
}