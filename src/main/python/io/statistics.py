from src.main.python.statistics import Statistics


class StatisticsWriter:

    @staticmethod
    def write(stats: Statistics,
              file: str):

        f = open(file, "w")
        f.write("Name\tValue")
        for name, value in stats.get_stats().items():
            f.write("\n" + name + "\t" + value)
        f.close()

