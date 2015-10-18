#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Reverse functions """


def flip_keys(to_flip):
    """
    Args:
        to_flip (list): immutable nested sequences
    Returns:
        list: Original list in reverse order.
    """

    idx = 0
    for item in to_flip:
        to_flip[idx] = item[::-1]
        idx += 1
    return to_flip

if __name__ == '__main__':
    print flip_keys([(1, 2, 3), 'acelera'])