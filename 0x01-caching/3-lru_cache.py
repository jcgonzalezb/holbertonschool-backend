#!/usr/bin/python3
""" LRUCache module to work with a basic dictionary.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache inherits from BaseCaching and
    is a caching system.
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.ordered_cache_keys = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        dict_data = self.cache_data
        if not (key is None or item is None):
            if (len(dict_data) == BaseCaching.MAX_ITEMS and
                    key not in dict_data):
                lru = self.ordered_cache_keys[0]
                print('DISCARD: {}'.format(lru))
                self.ordered_cache_keys.pop(0)
                del dict_data[lru]
                dict_data[key] = item
                self.ordered_cache_keys.append(key)
            elif (
                len(dict_data.keys()) == BaseCaching.MAX_ITEMS and
                (key in dict_data.keys())
            ):
                self.ordered_cache_keys.remove(key)
                self.ordered_cache_keys.append(key)
                dict_data[key] = item
            else:
                self.ordered_cache_keys.append(key)
                dict_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        dict_data = self.cache_data
        if key is None or key not in dict_data:
            return None

        return dict_data[key]
