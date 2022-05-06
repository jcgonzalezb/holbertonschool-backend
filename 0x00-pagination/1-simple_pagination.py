#!/usr/bin/env python3
"""
This project module contains a function that
takes two integer arguments and returns a tuple.
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        xxxxxx
        Returns:
            xxxxxx
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        tupl = index_range(page, page_size)
        #print(tupl)
        start_index = int(tupl[0])
        end_index = int(tupl[1])
        #print(type(start_index))
        result = Server.dataset(self)
        print(len(result))
        print(result[(start_index):(end_index)])
        #print(type(result))
        #print(result)
        #return Server.dataset(self)


def index_range(page, page_size):
    """
    Function that takes two integer arguments and
    returns a tuple.
    Returns:
        A tuple of size two containing a start index
        and an end index corresponding to the range
        of indexes to return in a list for those
        particular pagination parameters.
    """
    tuple1 = ()
    tuple2 = ()
    end_index = page * page_size
    tuple2 += (end_index, )
    start_index = end_index - page_size
    tuple1 += (start_index, )

    return tuple1 + tuple2
