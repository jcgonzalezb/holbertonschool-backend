#!/usr/bin/python3
""" FIFOCache module to work with a basic dictionary.
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ BasicCache inherits from BaseCaching and
    is a caching system.
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        dict_data = self.cache_data
        if key or item is None:
            pass
        else:
            if len(dict_data.keys) > BaseCaching.MAX_ITEMS:
                item = dict_data.popitem(last = False)
                key = str(item[0])
                return print("DISCARD: {}".format(key))


    def get(self, key):
        """ Get an item by key
        """
        dict_data = self.cache_data
        if key is None or key not in dict_data:
            return None

        return dict_data[key]
