# #Zamiast pisać w pętli
# zakres=[1, 2, 5]
# lista = []
# for element in zakres:
# 	if element > 1:
# 		lista.append("Cos sie dzieje z: %d " % element)
#
# print(lista)
# lista = []
# #możemy zapisać w jednej linijce
# lista = ["Cos sie dzieje z: %d" % element for element in zakres if element > 1]
# print(lista)
#Chcemy uzyskać liczby parzyste z podanego zakresu

#Wersja z pętlą

# liczby=[1,2,3,4,5,6,7,8,9,10]
# lista=[]
# for i in liczby:
#     if i % 2 == 0:
#         lista.append(i)
#
# print("Liczby parzyste uzyskane z wykorystaniem pętli")
# print(lista)
#
# #wersja z Python comprehension
#
# lista2=[i for i in liczby if i % 2 == 0]
# print(lista2)
# #Zagnieżdżanie
#Zamiast pisać tak:
# lista=[]
# for i in [1, 2, 3]:
#     for j in [4, 5, 6]:
#       if i != j:
#           lista.append((i,j))
# print(lista)
#
# #można to zrobić krócej
# lista2=[(i,j) for i in [1, 2, 3] for j in [4, 5, 6]]
# print(lista2)
# #Słowniki i zamiana klucza z wartością
#
# skroty={"PZU": "Państwowy zakład Ubezpieczeń",
#           "ZUS": "Zakład Ubezpieczeń Społecznych",
#           "PKO": "Powszechna Kasa Oszczędności"}
#
# odwrocone={value: key for key, value in skroty.items()}
# print("Oryginalny słownik")
# print(skroty)
# print("Słownik odwrócony")
# print(odwrocone)
# import math
#
# def row_kwadratowe(a, b, c):
#     delta = b**2 - 4 * a * c
#     if (delta < 0):
#         print("Brak pierwiastków")
#         return -1
#     elif (delta == 0):
#         print("Jeden pierwiastek")
#         x = (-b) / (2 * a)
#         return x
#     else:
#         print("Równanie ma dwa pierwiastki")
#         x1= (- b - math.sqrt(delta)) / (2 * a)
#         x2= (- b + math.sqrt(delta)) / (2 * a)
#         return x1, x2
#
# print(row_kwadratowe(6,1,3))
# print(row_kwadratowe(1,2))
# print(row_kwadratowe(1,4,1,4))
#Definiujemy funkcje z wartościami domyślnymi
# import math
#
# def dlugosc_odcinka(x1 = 0, y1 = 0, x2 = 0, y2 = 0):
#     return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#
# #wywołujemy dla wartości domyślnych
# print(dlugosc_odcinka())
#
# #wywolujemy dla własnych podanych wartości
# #są to argumenty pozycjne czyli ważna jest kolejnosć podania wartości
# print(dlugosc_odcinka(1, 2, 3, 4))
#
# #Wywolujemy funkcje podając mieszane wartości
# #Dwie pierwsze są interpretowane jako x1 i y1 jak podano w definicji funkcji
# print(dlugosc_odcinka(2, 2, y2 = 2, x2 = 1))
#
# #wywołujemy funkcje pdoając wartości nie w kolejności
# print(dlugosc_odcinka(y2 = 5, x1 = 2, y1 = 2, x2 = 6))
#
# #wywołujemy funkcję podając tylko dwa argumenty a reszta domyślne
# print(dlugosc_odcinka(x2 = 5, y2 = 5))
# #symbol * oznacza dowolną ilość argumentów przechowywanych w krotce
#
# def ciag(* liczby):
#     print(liczby)
#
#     #jeżeli nie ma argumentów to
#     if len(liczby) == 0:
#         return 0.0
#     else:
#         suma = 0.0
#
#         #sumujemy elementy ciągu
#         for i in liczby:
#             suma += i
#         #zwracamy wartość sumy
#         return suma
# #wywołanie gdy brak argumentów
# print(ciag())
#podajemy argumenty
# print(ciag(1,2,3,4,5,6,7,8))
# ** czyli dwie gwiazdki oznaczają że możemy użyć
# dowolną ilość argumentów z kluczem
# def to_lubie(** rzeczy):
#     for cos in rzeczy:
#         print("To jest ")
#         print(cos)
#         print(" co lubie ")
#         print(rzeczy[cos])
#
#
# to_lubie(slodyscze="czekolada", rozrywka=["disco-polo", "moda na sukces"])
import litery as litery2
from teksty import *
a = "Ala ma kota"
piosenka.spiew()
litery.wyswietl(a)
litery2.wyswietl(a)
print(litery.dlugosc(a))

#wyświetla wszystkie zmienne oraz nazwy modułów, które się w nim znajdują
print(dir(litery2))
print(dir(litery))
