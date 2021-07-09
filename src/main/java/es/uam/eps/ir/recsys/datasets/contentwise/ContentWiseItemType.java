/*
 * Copyright (C) 2021 Information Retrieval Group at Universidad Autónoma
 * de Madrid, http://ir.ii.uam.es.
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */
package es.uam.eps.ir.recsys.datasets.contentwise;

/**
 * Type of items in the ContentWise Impressions dataset.
 *
 * @author Javier Sanz-Cruzado (javier.sanz-cruzado@uam.es)
 */
public enum ContentWiseItemType
{
    MOVIES, MOVIES_CLIPS, TV_MOVIES, TV_SERIES;

    /**
     * Obtains the type of item from its value on the original dataset.
     * @param val the value in the original dataset.
     * @return the type of item, null if it is incorrect.
     */
    public static ContentWiseItemType from(int val)
    {
        if(val == 0) return MOVIES;
        else if(val == 1) return MOVIES_CLIPS;
        else if(val == 2) return TV_MOVIES;
        else if(val == 3) return TV_SERIES;
        return null;
    }
}