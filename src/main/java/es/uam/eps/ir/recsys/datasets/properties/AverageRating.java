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

import java.util.HashMap;
import java.util.Map;
import java.util.OptionalDouble;

/**
 * Finds the average rating value of a dataset.
 *
 * @author Javier Sanz-Cruzado (javier.sanz-cruzado@uam.es)
 */
public class AverageRating
{
    /**
     * The rating matrix.
     */
    private final RatingMatrix ratingMatrix;

    /**
     * Constructor.
     * @param ratingMatrix the rating matrix.
     */
    public AverageRating(RatingMatrix ratingMatrix)
    {
        this.ratingMatrix = ratingMatrix;
    }

    /**
     * Finds the average rating of the dataset.
     * @return the average rating of the dataset.
     */
    public double averageRating()
    {
        return ratingMatrix.getUsers().mapToDouble(userId -> ratingMatrix.getUserRatings(userId).mapToDouble(r -> r.v2/(ratingMatrix.getNumRatings() + 0.0)).sum()).sum();
    }

    /**
     * Finds the average rating for each user.
     * @return a map containing the average rating of all the users.
     */
    public Map<Integer, Double> averageRatingUsers()
    {
        Map<Integer, Double> averages = new HashMap<>();
        ratingMatrix.getUsers().forEach(userId ->
        {
            OptionalDouble opt = ratingMatrix.getUserRatings(userId).mapToDouble(r -> r.v2).average();
            averages.put(userId, (opt.isPresent() ? opt.getAsDouble() : 0.0));
        });

        return averages;
    }

    /**
     * Finds the average rating for each user.
     * @return a map containing the average rating of all the items.
     */
    public Map<Integer, Double> averageRatingItems()
    {
        Map<Integer, Double> averages = new HashMap<>();
        ratingMatrix.getItems().forEach(itemId ->
        {
            OptionalDouble opt = ratingMatrix.getItemRatings(itemId).mapToDouble(r -> r.v2).average();
            averages.put(itemId, (opt.isPresent() ? opt.getAsDouble() : 0.0));
        });

        return averages;
    }

    /**
     * Finds the average rating for an individual user.
     * @param userId the user.
     * @return the average rating for the individual user.
     */
    public double averageRatingUser(int userId)
    {
        OptionalDouble opt = ratingMatrix.getUserRatings(userId).mapToDouble(r -> r.v2).average();
        return opt.isPresent() ? opt.getAsDouble() : 0.0;
    }

    /**
     * Finds the average rating for an individual item.
     * @param itemId the item.
     * @return the average rating for the individual item.
     */
    public double averageRatingItem(int itemId)
    {
        OptionalDouble opt = ratingMatrix.getItemRatings(itemId).mapToDouble(r -> r.v2).average();
        return opt.isPresent() ? opt.getAsDouble() : 0.0;
    }
}