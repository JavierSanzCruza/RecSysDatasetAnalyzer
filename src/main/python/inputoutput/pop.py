from src.main.python.properties.distributions.popularity_distribution import PopularityDistribution


class PopularityDistributionWriter:
    @staticmethod
    def write(pop: PopularityDistribution,
              file: str,
              relevant: bool = False):
        f = open(file, "w")
        distribution = pop.get_relevant_item_distribution() if relevant else pop.get_item_distribution()
        i = 0
        f.write("Item\tNum.ratings")
        for val in distribution:
            f.write("\n" + str(i) + "\t" + str(val))
            i += 1
        f.close()
