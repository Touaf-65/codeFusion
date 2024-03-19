#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 11:30:32 2024

@author: touaf
"""

import itertools


def execute():
	count = 0
	for i in itertools.count(1):
		s = str(i)
		t = "".join(sorted(s))
		if s != t and s[ : : -1] != t:
			count += 1  # i is bouncy
		if count * 100 == 99 * i:
			return str(i)


if __name__ == "__main__":
	print(execute())