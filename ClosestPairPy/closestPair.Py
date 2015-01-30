# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 09:31:56 2015

@author: tushar
"""

import sys

def main():

    alist = [1, 4, 5, 7]
    blist = [10, 20, 30, 40]
    
    answersum = 32

    aleft   = 0
    bright  = len(blist) - 1
    tempsum = 0
    diff    = sys.maxint
    l_res   = 0
    r_res   = 0
    
    while aleft < len(alist) and bright > 0:
        tempsum = alist[aleft] + blist[bright]                
        
        if abs(answersum - tempsum) < diff:
            diff = abs(answersum - tempsum)
            l_res = aleft
            r_res = bright
        if tempsum > answersum:
            bright -= 1
        else:
            aleft += 1
            
            
    print "Elements are {first} and  {second}".format(first=alist[l_res], second=blist[r_res])
    
    
main ()    
            
            