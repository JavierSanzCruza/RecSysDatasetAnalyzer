"""
Representation of the impressions included in a dataset.
"""

__version__ = '0.1'
__author__ = 'Javier Sanz-Cruzado, Pablo Castells'
__email__ = 'javier.sanz-cruzado@uam.es, pablo.castells@uam.es'

from data import AddingReturn


class Impressions:
    """
    Class that represents the impressions, i.e. the set of items which have been shown to a user.
    """

    def __init__(self):
        """
        Initializes the impressions in the system.
        """
        self.user_impressions = dict()
        self.item_impressions = dict()
        self.num_impressions = 0

    def add_user(self, user_id):
        """
        Adds a new user to the rating matrix.
        :param user_id: the identifier of the user.
        :return: true if we add the user, false otherwise.
        """
        if self.user_impressions.keys().__contains__(user_id):
            return False
        else:
            self.user_impressions[user_id] = set()
            return True

    def add_item(self, item_id):
        """
        Adds a new item to the rating matrix
        :param item_id: the identifier of the item.
        :return: true if we add the item, false otherwise.
        """
        if self.item_impressions.keys().__contains__(item_id):
            return False
        else:
            self.item_impressions[item_id] = set()
            return True

    def add_impression(self, user_id, item_id):
        """
        Adds a new impression
        :param user_id: the identifier of the user.
        :param item_id: the identifier of the item.
        :return: AddingReturn.ADDED if the impression is new, AddingReturn.NONE if it already existed,
                 AddingReturn.ERROR if something failed.
        """

        if self.user_impressions.keys().__contains__(user_id) and self.item_impressions.keys().__contains__(item_id):
            if self.user_impressions[user_id].__contains__(item_id):
                return AddingReturn.NONE
            else:
                self.user_impressions[user_id].add(item_id)
                self.item_impressions[item_id].add(user_id)
                self.num_impressions += 1
                return AddingReturn.ADDED
        return AddingReturn.ERROR

    def get_users(self):
        """
        Obtains the set of users.
        :return: the set of users.
        """
        return iter(self.user_impressions.keys())

    def get_items(self):
        """
        Obtains the set of items.
        :return: the set of items.
        """
        return iter(self.item_impressions.keys())

    def get_user_impressions(self, user_id):
        """
        Obtains the set of impressions for a user.
        :param user_id: the identifier of the user.
        :return: an iterator of the impressions for the user.
        """
        return iter(self.user_impressions.get(user_id, set()))

    def get_item_impressions(self, item_id):
        """
        Obtains the set of users including an item in their impressions.
        :param item_id: the identifier of the item.
        :return: an iterator of the impressed users.
        """
        return iter(self.item_impressions.get(item_id, set()))

    def get_num_impressions(self):
        """
        Obtains the number of impressions.
        :return: the number of impressions.
        """
        return self.num_impressions

    def get_num_users(self):
        """
        Obtains the number of users.
        :return: the number of users.
        """
        return self.user_impressions.keys().__len__()

    def get_num_items(self):
        """
        Obtains the number of items.
        :return: the number of items.
        """
        return self.item_impressions.keys().__len__()