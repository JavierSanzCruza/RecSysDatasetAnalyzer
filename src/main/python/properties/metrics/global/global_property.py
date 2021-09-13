"""
Definition of a global property of the rating matrix.
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


class GlobalProperty(ABC):
    """
    Global property of ratings in a dataset.
    """

    @abstractmethod
    def compute(self, rating_matrix):
        """
        Computes the value of a metric.
        :param rating_matrix: the rating matrix of the dataset
        """
        pass

    @abstractmethod
    def compute_relevant(self, rating_matrix):
        """
        Computes the value of a metric, restricted to the relevant ratings.
        :param rating_matrix: the rating matrix of the dataset
        """
        pass

    @abstractmethod
    def compute_filter(self, rating_matrix, user_filter=lambda x: x, item_filter=lambda x: x, rating_filter=lambda x: x):
        """
        Computes the value of a metric.
        :param rating_matrix: the rating matrix of the dataset.
        :param user_filter: (OPTIONAL) filters the set of users to consider. By default, no filter is applied.
        :param item_filter: (OPTIONAL) filters the set of items to consider. By default, no filter is applied.
        :param rating_filter: (OPTIONAL) filters the set of ratings to consider. By default, no filter is applied.
        :return: the value of the global property.
        """
        pass




