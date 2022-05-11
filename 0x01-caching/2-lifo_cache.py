#!/usr/bin/python3
""" LIFOCacheCache module to work with a basic dictionary.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching and
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
        if not (key is None and item is None):
            if (len(dict_data) == BaseCaching.MAX_ITEMS and
            key not in dict_data):
                last = sorted(dict_data.keys())[-1]
                print("DISCARD: {}".format(last))
                del dict_data[last]
                dict_data[key] = item
            else:
                dict_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        dict_data = self.cache_data
        if key is None or key not in dict_data:
            return None

        return dict_data[key]
