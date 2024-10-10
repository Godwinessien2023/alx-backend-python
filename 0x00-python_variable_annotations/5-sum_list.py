#!/usr/bin/python3
"""
A type-annotated function
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    function sum_list that takes a list of floats as an
    argument and returns their sum as a float:
    """
    return sum(input_list)
