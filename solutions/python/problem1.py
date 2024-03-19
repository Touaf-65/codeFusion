#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 05:04:39 2024

@author: touaf
"""

import hacklib

def execute():
	LIMIT = 10**14
	
	# utilisation d'une liste d'un element pour stocker la somme, car Python 
    # ne supporte ne supporte pas les variables 'non locales'
	ans = [0]
	
	# find_harshad_primes(n, digitsum, isstrong)
    # n: doit etre un nombre Harshad troncable a droite, 
    # digitsum: somme des chiffres composant n,
    # isstrong: flag indiquant si oui ou on n est un nombre premier.
    
	def find_harshad_primes(n, digitsum, isstrong):
		# Décalez d'un chiffre vers la gauche et essayez les 10 possibilités pour le chiffre le plus à droite
		m = n * 10
		s = digitsum
		for i in range(10):
			if m >= LIMIT:
				break
			if isstrong and hacklib.is_prime(m):
				ans[0] += m
			if m % s == 0:
				find_harshad_primes(m, s, hacklib.is_prime(m // s))
			m += 1
			s += 1
	
	for i in range(1, 10):  # Tous les nombres à un chiffre sont trivialement des nombres Harshad
		find_harshad_primes(i, i, False)
	return str(ans[0])


if __name__ == "__main__":
	print(execute())