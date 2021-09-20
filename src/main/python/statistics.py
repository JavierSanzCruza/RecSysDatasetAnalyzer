from abc import ABC

import typing


class Statistics(ABC):
    """
    Class for storing the basic statistics for a dataset. This class is abstract, since each dataset has its own
    statistics.
    """

    def __init__(self):
        """
        Constructor. Initializes the dictionary.
        """
        self.stats = dict()

    def add_stat(self,
                 name: str,
                 value: typing.Any):
        """
        Constructor. Adds a key to the dictionary.
        """
        self.stats[name] = value

    def get_stats(self):
        return self.stats