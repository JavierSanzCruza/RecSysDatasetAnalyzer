/*
 * Copyright (C) 2021 Information Retrieval Group at Universidad Autónoma
 * de Madrid, http://ir.ii.uam.es.
 *
 * This Source Code Form is subject to the terms of the Mozilla Public
 * License, v. 2.0. If a copy of the MPL was not distributed with this
 * file, You can obtain one at http://mozilla.org/MPL/2.0/.
 */
package es.uam.eps.ir.recsys.datasets.io;

import es.uam.eps.ir.recsys.datasets.Statistics;
import org.jooq.lambda.tuple.Tuple2;

import java.io.BufferedWriter;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.util.List;

/**
 * Writes the statistics of a dataset.
 *
 * @author Javier Sanz-Cruzado (javier.sanz-cruzado@uam.es)
 */
public class StatisticsWriter
{
    /**
     * Writes the statistics of the dataset into a file.
     * @param stats the statistics to write.
     * @param file  the file in which to write the statistics.
     * @throws IOException  if something fails while writing the file.
     */
    public void write(Statistics stats, String file) throws IOException
    {
        List<Tuple2<String, Boolean>> statistics = stats.statistics();
        try(BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(file))))
        {
            bw.write("Stat\tValue");
            for(Tuple2<String, Boolean> indiv : statistics)
            {
                bw.write("\n" + indiv.v1);
                if(indiv.v2)
                {
                    bw.write("\t" + stats.getDoubleStat(indiv.v1));
                }
                else
                {
                    bw.write("\t" + stats.getLongStat(indiv.v1));
                }
            }
        }
    }
}