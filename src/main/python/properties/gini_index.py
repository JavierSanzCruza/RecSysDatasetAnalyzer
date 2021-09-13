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

class GiniIndex:
    """
    Auxiliar class for computing the Gini index of
    """
    @staticmethod
    def compute(list, sorted=True, reverse=False):
        """
        Computes the Gini index of a list of values.
        :param list: the list of values
        :param sorted: True if the list is sorted, False otherwise.
        :param reverse: True if the list is sorted, but in reverse order.
        :return: the value of the Gini index.
        """

        gini = 0.0
        size = len(list)
        sum = reduce((lambda x, y: x + y), list)

        if not sorted:
            # We copy the list:
            auxlist = [x for x in list]
            auxlist.sort()
            reverse = False
        else:
            auxlist = list

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
