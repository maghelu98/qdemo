# cd ~/.config/ipython/profile_default
# sqlite3 history.sqlite
#sqlite> select source from history;
#source
12
get_ipython().magic('quickref')
(2 + 6) / 4
x = (2 + 6) / 4
x
x
y
y = 1
y
y=3
y
y = y + 5
y
z = x
z = x + y
z
u = x + y
u
u = u + 1
u
z
print( "u è uguale a " + u + ", z è uguale a " + z)
print( "u è uguale a " + str(u) + ", z è uguale a " + str(z))
forse
forse = 5 + 10
forse
ho_capito = 1000 + 1000
forse + ho_capito
forse = 5 + 12
forse + ho_capito
ok = "OK"
print (ok)
print ((ok+"! ")

)
print ((ok+"! "))
print ((ok+"! "*10))
print (( (ok+"! ") *10))
ho_cpito
ho_capito
print ( ho_capito * 3 , str(ho_capito) * 3)
type(9)
type(9.0)
type(9.5)
number = 9
print(type(number))
is_sabato = True
is_aprile = True
is_maggio = False
is_giorno = True
is_notte  = False
is_notte and is_aprile
is_giorno and is_aprile
is_notte or is_aprile
is_notte or (is_maggio and is_sabato)
is_notte or (is_aprile and is_sabato)
is_notte or (is_aprile and not is_sabato)
is_notte or (is_aprile or not is_sabato)
is_notte or (1 == 1)
is_notte or (1 == 2)
(10 - 5 == 3 + 2)
(10 - 5 == 3 + 2) and ( 10 > 11 )
(10 - 5 == 3 + 2) and (( 10 > 11 ) or ( 11 > 10))
(10 - 5 == 3 + 2) xor (( 10 > 11 ) or ( 11 > 10))
(10 - 5 == 3 + 2) or (( 10 > 11 ) or ( 11 > 10))
81 / 13
81% 13
6 * 13
a = "xxx"
a
b = "yyy"
b
c = "eee"
e
c
d= a+b+c
d
m= a+b+c+d
m
m * 6
122/3
3*44
l = [ 1, 5, 10 ]
l
len(l)
sum(l)
max(l)
min(l)
k = [ n * 2 for n in l ]
k
q = l+k+l
len(q)
q
q
sum(q)
p = set(q)
len(p)
p
qq = q * 5
qq
min(l)
[ n  for n in l ]
[ n + 5  for n in l ]
[ n * 2 + 5  for n in l ]
[ "<<<"+str(n)+">>>"  for n in l ]
sum([ "<<<"+str(n)+">>>"  for n in l ])
[ n > 3  for n in l ]
[ n   for n in l ]
[ n * 2 + 5  for n in l ]
[ (n * 2 + 5) <= 15  for n in l ]
[ (n * 2 + 5) <= 15  for n in l*3 ]
[ (n * 2 + 5) <= 15  for n in l ] * 3
[ (n * 2 + 5) <= 11  for n in l ]
[ (n * 2 + 5) <= 20  for n in l ]
[ '*' * (n * 2)  for n in l ]
[ '*' * (n)  for n in l ]
[ '#' * (n)  for n in l ]
l
[ '#' * (n+1)  for n in l ]
[ '#' * (n)  for n in l ]
[ l * (n)  for n in l ]
