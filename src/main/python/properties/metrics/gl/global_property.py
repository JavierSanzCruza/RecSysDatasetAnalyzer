"""
Definition of a gl property of the rating matrix.
"""

__version__ = '0.1'
__author__ = 'Javier Sanz-Cruzado, Pablo Castells'
__email__ = 'javier.sanz-cruzado@uam.es, pablo.castells@uam.es'
__copyright__ = """
 Copyright (C) 2021 Information Retrieval Group at Universidad Autónoma
 de Madrid, http://ir.ii.uam.es.

 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this
 file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""
__license__ = 'Mozilla Public License v. 2.0'

from abc import ABC, abstractmethod

from src.main.python.data import RatingMatrix
import typing


class GlobalProperty(ABC):
    """
    Global property of ratings in a dataset.
    """

    def __init__(self,
                 rating_matrix: RatingMatrix):
        """
        Initializes the metric.
        :param rating_matrix: the rating matrix over which the metric shall be computed.
        """
        self.rating_matrix = rating_matrix

    @abstractmethod
    def compute(self,
                relevant: bool = False,
                user_filter: typing.Callable[[int], bool] = None,
                item_filter: typing.Callable[[int], bool] = None,
                rating_filter: typing.Callable[[int, int, float], bool] = None
                ) -> float:
        """
        Computes the value of a metric.
        :param relevant: True if we only consider relevant ratings, False otherwise.
        :param user_filter: (OPTIONAL) filter for selecting the users. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filter for selecting the items. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filter for selecting the ratings. By default, no filter is applied.
        """
        pass
