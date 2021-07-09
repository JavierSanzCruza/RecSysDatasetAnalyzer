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

import java.util.*;

/**
 * Class for computing and storing the popularity distribution of a dataset. It obtains a list containing the number of ratings
 * per item (it just stores these numbers, sorted from larger to smaller).
 *
 * @author Javier Sanz-Cruzado (javier.sanz-cruzado@uam.es)
 */
public class PopularityDistribution
{
    /**
     * The rating matrix.
     */
    private final RatingMatrix ratingMatrix;

    /**
     * Constructor. Finds the probability distribution of a dataset.
     * @param ratingMatrix  the rating matrix of the dataset.
     */
    public PopularityDistribution(RatingMatrix ratingMatrix)
    {
        this.ratingMatrix = ratingMatrix;
    }

    /**
     * Obtains the distribution list. To prevent modifying the original list,
     * it just returns a proxy.
     * @return the list containing the distribution.
     */
    public List<Long> getUserDistribution()
    {
        List<Long> distribution = new ArrayList<>();
        ratingMatrix.getUsers().forEach(user -> distribution.add(ratingMatrix.getUserRatings(user).count()));
        distribution.sort(Comparator.reverseOrder());
        return new ArrayList<>(distribution);
    }

    /**
     * Obtains the distribution list. To prevent modifying the original list,
     * it just returns a proxy.
     * @return the list containing the distribution.
     */
    public List<Long> getRelevantUserDistribution()
    {
        List<Long> distribution = new ArrayList<>();
        ratingMatrix.getUsers().forEach(user -> distribution.add(ratingMatrix.getRelevantUserRatings(user).count()));
        distribution.sort(Comparator.reverseOrder());
        return new ArrayList<>(distribution);
    }

    /**
     * Obtains the distribution list. To prevent modifying the original list,
     * it just returns a proxy.
     * @return the list containing the distribution.
     */
    public List<Long> getItemDistribution()
    {
        List<Long> distribution = new ArrayList<>();
        ratingMatrix.getItems().forEach(item -> distribution.add(ratingMatrix.getItemRatings(item).count()));
        distribution.sort(Comparator.reverseOrder());
        return new ArrayList<>(distribution);
    }

    /**
     * Obtains the distribution list. To prevent modifying the original list,
     * it just returns a proxy.
     * @return the list containing the distribution.
     */
    public List<Long> getRelevantItemDistribution()
    {
        List<Long> distribution = new ArrayList<>();
        ratingMatrix.getItems().forEach(item -> distribution.add(ratingMatrix.getRelevantItemRatings(item).count()));
        distribution.sort(Comparator.reverseOrder());
        return new ArrayList<>(distribution);
    }
}