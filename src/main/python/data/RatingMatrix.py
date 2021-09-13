"""
Representation of the basic rating matrix of a recommendation dataset.
It just includes a) users, b) items and c) ratings between users and items.
"""

__version__ = '0.1'
__author__ = 'Javier Sanz-Cruzado, Pablo Castells'
__email__ = 'javier.sanz-cruzado@uam.es, pablo.castells@uam.es'

import math

from data import AddingReturn


class RatingMatrix:
    """
    Representation of the basic rating matrix of a recommendation dataset.
    It just includes a) users, b) items and c) ratings between users and items.
    """

    def __init__(self, threshold, binarize, update):
        """
        Initializes the rating matrix.
        :param threshold: the relevance threshold of the ratings.
        :param binarize: true if we want to store binarized ratings, false otherwise.
        :param update:  true if a) we want to add the number of relevant ratings to a user (when binarizing) or
                        b) we want to take the maximum possible value for a rating (when we do not binarize). False otherwise.
        """
        self.users = set()
        self.items = set()

        self.user_2_item_matrix = dict()
        self.item_2_user_matrix = dict()

        self.num_ratings = 0
        self.num_rel_ratings = 0

        self.num_total_ratings = 0
        self.num_total_rel_ratings = 0

        self.threshold = threshold
        self.binarize = binarize
        self.update = update

    def add_user(self, user_id):
        """
        Adds a new user to the rating matrix.
        :param user_id: the identifier of the user.
        :return: true if we add the user, false otherwise.
        """
        if self.users.__contains__(user_id):
            return False
        else:
            self.users.append(user_id)
            self.user_2_item_matrix[user_id] = dict()
            return True

    def add_item(self, item_id):
        """
        Adds a new item to the rating matrix
        :param item_id: the identifier of the item.
        :return: true if we add the item, false otherwise.
        """
        if self.items.__contains__(item_id):
            return False
        else:
            self.items.append(item_id)
            self.item_2_user_matrix[item_id] = dict()
            return True

    def rate(self, user_id, item_id, value):
        """
        Adds a new rating to the matrix.
        :param user_id: the identifier of the user.
        :param item_id: the identifier of the item.
        :param value: the value of the rating.
        :return: AddingReturn.ADDED if the rating is new, AddingReturn.UPDATED if we just updated it, AddingReturn.NONE
        if it kept the same, AddingReturn.ERROR if something failed.
        """
        if math.isnan(value):
            return AddingReturn.ERROR

        if self.users.__contains__(user_id) and self.items.__contains__(item_id):
            oldval = self.user_2_item_matrix[user_id].get(item_id, math.nan)
            val = (1.0 if value >= self.threshold else 0.0) if self.binarize else value
            rel = value >= self.threshold

            self.num_total_ratings += 1
            self.num_total_rel_ratings += 1 if rel else 0

            if math.isnan(oldval): # The rating does not exist.
                self.user_2_item_matrix[user_id][item_id] = val
                self.item_2_user_matrix[item_id][user_id] = val
                self.num_rel_ratings += 1 if rel else 0
                self.num_ratings += 1
                return AddingReturn.ADDED
            elif self.binarize and self.update: # The rating already exists, and we count the number of positives.
                oldrel = oldval > 0
                self.user_2_item_matrix[user_id][item_id] = val + oldval
                self.item_2_user_matrix[item_id][user_id] = val + oldval
                self.num_rel_ratings += 1 if (not oldrel and rel) else 0
                return AddingReturn.UPDATED
            elif self.update and val > oldval:
                oldrel = oldval >= self.threshold
                val = max(oldval, val)
                self.num_rel_ratings += 1 if (not oldrel and rel) else 0
                self.user_2_item_matrix[user_id][item_id] = val
                self.item_2_user_matrix[item_id][user_id] = val
                return AddingReturn.UPDATED
            else:
                return AddingReturn.NONE
        else:
            return AddingReturn.ERROR

    def get_num_ratings(self):
        """
        Obtains the number of ratings (not repeated)
        :return: the number of ratings (not repeated)
        """
        return self.num_ratings

    def get_num_rel_ratings(self):
        """
        Obtains the number of relevant ratings (not repeated)
        :return: the number of relevant ratings (not repeated)
        """
        return self.num_ratings

    def get_num_total_ratings(self):
        """
        Obtains the number of ratings (with repetitions)
        :return: the number of ratings (with repetitions)
        """
        return self.num_total_ratings

    def get_num_rel_ratings(self):
        """
        Obtains the number of relevant ratings (with repetitions)
        :return: the number of relevant ratings (with repetitions)
        """
        return self.num_ratings