# plik = open("data.txt","r")
# # plik.writelines(["sdsdds\n","dssd\n","sdsdds"])
# # plik.write("sdsd")
# print(plik.read(2))
#
# #odczyt jednej lini z pliku
# print(plik.readline())
#
# #odczyt wierszy z pliku
# print(plik.readlines())
#
# #zamkniecie pliku
# plik.close()
# with open("dane.txt", "r") as plik:
#     for linia in plik:
#         print(linia, end="")


class PierwszaKlasa:
    "Przykład klasy"
    atrybut = 54321
    def __init__(self, atrybut):
        self.atrybut = atrybut
    def pierwsza_metoda(self):
        print(self.atrybut)
        return "Teraz działa pierwsza Metoda"
    def __del__(self):
        print("zamykamy", self.atrybut)
class DrugaKlasa(PierwszaKlasa):
    "Przykład klasy"

obiekt = PierwszaKlasa(1)
obiekt1 = DrugaKlasa(2)
# obiekt1.atrybut = 2323
obiekt.pierwsza_metoda()
obiekt1.pierwsza_metoda()
print(obiekt)
print(obiekt1)
# print(obiekt1.atrybut)
# print(obiekt.atrybut)
# print(PierwszaKlasa)
#
# #drukujemy atrybut
# print(obiekt.atrybut)
#
# #drukujemy metodę
# print(obiekt.pierwsza_metoda())
#
# #dodajemy atrybut do istniejącego obiektu
# obiekt.tekst = "la la la"
#
# print(obiekt.tekst)
#
# #ale go nie będzie w nowej instancji klasy
# nowy_obiekt = PierwszaKlasa()
# print(nowy_obiekt.tekst)
#
