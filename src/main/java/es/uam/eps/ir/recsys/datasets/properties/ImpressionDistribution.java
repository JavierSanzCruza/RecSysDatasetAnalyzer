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

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 * Class for computing and storing the popularity distribution of a dataset. It obtains a list containing the number of ratings
 * per item (it just stores these numbers, sorted from larger to smaller).
 *
 * @author Javier Sanz-Cruzado (javier.sanz-cruzado@uam.es)
 */
public class ImpressionDistribution
{
    /**
     * The rating matrix.
     */
    private final Impressions impressions;

    /**
     * Constructor. Finds the probability distribution of a dataset.
     * @param impressions  the rating matrix of the dataset.
     */
    public ImpressionDistribution(Impressions impressions)
    {
        this.impressions = impressions;
    }

    /**
     * Obtains the distribution list. To prevent modifying the original list,
     * it just returns a proxy.
     * @return the list containing the distribution.
     */
    public List<Long> getUserDistribution()
    {
        List<Long> distribution = new ArrayList<>();
        impressions.getUsers().forEach(user -> distribution.add(impressions.getUserImpressions(user).count()));
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
        impressions.getItems().forEach(item -> distribution.add(impressions.getItemImpressions(item).count()));
        distribution.sort(Comparator.reverseOrder());
        return new ArrayList<>(distribution);
    }
}