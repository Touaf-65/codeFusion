#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 11:00:47 2024

@author: touaf
"""

import itertools


def execute():
	LIMIT = 10**6
	
	# divisorsum[n] est la somme de tous les diviseurs propres de n
	divisorsum = [0] * (LIMIT + 1)
	for i in range(1, LIMIT + 1):
		for j in range(i * 2, LIMIT + 1, i):
			divisorsum[j] += i
	
	# Analyse de la longueur de la chaine amicale pour chq nombre dans l'ordre croissant
	maxchainlen = 0
	ans = -1
	for i in range(LIMIT + 1):
		visited = set()
		cur = i
		for count in itertools.count(1):
			# count represente la longueur de la chaine amicale
			visited.add(cur)
			next = divisorsum[cur]
			if next == i:
				if count > maxchainlen:
					ans = i
					maxchainlen = count
				break
			# condition de superiorite a la limte ou non chaine
			elif next > LIMIT or next in visited:
				break
			else:
				cur = next
	
	return str(ans)


if __name__ == "__main__":
	print(execute())