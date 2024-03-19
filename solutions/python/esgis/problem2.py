#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:46:05 2024

@author: touaf
"""

import hacklib2


def execute():
	ans = 0
	isprime = hacklib2.list_primality(999999)
	primes = hacklib2.list_primes(999999)
	consecutive = 0
	for i in range(len(primes)):
		sum = primes[i]
		consec = 1
		for j in range(i + 1, len(primes)):
			sum += primes[j]
			consec += 1
			if sum >= len(isprime):
				break
			if isprime[sum] and consec > consecutive:
				ans = sum
				consecutive = consec
	return str(ans)


if __name__ == "__main__":
	print(execute())
    
    