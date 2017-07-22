#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 17:59:20 2017

@author: margherita
"""

# %%



##---(Sat Jul 22 16:53:03 2017)---
runfile('/home/margherita/Dropbox/qdemo/coso_cosa.py', wdir='/home/margherita/Dropbox/qdemo')
l = [ 1, 5, 10 ]
l = [ 1, 5, 10 ]
[ "<<<"+str(n)+">>>"  for n in l ]
k = [ n * 2 for n in l ]

##---(Sat Jul 22 17:15:17 2017)---
l = [ 1, 5, 10 ]
k = [ n * 2 for n in l ]
10 +1
444444*888888
1 + 1 * 2
"1" + "1" * 2
"a" + "b" * 2
"a" + "bcdef" * 2
10 > 5
10 < 5
(10 < 5) or (3 > 4)
(10 < 5) or (3 < 4)
(10 < 5) or (3 > 4)
(10 < 5) or not (3 > 4)
(10 < 5) and not (3 > 4)
not (10 < 5) and not (3 > 4)
[ 1, 2, 5]
[ 1, 2, 5] * 2
[ 1, 2, 5] * 10
l = [ 1, 2, 5] 
[ x for x in l ]
[ x + 1  for x in l ]
[ x + 1  for x in l * 2 ]
[ x > 2  for x in l * 2 ]
[ x  for x in l * 2 ]
[ "#" * (x*2)  for x in l * 2 ]
[ "#" * (x*3)  for x in l * 2 ]
[ "#" * (x*3)  for x in l * 5 ]
set([ "#" * (x*3)  for x in l * 5 ])
set([ "#" * (x*3)  for x in l * 15 ])
[ "#" * (x*3)  for x in l * 15 ]
k = set([ "#" * (x*3)  for x in l * 5 ])
k = set([ x  for x in l ])
k
6 in k
5 in k
[ x  for x in range(10) ]
[ x  for x in range(5) ]
[ x  for x in range(20) ]
[ x  for x in range(10) ]
[ x in k for x in range(10) ]
[ x for x in range(0) ]
[ x for x in range(100) ]
[ x for x in range(1000) ]
[ x for x in range(1000) if (x % 7) == 0 ]
[ x for x in range(7000) if (x % 7) == 0 ]
[ [ x for x in range(100) if (x % 7) == 0 ] for y in range(5) +1 ]
[ [ x for x in range(100) if (x % 7) == 0 ] for y in range(5) ]
[ (y,[ x for x in range(100) if (x % 7) == 0 ]) for y in range(5) ]
[ (y,[ x for x in range(100) if (x % (y+1)) == 0 ]) for y in range(5) ]
[ (y+1,[ x for x in range(100) if (x % (y+1)) == 0 ]) for y in range(5) ]
[ [ x for x in range(100) if (x % (y+1)) == 0 ] for y in range(5) ]
[ [ x for x in range(50) if (x % (y+2)) == 0 ] for y in range(3) ]
[ (y,[ x for x in range(50) if (x % y+1) == 0 ]) for y in range(3) ]
[ (y,[ x for x in range(50) if (x % (y+1)) == 0 ]) for y in range(3) ]
[ (y,[ x for x in range(20) if (x % (y+1)) == 0 ]) for y in range(3) ]
[ (y+7,[ x for x in range(20) if (x % (y+7)) == 0 ]) for y in range(3) ]
[ (y+7,[ x for x in range(100) if (x % (y+7)) == 0 ]) for y in range(3) ]
(1,2,3)
(1,"a",3)
((1,"a",3), 1)
[ (x,y) for x in range(10) for y in range(5) ]
[ (x,y) for x in range(3) for y in range(5) ]
[ (x,y) for x in range(3) for y in range(5) if x >= y]
[ (x,y) for x in range(3) for y in range(5) if ((x + y) % 2) ]
[ (x,y) for x in range(3) for y in range(5) if ((x + y) % 2) == 0 ]
[ (x,y, x+y) for x in range(3) for y in range(5) if ((x + y) % 2) == 0 ]
