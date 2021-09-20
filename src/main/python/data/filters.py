"""
Filters for selecting the different elements of a dataset.
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

from typing import Callable


class UserFilter:
    """
    Methods for selecting the users to consider.
    """

    @staticmethod
    def default():
        """
        Default filter. It does not apply any filter.
        """
        func: Callable[[int], bool] = lambda user: True
        return func


class ItemFilter:
    """
    Methods for selecting the items to consider.
    """

    @staticmethod
    def default():
        """
        Default filter. It does not apply any filter.
        """
        func: Callable[[int], bool] = lambda item: True
        return func


class RatingFilter:
    """
    Methods for selecting the ratings to consider.
    """

    @staticmethod
    def default():
        func: Callable[[int, int, float], bool] = lambda user, item, rating: True
        return func


class ImpressionsFilter:
    """
    Methods for selecting the impressions to consider
    """

    @staticmethod
    def default():
        func: Callable[[int, int], bool] = lambda user, item: True
        return func
