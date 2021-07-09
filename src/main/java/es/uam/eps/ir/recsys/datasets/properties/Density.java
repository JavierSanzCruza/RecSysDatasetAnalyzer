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

/**
 * Finds the density of a dataset.
 *
 * @author Javier Sanz-Cruzado (javier.sanz-cruzado@uam.es)
 */
public class Density
{
    /**
     * The rating matrix.
     */
    private final RatingMatrix ratingMatrix;

    /**
     * Constructor.
     * @param ratingMatrix the rating matrix.
     */
    public Density(RatingMatrix ratingMatrix)
    {
        this.ratingMatrix = ratingMatrix;
    }

    /**
     * Computes the density (considering both relevant and non relevant ratings).
     * @return the density of the rating matrix.
     */
    public double density()
    {
        return (this.ratingMatrix.getNumRatings())/(this.ratingMatrix.getNumUsers()*this.ratingMatrix.getNumItems()+0.0);
    }

    /**
     * Computes the density (considering only relevant ratings)
     * @return the density of the rating matrix if we only had positive ratings.
     */
    public double relDensity()
    {
        return (this.ratingMatrix.getNumRelRatings())/(this.ratingMatrix.getNumUsers()*this.ratingMatrix.getNumItems()+0.0);
    }
}