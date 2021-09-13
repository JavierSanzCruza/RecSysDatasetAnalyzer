/*
 * Copyright (C) 2021 Information Retrieval Group at Universidad Autónoma
 * de Madrid, http://ir.ii.uam.es.
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */
package es.uam.eps.ir.recsys.datasets.data;

import java.util.*;
import java.util.stream.Stream;

/**
 * Class that represents the basic rating matrix of a recommendation dataset.
 * It just includes: a) users b) items c) ratings between users and items.
 *
 * @author Javier Sanz-Cruzado (javier.sanz-cruzado@uam.es)
 */
public class Impressions
{
    /**
     * The number of ratings in the system.
     */
    private int numImpressions;

    /**
     * User-to-item rating matrix.
     */
    private final Map<Integer, Set<Integer>> userImpressions;
    /**
     * Item-to-user rating matrix.
     */
    private final Map<Integer, Set<Integer>> itemImpressions;

    /**
     * Constructor.
     */
    public Impressions()
    {
        // Initialize the structures:
        this.userImpressions = new HashMap<>();
        this.itemImpressions = new HashMap<>();
    }

    /**
     * We add a new user to the matrix.
     * @param userId the identifier of the user.
     * @return true if we add it, false otherwise (if it exists).
     */
    public boolean addUser(int userId)
    {
        if(userImpressions.containsKey(userId)) return false;
        this.userImpressions.put(userId, new HashSet<>());
        return true;
    }

    /**
     * We add a new item to the matrix.
     * @param itemId the identifier of the item.
     * @return true if we add it, false otherwise (if it exists).
     */
    public boolean addItem(int itemId)
    {
        if(itemImpressions.containsKey(itemId)) return false;
        this.itemImpressions.put(itemId, new HashSet<>());
        return true;
    }

    /**
     * We add a new impression to the matrix.
     * @param userId the identifier of the user.
     * @param itemId the identifier of the item.
     * @return true if we add it or we update a previous case, false otherwise (if it exists).
     */
    public AddingReturn addImpression(int userId, int itemId)
    {
        if(userImpressions.containsKey(userId) && itemImpressions.containsKey(itemId))
        {
            if (userImpressions.get(userId).contains(itemId))
            {
                return AddingReturn.NONE;
            }
            else
            {
                userImpressions.get(userId).add(itemId);
                itemImpressions.get(itemId).add(userId);
                numImpressions++;
                return AddingReturn.ADDED;
            }
        }

        return AddingReturn.NONE;
    }

    /**
     * Obtains the set of users.
     * @return the set of users.
     */
    public Stream<Integer> getUsers()
    {
        return this.userImpressions.keySet().stream();
    }

    /**
     * Obtains the set of items.
     * @return the set of items.
     */
    public Stream<Integer> getItems()
    {
        return this.itemImpressions.keySet().stream();
    }

    /**
     * Obtains the impressions of a user.
     * @param userId the identifier of the user.
     * @return the impressions of the user (an empty stream if there are none, or the user does not even exist).
     */
    public Stream<Integer> getUserImpressions(int userId)
    {
        if(!userImpressions.containsKey(userId)) return Stream.empty();
        return userImpressions.get(userId).stream();
    }

    /**
     * Obtains the ratings of a item.
     * @param itemId the identifier of the item.
     * @return the ratings of the item (an empty stream if there are none, or the item does not even exist).
     */
    public Stream<Integer> getItemImpressions(int itemId)
    {
        if(!itemImpressions.containsKey(itemId)) return Stream.empty();
        return itemImpressions.get(itemId).stream();
    }

    /**
     * Obtains the number of impressions.
     * @return the number of impressions.
     */
    public int getNumImpressions()
    {
        return this.numImpressions;
    }

    public int getNumUsers()
    {
        return this.userImpressions.size();
    }

    public int getNumItems()
    {
        return this.itemImpressions.size();
    }
}