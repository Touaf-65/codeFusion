#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 09:33:44 2024

@author: touaf
"""

import hacklib2


def execute():
	isprime = hacklib2.list_primality(10000)
	digits = list(range(1, 10))
	
	def count_prime_sets(startindex, prevnum):
		if startindex == len(digits):
			return 1
		else:
			result = 0
			for split in range(startindex + 1, len(digits) + 1):
				num = int("".join(map(str, digits[startindex : split])))
				if num > prevnum and is_prime(num):
					result += count_prime_sets(split, num)
			return result
	
	def is_prime(n):
		if n < len(isprime):
			return isprime[n]
		else:
			return hacklib2.is_prime(n)
	
	ans = 0
	while True:
		ans += count_prime_sets(0, 0)
		if not hacklib2.next_permutation(digits):
			break
	return str(ans)


if __name__ == "__main__":
	print(execute())
