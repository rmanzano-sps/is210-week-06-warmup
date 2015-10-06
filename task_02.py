#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""interacting with an existing list and performing some standard access functions"""

import data

BALLETS = data.BALLETS

del BALLETS[11]

BALLETS.append('Herman Schmerman')

BALLETS.extend(['Don Quixote', 'Sylvia'])
