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

import java.util.OptionalDouble;

/**
 * Computes the number of interactions (per user / item) in a dataset.
 *
 * @author Javier Sanz-Cruzado (javier.sanz-cruzado@uam.es)
 */
public class InteractionCount
{
    /**
     * The rating matrix.
     */
    private final RatingMatrix ratingMatrix;

    /**
     * Constructor.
     * @param ratingMatrix the rating matrix.
     */
    public InteractionCount(RatingMatrix ratingMatrix)
    {
        this.ratingMatrix = ratingMatrix;
    }

    /**
     * Computes the number of interactions per user.
     * @return the number of interactions per user.
     */
    public double averageCountUsers()
    {
        return (this.ratingMatrix.getNumRatings())/(this.ratingMatrix.getNumUsers()+0.0);
    }

    /**
     * Computes the number of relevant interactions per user.
     * @return the number of relevant interactions for the users.
     */
    public double averageRelCountUsers()
    {
        return (this.ratingMatrix.getNumRelRatings())/(this.ratingMatrix.getNumUsers()+0.0);
    }

    /**
     * Computes the number of interactions per item.
     * @return the number of interactions per item.
     */
    public double averageCountItems()
    {
        return (this.ratingMatrix.getNumRatings())/(this.ratingMatrix.getNumItems()+0.0);
    }

    /**
     * Computes the number of relevant interactions per item.
     * @return the number of relevant interactions per item.
     */
    public double averageRelCountItems()
    {
        return (this.ratingMatrix.getNumRelRatings())/(this.ratingMatrix.getNumItems()+0.0);
    }

    /**
     * Computes the maximum number of interactions per user.
     * @return the maximum number of interactions per user.
     */
    public double maxCountUsers()
    {
        OptionalDouble opt =  this.ratingMatrix.getUsers().mapToDouble(user -> ratingMatrix.getUserRatings(user).count() + 0.0).max();
        if(opt.isPresent()) return opt.getAsDouble();
        else return 0.0;
    }

    /**
     * Computes the maximum number of relevant interactions per user.
     * @return the maximum number of relevant interactions per user.
     */
    public double maxRelCountUsers()
    {
        OptionalDouble opt =  this.ratingMatrix.getUsers().mapToDouble(user -> ratingMatrix.getRelevantUserRatings(user).count() + 0.0).max();
        if(opt.isPresent()) return opt.getAsDouble();
        else return 0.0;
    }

    /**
     * Computes the maximum number of interactions per item.
     * @return the maximum number of interactions per items.
     */
    public double maxCountItems()
    {
        OptionalDouble opt =  this.ratingMatrix.getItems().mapToDouble(item -> ratingMatrix.getItemRatings(item).count() + 0.0).max();
        if(opt.isPresent()) return opt.getAsDouble();
        else return 0.0;
    }

    /**
     * Computes the maximum number of relevant interactions per item.
     * @return the maximum number of interactions per item.
     */
    public double maxRelCountItems()
    {
        OptionalDouble opt =  this.ratingMatrix.getItems().mapToDouble(item -> ratingMatrix.getRelevantItemRatings(item).count() + 0.0).max();
        if(opt.isPresent()) return opt.getAsDouble();
        else return 0.0;
    }

    /**
     * Computes the minimum number of interactions per user.
     * @return the minimum number of interactions per user.
     */
    public double minCountUsers()
    {
        OptionalDouble opt =  this.ratingMatrix.getUsers().mapToDouble(user -> ratingMatrix.getUserRatings(user).count() + 0.0).min();
        if(opt.isPresent()) return opt.getAsDouble();
        else return 0.0;
    }

    /**
     * Computes the minimum number of relevant interactions per user.
     * @return the minimum number of relevant interactions per user.
     */
    public double minRelCountUsers()
    {
        OptionalDouble opt =  this.ratingMatrix.getUsers().mapToDouble(user -> ratingMatrix.getRelevantUserRatings(user).count() + 0.0).min();
        if(opt.isPresent()) return opt.getAsDouble();
        else return 0.0;
    }

    /**
     * Computes the minimum number of interactions per item.
     * @return the minimum number of interactions per items.
     */
    public double minCountItems()
    {
        OptionalDouble opt =  this.ratingMatrix.getItems().mapToDouble(item -> ratingMatrix.getItemRatings(item).count() + 0.0).min();
        if(opt.isPresent()) return opt.getAsDouble();
        else return 0.0;
    }

    /**
     * Computes the minimum number of relevant interactions per item.
     * @return the minimum number of interactions per item.
     */
    public double minRelCountItems()
    {
        OptionalDouble opt =  this.ratingMatrix.getItems().mapToDouble(item -> ratingMatrix.getRelevantItemRatings(item).count() + 0.0).min();
        if(opt.isPresent()) return opt.getAsDouble();
        else return 0.0;
    }
}