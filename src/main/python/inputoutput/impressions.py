from src.main.python.properties.distributions.impression_distribution import ImpressionsDistribution


class ImpressionDistributionWriter:

    @staticmethod
    def write_item_distribution(impressions: ImpressionsDistribution,
                                file: str):
        f = open(file, "w")
        f.write("Item.Id\tNum.Impressions")
        distribution = impressions.get_item_distribution()
        i = 0
        for val in distribution:
            f.write("\n" + str(i) + "\t" + val)
            i += 1
        f.close()

    @staticmethod
    def write_user_distribution(impressions: ImpressionsDistribution,
                                file: str):
        f = open(file, "w")
        f.write("User.Id\tNum.Impressions")
        distribution = impressions.get_user_distribution()
        i = 0
        for val in distribution:
            f.write("\n" + str(i) + "\t" + val)
            i += 1
        f.close()
