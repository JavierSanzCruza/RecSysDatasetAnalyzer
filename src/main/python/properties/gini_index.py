"""
Implementation of the Gini index of a list of values.
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

from functools import reduce
import typing


class GiniIndex:
    """
    Auxiliar class for computing the Gini index of a list of values.
    """

    @staticmethod
    def compute(values: typing.List[float],
                is_sorted: bool = True,
                reverse: bool = False):
        """
        Computes the Gini index of a list of values.
        :param values: the list of values
        :param is_sorted: True if the list is sorted, False otherwise.
        :param reverse: True if the list is sorted, but in reverse order.
        :return: the value of the Gini index.
        """

        gini = 0.0
        size = len(values)
        sum = reduce((lambda x, y: x + y), values)

        if not is_sorted:
            # We copy the list:
            auxlist = [x for x in values]
            auxlist.sort()
            reverse = False
        else:
            auxlist = values

        if reverse:
            for i in range(0, size):
                val = (2.0 * i - size + 1.0) * auxlist[i]
                val /= sum
                gini += val
        else:
            for i in range(0, size):
                val = (2.0 * i - size + 1.0) * auxlist[i]
                val /= sum
                gini += val
            for i in range(0, size):
                val = (2.0 * (size - i) - size - 1.0) * auxlist[i]
                val /= sum
                gini += val

        return gini / (size - 1.0)
