#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache defines:
    - It is a caching system
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        dict_data = self.cache_data
        dict_data[key] = item
        return dict_data


    def get(self, key):
        """ Get an item by key
        """
        dict_data = self.cache_data
        if key is None or key not in dict_data:
            return None

        return dict_data[key]
