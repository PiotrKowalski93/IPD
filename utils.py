# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 14:41:13 2018

@author: Craftware
"""
import random

def getRandomFromRange(amount,a,b):
    weights = []
    for i in range(amount):     
        weights.append(round(random.uniform(a, b),2))  
    return weights

    