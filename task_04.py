#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Working with for loop """


def process_data(data):
    """
    Args:
        data(mixed): A list or tuple containing numbers
    Returns:
        tuple: Sum and average of data
    """
    addition = 0
    for item in data:
        addition += item
    average = addition / float(len(data))
    return (addition, average)

if __name__ == '__main__':
    print process_data((1, 2, 5))