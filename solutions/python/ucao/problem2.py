#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 07:44:39 2024

@author: touaf
"""
def execute():
	MOD = 10**10
	ans = (28433 * pow(2, 7830457, MOD) + 1) % MOD
	return str(ans)


if __name__ == "__main__":
	print(execute())