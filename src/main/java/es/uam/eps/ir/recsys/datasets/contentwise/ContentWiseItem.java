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
 * Full information about a single item in the ContentWise Impressions dataset.
 */
public class ContentWiseItem
{
    /**
     * Identifier of the item.
     */
    private final int itemId;
    /**
     * Identifier of the series.
     */
    private final int seriesId;
    /**
     * Episode number.
     */
    private final int episodeNumber;
    /**
     * Item type.
     */
    private final ContentWiseItemType type;

    /**
     * Constructor.
     * @param itemId            identifier of the item.
     * @param seriesId          identifier of the series.
     * @param episodeNumber     episode number.
     * @param type              type of the item.
     */
    public ContentWiseItem(int itemId, int seriesId, int episodeNumber, ContentWiseItemType type)
    {
        this.itemId = itemId;
        this.seriesId = seriesId;
        this.episodeNumber = episodeNumber;
        this.type = type;
    }

    /**
     * Obtains the identifier of the item.
     * @return the identifier of the item.
     */
    public int getItemId()
    {
        return itemId;
    }

    /**
     * Obtains the identifier of the series.
     * @return the identifier of the series.
     */
    public int getSeriesId()
    {
        return seriesId;
    }

    /**
     * Obtains the episode number.
     * @return the episode number.
     */
    public int getEpisodeNumber()
    {
        return episodeNumber;
    }

    /**
     * Obtains the type of the item.
     * @return the type of the item.
     */
    public ContentWiseItemType getType()
    {
        return type;
    }
}