package es.uam.eps.ir.recsys.datasets;

import es.uam.eps.ir.recsys.datasets.contentwise.ContentWiseDataset;
import es.uam.eps.ir.recsys.datasets.contentwise.ContentWiseImpressionStatistics;
import es.uam.eps.ir.recsys.datasets.io.ImpressionDistributionWriter;
import es.uam.eps.ir.recsys.datasets.io.PopularityDistributionWriter;
import es.uam.eps.ir.recsys.datasets.io.StatisticsWriter;
import es.uam.eps.ir.recsys.datasets.io.TemporalDistributionWriter;
import es.uam.eps.ir.recsys.datasets.properties.ImpressionDistribution;
import es.uam.eps.ir.recsys.datasets.properties.PopularityDistribution;
import es.uam.eps.ir.recsys.datasets.properties.TemporalDistribution;

import java.io.IOException;

/**
 * Class for analyzing different types of datasets.
 *
 * @author Javier Sanz-Cruzado (javier.sanz-cruzado@uam.es)
 */
public class Analyzer
{
    private final static String CONTENTWISE = "ContentWise";
    public static void main(String[] args) throws IOException
    {
        // ContentWise impressions:

        switch (args[0])
        {
            case CONTENTWISE ->
            {
                long timea = System.currentTimeMillis();

                String inter = args[1];
                String imprDirect = args[2];
                String imprNoDirect = args[3];

                ContentWiseDataset dataset = ContentWiseDataset.load(inter, imprDirect, imprNoDirect);

                long timeb = System.currentTimeMillis();
                System.err.println("Data read (" + (timeb - timea) + "ms.)");

                // Print and find the impressions:
                ContentWiseImpressionStatistics stats = new ContentWiseImpressionStatistics(dataset);
                StatisticsWriter writer = new StatisticsWriter();

                writer.write(stats, args[4] + "stats.txt");

                timeb = System.currentTimeMillis();
                System.err.println("Stats computed (" + (timeb - timea) + " ms.)");

                // Now, we do print the popularity distributions:
                PopularityDistributionWriter popWriter = new PopularityDistributionWriter();
                // a) Popularity distribution for user-item interactions
                PopularityDistribution pop = new PopularityDistribution(dataset.getUser2ItemInteractions());
                popWriter.writeItemDistribution(pop, args[4] + "pop-user-item.txt");
                // b) Popularity distribution for user-series interactions
                pop = new PopularityDistribution(dataset.getUser2SeriesInteractions());
                popWriter.writeItemDistribution(pop, args[4] + "pop-user-series.txt");
                // c) Popularity distribution for user-item interactions (with impressions)
                pop = new PopularityDistribution(dataset.getUser2ItemInteractionsFromImpressions());
                popWriter.writeItemDistribution(pop, args[4] + "pop-user-item-impr.txt");
                // d) Popularity distribution for user-series interactions (with impressions)
                pop = new PopularityDistribution(dataset.getUser2SeriesInteractionsFromImpressions());
                popWriter.writeItemDistribution(pop, args[4] + "pop-user-series-impr.txt");

                timeb = System.currentTimeMillis();
                System.err.println("Popularity distributions computed (" + (timeb - timea) + " ms.)");

                // Now, we do print the distributions for the impressions (number of points / ..)
                ImpressionDistributionWriter imprWriter = new ImpressionDistributionWriter();
                ImpressionDistribution impr = new ImpressionDistribution(dataset.getImpressions());
                imprWriter.writeUserDistribution(impr, "impr-user.txt");
                imprWriter.writeItemDistribution(impr, "impr-item.txt");

                timeb = System.currentTimeMillis();
                System.err.println("Impression distributions computed (" + (timeb - timea) + " ms.)");

                // and the distribution of timestamps:
                TemporalDistributionWriter tempWriter = new TemporalDistributionWriter();
                // a) For the users:
                TemporalDistribution temp = dataset.getUser2ItemTemporalDistrib();
                tempWriter.writeUserDistribution(temp, args[4] + "time-users.txt", true);
                tempWriter.writeItemDistribution(temp, args[4] + "time-items.txt", true);
                temp = dataset.getUser2SeriesTemporalDistrib();
                tempWriter.writeItemDistribution(temp, args[4] + "time-series.txt", true);

                temp = dataset.getUser2ItemWithImpressionsTemporalDistrib();
                tempWriter.writeUserDistribution(temp, args[4] + "time-users-impressions.txt", true);
                tempWriter.writeItemDistribution(temp, args[4] + "time-items-impressions.txt", true);
                temp = dataset.getUser2SeriesWithImpressionsTemporalDistrib();
                tempWriter.writeItemDistribution(temp, args[4] + "time-series-impressions.txt", true);


                temp = dataset.getUser2ItemTemporalDistrib();
                tempWriter.writeUserDistribution(temp, args[4] + "time-users-inv.txt", false);
                tempWriter.writeItemDistribution(temp, args[4] + "time-items-inv.txt", false);
                temp = dataset.getUser2SeriesTemporalDistrib();
                tempWriter.writeItemDistribution(temp, args[4] + "time-series-inv.txt", false);

                temp = dataset.getUser2ItemWithImpressionsTemporalDistrib();
                tempWriter.writeUserDistribution(temp, args[4] + "time-users-impressions-inv.txt", false);
                tempWriter.writeItemDistribution(temp, args[4] + "time-items-impressions-inv.txt", false);
                temp = dataset.getUser2SeriesWithImpressionsTemporalDistrib();
                tempWriter.writeItemDistribution(temp, args[4] + "time-series-impressions-inv.txt", false);


                timeb = System.currentTimeMillis();
                System.err.println("Temporal distributions computed (" + (timeb - timea) + " ms.)");
            }
            default ->
            {
                System.err.println("ERROR: The dataset you are trying to analyze is not correct.");
            }
        }
    }
}