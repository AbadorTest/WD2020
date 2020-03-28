import sys

print("Podaj jakiś tekst")
s=sys.stdin.readline() #Wczytuje wiersz
print("Twój tekst to: "+s)

#Do wydruku można użyć też komendy write np.
sys.stdout.write(s)
#Pobieramy od użytkownika liczbę
#Chcemy sprawdzić czy jest dodatnia czy ujemna

l=input("Podaj jakąś liczbę")

#l jest typu string musimy ją rzutować na całkowitą

l=int(l)

if l > 0:
    print("Podano liczbę dodatnią")
elif l < 0:
    print("Podano liczbę ujemną")
else:
    print("Podano liczbe równą zero")
Chcemy wyświetlić liczby od 1 do 5

for x in range(1, 6, 1):
    print(str(x)+" ")


#Tworzymy swoją listę i chcemy jej użyć jako sekwencji do wyświetlania wartości

lista=[3, 4, 2, 1, 6]

for x in lista:
    print(str(x)+" ")


#Wyświetlamy elementy za pomocą pętli ale na koniec odpowiedni komunikat

lista=[3, 4, 2, 1, 6]

for x in lista:
    print(str(x)+" ")
else:
    print("Koniec wyświetlania")
#skrypt wyświetla losowe liczby całkowite aż napotka 5

import random #biblioteka z funkcjami do losowania

random.seed() #inicjowanie generatora

z=random.randint(1,15) #losowanie pierwszej liczby

while(z!=5):
    print(str(z))
    z=random.randint(1,15)
else:
    print("Znalazłem 5 koniec działania")
#Użytkownik podaje liczbę
#Przeglądamy listę liczb i jeśli znajdziemy tę podaną przez użytkownika
#wyświetlamy komunikat i kończymy działanie pętli

lista = [1, 5, 3, 2, 6, 5, 7, 8, 9, 10]
print("Podaj liczbę a sprawdzę czy jest na liście")
liczba=input()
licznik=0
while licznik<10:
    #Jeśli znajdziemy liczbę przerywamy
    if int(liczba) == lista[licznik]:
        print("Twoja liczba: "+liczba+"znaleziona na pozycji: "+str(licznik))
        continue
    print("!")
    licznik+=1
import sys

for i in [1, 2, 3, 4, 5]:
    for j in [1, 2, 3, 4, 5]:
        #sprawdza czy jest w pionowej linii H
        if i==3:
            sys.stdout.write('H')
            continue
        #jeśli nie to rysuje H na brzegach
        else:
            #sprawdzamy czy j zawiera się na liście, czyli jest na brzegach
            if j in [1,5]:
                sys.stdout.write('H')
            #jeśli nie piszemy spację
            else:
                sys.stdout.write(' ')
    sys.stdout.write('\n')
#Uzytkownik podaje liczby do dzielenia
#Chcemy wyłapać moment dzielenia przez zero
print("Proszę podać pierwszą liczbę")
licz1 = input()
print("Proszę podać drugą liczbę")
licz2 = input()
try:
    wynik = int(licz1) / int(licz2)
    print("Wynik= "+str(wynik))
except: #nazwa błędu dzielenia przez zero
    print("Nie ta wartość")
