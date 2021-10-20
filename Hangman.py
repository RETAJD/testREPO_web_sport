import random
import linecache
pierwsza = linecache.getline("baza.txt",1)
f = open("baza.txt", "r")
liczba_linii = len(open("baza.txt", "r").readlines())
baza = [pierwsza]
for i in range(liczba_linii+1):
    baza.append(f.readline())
    baza[i] = baza[i].replace("\n","")
baza.pop(0)
baza.pop(-1)
#print(baza)
slowo = random.choice(baza)
odpowiedz = slowo
dlugosc = len(slowo)
#print(slowo)
print("Wylosowane slowo ma ",dlugosc, "liter(y), masz 3 zycia")
blad1 = None
blad2 = None 
zycia = 3
odgadniete = ["_"]*dlugosc
while (True):
    #dobre_proby = ["pierwsza","druga"]
    x = input("Podaj litere: ")
    while(x<"a" or x>"z" or len(x)!=1):
        x = input("Niepoprawnie wprowadzona litera, sprobuj ponownie: ")
    if (x in slowo):
        for i in range(dlugosc):
            if(slowo[i] == x):
                odgadniete[i] = x
            print(odgadniete[i], end=" ")
        print("\nTak, \"",x,"\" wystepuje w slowie, pozostalo zyc:",zycia)
        if ("_" not in odgadniete):
            print("Gratulacje! odgadniete slowo to:",odpowiedz)
            break
    else: 
        for i in range(dlugosc):
            print(odgadniete[i], end=" ")
        zycia = zycia - 1
        if (zycia == 2):
            blad1 = x
            print("\nNie, \"",x,"\" nie wystepuje w slowie, popelnione bledy: \"",blad1,"\" pozostalo zyc:",zycia)
        if (zycia == 1):
            blad2 = x
            print("\nNie, \"",x,"\" nie wystepuje w slowie, popelnione bledy: \"",blad1,"\",\"",blad2,"\" pozostalo zyc:",zycia)
        if (zycia == 0):
            print("\nKoniec gry... chodzilo o slowo:",odpowiedz)
            break
