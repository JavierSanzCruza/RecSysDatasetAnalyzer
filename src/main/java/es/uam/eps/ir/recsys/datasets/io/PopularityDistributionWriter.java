/*
 * Copyright (C) 2021 Information Retrieval Group at Universidad Autónoma
 * de Madrid, http://ir.ii.uam.es.
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */
package es.uam.eps.ir.recsys.datasets.io;

import es.uam.eps.ir.recsys.datasets.properties.PopularityDistribution;

import java.io.BufferedWriter;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.List;

/**
 * Writes the popularity distribution of a dataset.
 *
 * @author Javier Sanz-Cruzado (javier.sanz-cruzado@uam.es)
 */
public class PopularityDistributionWriter
{
    /**
     * Writes the popularity distribution of a dataset (by items)
     * @param stats     the popularity distribution of the dataset.
     * @param file      the file in which to store the popularity distribution.
     * @throws IOException if something fails while writing the popularity distribution.
     */
    public void writeItemDistribution(PopularityDistribution stats, String file) throws IOException
    {
        try(BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file))))
        {
            bw.write("Item Id\tNum. Ratings");
            List<Long> distrib = stats.getItemDistribution();
            int i = 0;
            for(long val : distrib)
            {
                bw.write("\n" + i + "\t" + val);
            }
        }
    }

    /**
     * Writes the popularity distribution of a dataset, taking relevance into account (by items).
     * @param stats     the popularity distribution of the dataset.
     * @param file      the file in which to store the popularity distribution.
     * @throws IOException if something fails while writing the popularity distribution.
     */
    public void writeRelevantItemDistribution(PopularityDistribution stats, String file) throws IOException
    {
        try(BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file))))
        {
            bw.write("Item Id\tNum. Ratings");
            List<Long> distrib = stats.getRelevantItemDistribution();
            int i = 0;
            for(long val : distrib)
            {
                bw.write("\n" + i + "\t" + val);
            }
        }
    }

    /**
     * Writes the popularity distribution of a dataset (by users).
     * @param stats     the popularity distribution of the dataset.
     * @param file      the file in which to store the popularity distribution.
     * @throws IOException if something fails while writing the popularity distribution.
     */
    public void writeUserDistribution(PopularityDistribution stats, String file) throws IOException
    {
        try(BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file))))
        {
            bw.write("Item Id\tNum. Ratings");
            List<Long> distrib = stats.getUserDistribution();
            int i = 0;
            for(long val : distrib)
            {
                bw.write("\n" + i + "\t" + val);
            }
        }
    }

    /**
     * Writes the popularity distribution of a dataset, taking relevance into account (by users).
     * @param stats     the popularity distribution of the dataset.
     * @param file      the file in which to store the popularity distribution.
     * @throws IOException if something fails while writing the popularity distribution.
     */
    public void writeRelevantUserDistribution(PopularityDistribution stats, String file) throws IOException
    {
        try(BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file))))
        {
            bw.write("Item Id\tNum. Ratings");
            List<Long> distrib = stats.getRelevantUserDistribution();
            int i = 0;
            for(long val : distrib)
            {
                bw.write("\n" + i + "\t" + val);
            }
        }
    }
}