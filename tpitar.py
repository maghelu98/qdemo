#!/usr/bin/python
#qpy:console
################################
# Tavola Pitagorica
################################
from __future__ import print_function

def larghezza(num):
   return 5 * num + 10

def intestazione(num):
   print("=" * larghezza(num))
   print(">    || ", end='')
   for c in range(1,n+1):
       print("%3d| "%(c), end='')
   print(" <")
   print("-" * larghezza(num))

def chiusura(num):
   print("=" * larghezza(num))

print("Hello World!")
p = 1
while p == 1:
   n = input(">>> Dimensione Tabellina ? ")

   intestazione(n)
   for r in range(1,n+1):
       print( "> %3d|| "%(r), end='')

       for c in range(1,n+1):
           print("%3d| "%(r * c), end='')
          
       print(" <")
   chiusura(n)
   print("+++ ")
   p = input("0:exit, 1:loop ? ")
   
print("Bye!")
