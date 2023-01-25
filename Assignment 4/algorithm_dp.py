# -*- coding: utf-8 -*-
import time
import numpy as np
import sys
import matplotlib.pyplot as plt

#########################################################

def fillFarm(f, w, r, c):
  f[0][0] = w[0][0]

  for i in range(1, r):
    f[i][0] = f[i-1][0] + w[i][0]
  
  for j in range(1, c):
    f[0][j] = f[0][j-1] + w[0][j]

  for i in range(1, r):
    for j in range(1, c):
      f[i][j] = max(f[i-1][j], f[i][j-1]) + w[i][j]

#########################################################

def findAPath(f, w, r, c):
  currR = r - 1
  currC = c - 1
  
  path = []
  while currR > 0 and currC > 0:
    path.append([currC + 1, currR + 1])
    if f[currR-1][currC] >= f[currR][currC-1]:
      currR = currR - 1
    elif f[currR-1][currC] < f[currR][currC-1]:
      currC = currC - 1
      
  while currC >= 1:
    path.append([currC + 1, currR + 1])
    currC = currC - 1

  while currR >= 1:
    path.append([currC + 1, currR + 1])
    currR = currR - 1  

  path.append([currC + 1, currR + 1])


  pathStr = ""

  for i in reversed(path):
    pathStr += '(' + str(i[1]) + ',' + str(i[0]) + ') -> ' 

  return pathStr

#########################################################

# if len(w) == 0 or len(w[0]) == 0:
#   print("Given input array does not contain any field (No area for the farm)")
#   sys.exit()

#########################################################

# Input array w will be entered below

w = [[0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
 [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
 [1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1],
 [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
 [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0],
 [0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1],
 [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
 [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0]]


#w = np.random.randint(2, size=(20,20))

print(w)

rowNum = len(w)
colNum = len(w[0])

f = [[0 for x in range(colNum)] for y in range(rowNum)]

fillFarm(f, w, rowNum, colNum)

p = findAPath(f, w, rowNum, colNum)

print("Maximum number of weeds cleaned: ", f[rowNum - 1][colNum - 1])
print("Found Path is: " + p[:-3])

print("Filled array f: ", f)

#########################################################

# f = [[0 for x in range(colNum)] for y in range(rowNum)]

# fillFarm(f, w, rowNum, colNum)

# p = findAPath(f, w, rowNum, colNum)

# timePassed = (end-start)/100

#########################################################

