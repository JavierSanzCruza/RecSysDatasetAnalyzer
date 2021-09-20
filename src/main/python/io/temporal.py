from src.main.python.properties.distributions.popularity_distribution import PopularityDistribution
from src.main.python.properties.distributions.temporal_distribution import TemporalDistribution


class TemporalDistributionWriter:
    @staticmethod
    def write_user_distribution(pop: TemporalDistribution,
                                file: str,
                                natural_order: bool = True):

        TemporalDistributionWriter.write_distribution(pop.get_user_distribution(), file, natural_order=natural_order)

    @staticmethod
    def write_item_distribution(pop: TemporalDistribution,
                                file: str,
                                natural_order: bool = True):
        TemporalDistributionWriter.write_distribution(pop.get_item_distribution(), file, natural_order=natural_order)

    @staticmethod
    def write_distribution(distribution: list,
                           file: str,
                           natural_order: bool = True):

        transform = dict()
        f = open(file, "w")
        f.write("Id\ttimestamp")
        if natural_order:
            for item, timestamp in distribution:
                if not transform.__contains__(item):
                    transform[item] = len(transform)
                f.write("\n" + str(transform.get(item)) + "\t" + str(timestamp))
        else:
            for i in range(len(distribution) - 1, 0, -1):
                item, timestamp = distribution[i]
                if not transform.__contains__(item):
                    transform[item] = len(transform)
                f.write("\n" + str(transform.get(item)) + "\t" + str(timestamp))
        f.close()
