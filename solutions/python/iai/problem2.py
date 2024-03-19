#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 11:24:20 2024

@author: touaf
"""

def execute():
    # Calculer la somme des diviseurs appropriés pour chaque nombre
	divisorsum = [0] * 10000
	for i in range(1, len(divisorsum)):
		for j in range(i * 2, len(divisorsum), i):
			divisorsum[j] += i
	
	# Trouvez toutes les paires amicales à portée
	ans = 0
	for i in range(1, len(divisorsum)):
		j = divisorsum[i]
		if j != i and j < len(divisorsum) and divisorsum[j] == i:
			ans += i
	return str(ans)


if __name__ == "__main__":
	print(execute())