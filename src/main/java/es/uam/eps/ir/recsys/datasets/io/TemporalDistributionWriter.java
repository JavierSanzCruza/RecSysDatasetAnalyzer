/*
 * Copyright (C) 2021 Information Retrieval Group at Universidad Autónoma
 * de Madrid, http://ir.ii.uam.es.
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */
package es.uam.eps.ir.recsys.datasets.io;

import es.uam.eps.ir.recsys.datasets.properties.TemporalDistribution;
import org.jooq.lambda.tuple.Tuple2;

import java.io.BufferedWriter;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.List;

/**
 * Writes the temporal distribution of a dataset.
 *
 * @author Javier Sanz-Cruzado (javier.sanz-cruzado@uam.es)
 */
public class TemporalDistributionWriter
{
    /**
     * Writes the temporal distribution of the dataset (per item).
     * @param stats     the temporal distribution of the dataset.
     * @param file      the file in which to store the popularity distribution.
     * @throws IOException if something fails while writing the popularity distribution.
     */
    public void writeItemDistribution(TemporalDistribution stats, String file) throws IOException
    {
        List<Tuple2<Integer, Long>> distrib = stats.getItemDistribution();
        writeDistribution(file, distrib);
    }

    /**
     * Writes the temporal distribution of the dataset (per user).
     * @param stats     the temporal distribution of the dataset.
     * @param file      the file in which to store the popularity distribution.
     * @throws IOException if something fails while writing the popularity distribution.
     */
    public void writeUserDistribution(TemporalDistribution stats, String file) throws IOException
    {
        List<Tuple2<Integer, Long>> distrib = stats.getUserDistribution();
        writeDistribution(file, distrib);
    }

    /**
     * Writes the popularity distribution.
     * @param file      the file in which to store it.
     * @param distrib   the distribution.
     * @throws IOException if something fails while writing
     */
    private void writeDistribution(String file, List<Tuple2<Integer, Long>> distrib) throws IOException
    {
        try(BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file))))
        {
            bw.write("Timestamp\tItemId");
            int i = 0;
            for(Tuple2<Integer, Long> val : distrib)
            {
                bw.write("\n" + val.v1 + "\t" + val.v2);
            }
        }
    }
}