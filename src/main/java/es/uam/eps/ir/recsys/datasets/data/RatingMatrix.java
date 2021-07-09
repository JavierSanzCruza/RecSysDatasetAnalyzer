/*
 * Copyright (C) 2021 Information Retrieval Group at Universidad Autónoma
 * de Madrid, http://ir.ii.uam.es.
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */
package es.uam.eps.ir.recsys.datasets.data;

import org.jooq.lambda.tuple.Tuple2;

import java.util.*;
import java.util.stream.Stream;

/**
 * Class that represents the basic rating matrix of a recommendation dataset.
 * It just includes: a) users b) items c) ratings between users and items.
 *
 * @author Javier Sanz-Cruzado (javier.sanz-cruzado@uam.es)
 */
public class RatingMatrix
{
    /**
     * The number of ratings in the system.
     */
    private int numRatings;
    /**
     * The number of relevant ratings in the system.
     */
    private int numRelRatings;

    /**
     * The total number of ratings (including repetitions) in the system.
     */
    private int numTotalRatings;
    /**
     * The total number of ratings (including repetitions) in the system.
     */
    private int numTotalRelRatings;

    /**
     * The relevance threshold of the ratings.
     */
    private final double threshold;
    /**
     * Indicates whether ratings are binarized or not. If true, when a rating is introduced, it will be binarized.
     */
    private final boolean binarize;
    /**
     * When a rating already present in the rating matrix is added, it indicates whether it is updated. In this case:
     * a) if binarize is true, it just adds (considering this as an implicit feedback matrix)
     * b) if binarize is false, we just store the higher possible value.
     */
    private final boolean update; // If we add in case it is repeated.

    /**
     * The set of users in the system.
     */
    private final Set<Integer> users;
    /**
     * The set of items in the system.
     */
    private final Set<Integer> items;

    /**
     * User-to-item rating matrix.
     */
    private final Map<Integer, Map<Integer, Double>> user2itemMatrix;
    /**
     * Item-to-user rating matrix.
     */
    private final Map<Integer, Map<Integer, Double>> item2userMatrix;

    /**
     * Constructor.
     * @param threshold the relevance threshold of the ratings.
     * @param binarize  true if we want to store the binarized ratings.
     * @param update    true if a) we want to add the number of relevant ratings to a user (when binarizing) or b) we want
     *                  to take the maximum possible value for a rating (when we do not binarize). False otherwise.
     */
    public RatingMatrix(double threshold, boolean binarize, boolean update)
    {
        // Initialize the structures:
        this.users = new HashSet<>();
        this.items = new HashSet<>();

        this.user2itemMatrix = new HashMap<>();
        this.item2userMatrix = new HashMap<>();

        this.numRatings = 0;
        this.numRelRatings = 0;
        this.threshold = threshold;
        this.binarize = binarize;
        this.update = update;
    }

    /**
     * We add a new user to the matrix.
     * @param userId the identifier of the user.
     * @return true if we add it, false otherwise (if it exists).
     */
    public boolean addUser(int userId)
    {
        if(users.contains(userId)) return false;
        users.add(userId);
        this.user2itemMatrix.put(userId, new HashMap<>());
        return true;
    }

    /**
     * We add a new item to the matrix.
     * @param itemId the identifier of the item.
     * @return true if we add it, false otherwise (if it exists).
     */
    public boolean addItem(int itemId)
    {
        if(items.contains(itemId)) return false;
        items.add(itemId);
        this.item2userMatrix.put(itemId, new HashMap<>());
        return true;
    }

    /**
     * We add a new rating to the matrix.
     * @param userId the identifier of the user.
     * @param itemId the identifier of the item.
     * @param value  the rating value
     * @return true if we add it or we update a previous case, false otherwise (if it exists).
     */
    public AddingReturn addRating(int userId, int itemId, double value)
    {
        if(users.contains(userId) && items.contains(itemId))
        {
            double oldval = user2itemMatrix.get(userId).getOrDefault(itemId, Double.NaN);
            double val =  (binarize ? (value >= threshold ? 1.0 : 0.0) : value);
            boolean rel = value >= threshold;

            numTotalRatings++;
            if(rel) numTotalRelRatings++;

            if(Double.isNaN(oldval) && !Double.isNaN(val)) // the rating does not exist: add
            {
                user2itemMatrix.get(userId).put(itemId, val);
                item2userMatrix.get(itemId).put(userId, val);
                this.numRelRatings += (rel ? 1 : 0);
                this.numRatings++;
                return AddingReturn.ADDED;
            }
            else if(!Double.isNaN(val) && (binarize && update)) // the rating already exists, and we just count the number of positives:
            {
                // Here, we do not update the number of ratings:
                boolean oldRel = (oldval > 0);
                user2itemMatrix.get(userId).put(itemId, val + oldval);
                item2userMatrix.get(userId).put(userId, val + oldval);

                if(!oldRel && rel) this.numRelRatings++;
                return AddingReturn.UPDATED;
            }
            else if(!Double.isNaN(val) && update) // In this case, we take the maximum value.
            {
                boolean oldRel = (oldval >= threshold);
                val = Math.max(oldval, val);

                if(!oldRel && rel) this.numRelRatings++;
                user2itemMatrix.get(userId).put(itemId, val);
                item2userMatrix.get(userId).put(userId, val);

                return AddingReturn.UPDATED;
            }
            else
            {
                return AddingReturn.NONE;
            }
        }

        return AddingReturn.NONE;
    }

