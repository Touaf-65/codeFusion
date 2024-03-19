#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 11:17:20 2024

@author: touaf
"""

# Renvoie le nombre de 1 dans la représentation binaire de
# l'entier non négatif x. Également connu sous le nom de poids de Hamming.
def popcount(x: int) -> int:
	return bin(x).count("1")