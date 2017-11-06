#!/usr/bin/env python
# -*- coding : utf-8 -*-
import collections

class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.is_word = False