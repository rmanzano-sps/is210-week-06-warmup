#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Explore Loop concept with our data module"""

def process_data(data):
    data_sum = 0
    for data_point in data:
        data_sum += data_point
    data_average = float(data_sum) / len(data)
    return(data_sum, data_average)
