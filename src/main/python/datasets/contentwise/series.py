"""
Representation of the ContentWise dataset series.
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


class ContentWiseSeries:
    """
    Class for storing the information of the series in the ContentWise dataset.
    """
    def __init__(self,
                 series_id: int,
                 length: int):
        """
        Initializes a series.
        :param series_id: the identifier of the series.
        :param length: the length of the series.
        """
        self.series_id = series_id
        self.length = length

    def get_series_id(self):
        """
        Obtains the identifier of the series.
        :return: the identifier of the series.
        """
        return self.series_id

    def get_length(self):
        """
        Obtains the length of the series.
        :return: the length of the series.
        """
        return self.length
