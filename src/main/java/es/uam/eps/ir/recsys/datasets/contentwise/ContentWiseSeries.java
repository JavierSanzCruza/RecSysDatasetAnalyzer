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
 * Full description of a series in the ContentWise Impressions dataset
 */
public class ContentWiseSeries
{
    /**
     * The identifier of the series.
     */
    private final int seriesId;
    /**
     * The length of the series (in episodes).
     */
    private final int length;

    /**
     * Constructor.
     * @param seriesId  the identifier of the series.
     * @param length    the length of the series (in episodes).
     */
    public ContentWiseSeries(int seriesId, int length)
    {
        this.seriesId = seriesId;
        this.length = length;
    }

    public int getSeriesId()
    {
        return seriesId;
    }

    public int getLength()
    {
        return length;
    }
}