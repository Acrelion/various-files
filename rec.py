# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 16:38:02 2017

@author: Ivan

This script shows the basic principles of recursion.
"""

def rec(bottom):
    final_result = 0
    
    if bottom <= 10:
        bottom += 1
        
        final_result += 1
        final_result += rec(bottom)
    return final_result
    
    
#a = rec(1)
#print a  

def rec2(bottom):
    final_result = []
    
    if bottom <= 10:
        bottom += 1
        
        final_result.append(bottom)
        final_result.extend(rec2(bottom))
    return final_result


b = rec2(0)
print b
      