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
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

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
    public void writeItemDistribution(TemporalDistribution stats, String file, boolean byFirst) throws IOException
    {
        List<Tuple2<Integer, Long>> distrib = stats.getItemDistribution();
        writeDistribution(file, distrib, byFirst);
    }

    /**
     * Writes the temporal distribution of the dataset (per user).
     * @param stats     the temporal distribution of the dataset.
     * @param file      the file in which to store the popularity distribution.
     * @throws IOException if something fails while writing the popularity distribution.
     */
    public void writeUserDistribution(TemporalDistribution stats, String file, boolean byFirst) throws IOException
    {
        List<Tuple2<Integer, Long>> distrib = stats.getUserDistribution();
        writeDistribution(file, distrib, byFirst);
    }

    /**
     * Writes the popularity distribution.
     * @param file      the file in which to store it.
     * @param distrib   the distribution.
     * @param byFirst   sorts the elements by the first timestamp if true, by the last if false.
     * @throws IOException if something fails while writing
     */
    private void writeDistribution(String file, List<Tuple2<Integer, Long>> distrib, boolean byFirst) throws IOException
    {
        Map<Integer, Integer> transform = new HashMap<>();

        try(BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file))))
        {
            bw.write("Id\tTimestamp");
            if(byFirst)
            {
                for (Tuple2<Integer, Long> val : distrib)
                {
                    if (!transform.containsKey(val.v1))
                    {
                        transform.put(val.v1, transform.size());
                    }
                    bw.write("\n" + transform.get(val.v1) + "\t" + val.v2);
                }
            }
            else
            {
                for(int i = distrib.size()-1; i >= 0; --i)
                {
                    Tuple2<Integer, Long> val = distrib.get(i);
                    if (!transform.containsKey(val.v1))
                    {
                        transform.put(val.v1, transform.size());
                    }
                    bw.write("\n" + transform.get(val.v1) + "\t" + val.v2);
                }
            }
        }
    }
}