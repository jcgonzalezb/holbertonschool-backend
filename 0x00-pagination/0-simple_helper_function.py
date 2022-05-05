#!/usr/bin/env python3
"""
Main file
"""


def index_range(page, page_size):
    tuple1 = ()
    tuple2 = ()
    end_index = page * page_size
    tuple2 +=(end_index, )
    start_index = end_index - page_size
    tuple1 +=(start_index, )

    return tuple1 + tuple2
