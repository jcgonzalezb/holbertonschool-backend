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

        try:
            while len(dict_data) < BaseCaching.MAX_ITEMS:
                dict_data[key] = item
                return dict_data

            if key not in dict_data:
                dict_data[key] = item
                fi = list(dict_data)[0]
                key = dict_data.pop(fi)
                print("DISCARD: {}".format(fi))
            else:
                dict_data[key] = item
                return dict_data

        except key or item is None:
            pass

    def get(self, key):
        """ Get an item by key
        """
        dict_data = self.cache_data
        if key is None or key not in dict_data:
            return None

        return dict_data[key]
