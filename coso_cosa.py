##
# ricercare l'elemento piu' frequente in una lista di numeri inseriti dall'utente
#


#mp = input("papo is bad")
#print("cattivo"+mp)

#print("###")
stringa_input = input("Digitare lista numeri separati da virgola: ")

print(" inserito: <<"+stringa_input+">>")


lista_input = stringa_input.split(",")


print(" separata virgola: ", lista_input)


for pezzo in lista_input:
    print("--> "+pezzo)

interi = [int(elem) for elem in lista_input]

print(interi)

print("sum:", sum(interi))
print("media:", sum(interi)/len(interi))








