"""
Implementation of the Gini index of the items (measuring the number of
ratings given to each user).
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

from src.main.python.properties.gini_index import GiniIndex
from .abstract_gini_index import AbstractGiniIndex


class UserGiniIndex(AbstractGiniIndex):
    """
    Implementation of the Gini index, measured over the items. A value close to 1 means a highly skewed distribution,
    whereas values close to 0 indicate balanced ones.
    """
    def compute_index(self, pop):
        distr = pop.get_user_distribution()
        return GiniIndex.compute(distr, True, True)

    def compute_relevant_index(self, pop):
        distr = pop.get_relevant_user_distribution()
        return GiniIndex.compute(distr, True, True)