    /**
     * Obtains the number of ratings (not repeated).
     * @return the number of ratings (not repeated).
     */
    public int getNumRatings()
    {
        return numRatings;
    }

    /**
     * Obtains the number of relevant ratings (not repeated)
     * @return the number of relevant ratings (not repeated)
     */
    public int getNumRelRatings()
    {
        return numRelRatings;
    }

    /**
     * Obtains the number of ratings (repeated).
     * @return the number of ratings (repeated).
     */
    public int getNumTotalRatings()
    {
        return numTotalRatings;
    }

    /**
     * Obtains the number of relevant ratings (repeated)
     * @return the number of relevant ratings (repeated)
     */
    public int getNumTotalRelRatings()
    {
        return numTotalRelRatings;
    }

    /**
     * Obtains the number of users in the system.
     * @return the number of users in the system.
     */
    public int getNumUsers()
    {
        return this.users.size();
    }

    /**
     * Obtains the number of items in the system.
     * @return the number of items in the system.
     */
    public int getNumItems()
    {
        return this.items.size();
    }

    /**
     * Obtains the set of users.
     * @return the set of users.
     */
    public Stream<Integer> getUsers()
    {
        return this.users.stream();
    }

    /**
     * Obtains the set of items.
     * @return the set of items.
     */
    public Stream<Integer> getItems()
    {
        return this.items.stream();
    }

    /**
     * Obtains an individual rating.
     * @param userId    the user identifier.
     * @param itemId    the item identifier.
     * @return the rating if it exists, an empty object otherwise.
     */
    public OptionalDouble getRating(int userId, int itemId)
    {
        if(user2itemMatrix.containsKey(userId) && user2itemMatrix.get(userId).containsKey(itemId))
        {
            return OptionalDouble.of(user2itemMatrix.get(userId).get(itemId));
        }
        else
            return OptionalDouble.empty();
    }

    /**
     * Obtains the ratings of a user.
     * @param userId the identifier of the user.
     * @return the ratings of the user (an empty stream if there are none, or the user does not even exist).
     */
    public Stream<Tuple2<Integer, Double>> getUserRatings(int userId)
    {
        if(!user2itemMatrix.containsKey(userId) || user2itemMatrix.get(userId).isEmpty()) return Stream.empty();
        else
        {
            return user2itemMatrix.get(userId).entrySet().stream().map(entry -> new Tuple2<>(entry.getKey(), entry.getValue()));
        }
    }

    /**
     * Obtains the ratings of a item.
     * @param itemId the identifier of the item.
     * @return the ratings of the item (an empty stream if there are none, or the item does not even exist).
     */
    public Stream<Tuple2<Integer, Double>> getItemRatings(int itemId)
    {
        if(!item2userMatrix.containsKey(itemId) || item2userMatrix.get(itemId).isEmpty()) return Stream.empty();
        else
        {
            return item2userMatrix.get(itemId).entrySet().stream().map(entry -> new Tuple2<>(entry.getKey(), entry.getValue()));
        }
    }

    /**
     * Obtains the ratings of a user.
     * @param userId the identifier of the user.
     * @return the ratings of the user (an empty stream if there are none, or the user does not even exist).
     */
    public Stream<Tuple2<Integer, Double>> getRelevantUserRatings(int userId)
    {
        if(!user2itemMatrix.containsKey(userId) || user2itemMatrix.get(userId).isEmpty()) return Stream.empty();
        else
        {
            return user2itemMatrix.get(userId).entrySet().stream().filter(entry -> entry.getValue() >= threshold).map(entry -> new Tuple2<>(entry.getKey(), entry.getValue()));
        }
    }

    /**
     * Obtains the ratings of a item.
     * @param itemId the identifier of the item.
     * @return the ratings of the item (an empty stream if there are none, or the item does not even exist).
     */
    public Stream<Tuple2<Integer, Double>> getRelevantItemRatings(int itemId)
    {
        if(!item2userMatrix.containsKey(itemId) || item2userMatrix.get(itemId).isEmpty()) return Stream.empty();
        else
        {
            return item2userMatrix.get(itemId).entrySet().stream().filter(entry -> entry.getValue() >= threshold).map(entry -> new Tuple2<>(entry.getKey(), entry.getValue()));
        }
    }
}