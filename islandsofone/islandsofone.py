# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 17:11:05 2015

@author: tushar
"""

import sys
import random

maxsize = 5

matrix  = []

for itera in range(0,maxsize):
    matrix.append([])
    for nest in range (0,maxsize):
        matrix[itera].append(random.randint(1, 100) % 2)
        
for itera in range(0,maxsize):
    for nest in range (0,maxsize):
        print " {first}".format(first=matrix[itera][nest]), 
    print "\n"
           
visited = []

for itera in range(0,maxsize):
    visited.append([])
    for nest in range (0,maxsize):
        visited[itera].append(0)

#Now we iterate over and do dfs

def call_dfs_neighbor(i, j):
    #norh direstion
    if j-1 >= 0:
        DFS_ISLAND(i, j-1)
    if i-1 >= 0:
        DFS_ISLAND(i-1, j)
    if i+1 < maxsize:
        DFS_ISLAND(i+1, j)
    if j+1 < maxsize:
        DFS_ISLAND(i, j+1)
    

def DFS_ISLAND(row, col):
    if matrix[row][col] == 1 and visited[row][col] != 1:
        visited[row][col] = 1
        call_dfs_neighbor(row, col)
    
 
def main():
     island_counter = 0
     
     for itera in range(0, maxsize):
         for nest in range(0, maxsize):
             if visited[itera][nest] != 1 and matrix[itera][nest] == 1: 
                 #for tera in range(0, maxsize):
                     #for est in range(0, maxsize):
                         #print visited[tera][est],
                     #print
                 DFS_ISLAND(itera, nest)
                 island_counter += 1
         visited[itera][nest] = 1
                 
     print island_counter
     
     
main()
        









    