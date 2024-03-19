#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 04:43:40 2024

@author: touaf
"""

import math

# verifie la primalite d'un nombre
def is_prime(x: int) -> bool:
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, math.isqrt(x) + 1, 2):
			if x % i == 0:
				return False
		return True