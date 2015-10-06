#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mutability differences between strings and their cousin, the tuple."""

def flip_keys(to_flip):
    flipped = []
    for item in to_flip:
        flipped.append(item[::-1])
    for i in range(0,len(flipped)):
        to_flip[i] = flipped[i]    
    return(to_flip)
