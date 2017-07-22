#qpy:console
################################
# quiz tabelline
################################

print "Hello World!"

p = 1
while p == 1:
   t= input(">>> Tabellina ? ")
   ok=0
   ko =0
   for i in range(0,10+1):
      r = input(" %d x %d = " % (i, t))
      if r == (t*i):
         ok = ok + 1
         print "esatto"
      else:
         ko = ko + 1
         print "SBAGLIATO! => " , t*i
         
      print "-" * 30
      for j in range(1,i+1):
          print "%3d) "%(j*t),(" margherita")*t
          
      print "-" * 30
      
   v = 10.0 * ok / (ok + ko)
   print "/" * 40
   print "Risultato Tabellina del ",t
   print " => ok= ",ok
   print " => ko= ",ko
   print " => voto: %.1f"%v
   print "/" * 40
   p = input("0:exit, 1:loop ? ")
   
print "Bye!"
