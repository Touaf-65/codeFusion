#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 04:43:40 2024

@author: touaf
"""

import math, array
from typing import List, TypeVar, cast, Optional, Protocol, Generator, Any, Callable, Dict, Generic

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

# renvoie une liste de booleen 
# pour 0 <= i <= n, result[i] == True si n premier, False sinon
def list_primality(n: int) -> List[bool]:
	result: List[bool] = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(math.isqrt(n) + 1):
		if result[i]:
			for j in range(i * i, len(result), i):
				result[j] = False
	return result


E = TypeVar("E", bound="_Comparable")


class _Comparable(Protocol):
	def __lt__(self: E, other: E) -> bool: ...
	def __le__(self: E, other: E) -> bool: ...
	def __gt__(self: E, other: E) -> bool: ...
	def __ge__(self: E, other: E) -> bool: ...

def next_permutation(arr: List[E]) -> bool:
    # Trouver un suffixe non croissant
	i: int = len(arr) - 1
	while i > 0 and arr[i - 1] >= arr[i]:
		i -= 1
	if i <= 0:
		return False
	
	# Trouver un successeur pour pivoter
	j: int = len(arr) - 1
	while arr[j] <= arr[i - 1]:
		j -= 1
	arr[i - 1], arr[j] = arr[j], arr[i - 1]
	
	# Renverser le suffixe
	arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
	return True