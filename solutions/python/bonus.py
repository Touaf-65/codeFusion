#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 07:01:06 2024

@author: touaf
"""

import itertools


def execute():
	cond = lambda i: all(sorted(str(i)) == sorted(str(j * i)) for j in range(2, 7))
	ans = next(i for i in itertools.count(1) if cond(i))
	return str(ans)


if __name__ == "__main__":
	print(execute())