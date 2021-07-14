/*
 * Copyright (C) 2021 Information Retrieval Group at Universidad Autónoma
 * de Madrid, http://ir.ii.uam.es.
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */
package es.uam.eps.ir.recsys.datasets.io;

import es.uam.eps.ir.recsys.datasets.properties.ImpressionDistribution;

import java.io.BufferedWriter;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.List;

/**
 * Writes the impression distribution of a dataset.
 *
 * @author Javier Sanz-Cruzado (javier.sanz-cruzado@uam.es)
 */
public class ImpressionDistributionWriter
{
    /**
     * Writes the impression distribution of a dataset (by items)
     * @param stats     the impression distribution of the dataset.
     * @param file      the file in which to store the popularity distribution.
     * @throws IOException if something fails while writing the popularity distribution.
     */
    public void writeItemDistribution(ImpressionDistribution stats, String file) throws IOException
    {
        try(BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file))))
        {
            bw.write("Item Id\tNum. Impressions");
            List<Long> distrib = stats.getItemDistribution();
            int i = 0;
            for(long val : distrib)
            {
                bw.write("\n" + i + "\t" + val);
                ++i;
            }
        }
    }

    /**
     * Writes the impression distribution of a dataset (by users).
     * @param stats     the impression distribution of the dataset.
     * @param file      the file in which to store the popularity distribution.
     * @throws IOException if something fails while writing the popularity distribution.
     */
    public void writeUserDistribution(ImpressionDistribution stats, String file) throws IOException
    {
        try(BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file))))
        {
            bw.write("User Id\tNum. Impressions");
            List<Long> distrib = stats.getUserDistribution();
            int i = 0;
            for(long val : distrib)
            {
                bw.write("\n" + i + "\t" + val);
                ++i;
            }
        }
    }
}