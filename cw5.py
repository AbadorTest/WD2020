class Ksztalty:
    __wywolanie = 0
    #definicja konstruktora
    def __init__(self, x, y):
        #deklarujemy atrybuty
        #self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.x=x
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole_prostokatu(self):
        return self.x * self.y

    def obwod(self):
        self.__wywolanie += 1
        print(self.__wywolanie)
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik


#a teraz klasa która dziedziczy po klasie Ksztalty
class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x =x
        self.y=x

#i jeszcze klasa, która dziedziczy po klasie Kwadrat
#bedzie definiwoać figurę złożoną z 3 kwadratów w kształcie litery L
# _
#| |_
#|_ _|
class KwadratowaLiteraL(Kwadrat):

    def obwod(self):
        print(self.__wywolanie)
        return 8 * self.x

    def pole_prostokatu(self):
        return 3 * self.x * self.y

# class Obiekt:
#     pass
#
# obiekt = Obiekt()
# obiekt.atrybut1 = "test"
# print(obiekt);
# print(obiekt.atrybut1);
# print(obiekt.atrybut2);
# print("inicjujemy klasę Kwadrat")
# figura = Kwadrat(5)
# figura2 = Kwadrat(5)
#
# print("figura : " , figura._Ksztalty__wywolanie)
# #sprawdzamy metody z klasy bazowej
# print(figura.pole_prostokatu())
#
# print(figura.obwod())
# print(figura.obwod())
# print(figura.obwod())
# print("figura : " , figura._Ksztalty__wywolanie)
#
# print("figura2 : " , figura2.obwod())
#
# figura.dodaj_opis("Kwadrat")
#
# print(figura.opis)
#
# figura.skalowanie(0.3)
#
# print(figura.obwod())
#
# print("inicjujemy klasę KwadratowaLiteraL")
# litera_l = KwadratowaLiteraL(5)
#
# #sprawdzamy jakie możemy wywołać metody
# # print(litera_l.obwod())
# print(litera_l.pole_prostokatu())
# litera_l.dodaj_opis("Litera L")
# print(litera_l.opis)
# litera_l.skalowanie(0.5)
# # print(litera_l.obwod())
imie = "Reks"
# it = iter(imie)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# class Wspak:
#     """Iterator zwracający wartości w odwróconym porządku"""
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]
# it = Wspak(imie)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# def reverse(data):
#     for index in range(len(data)-1, -1, -1):
#         yield data[index]
#
#
# gen = reverse("Feliks")
# print(next(gen))
# print("Marek")
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
litery = (litera for litera in "Zdzisław")
print(litery)
print(next(litery))
print(next(litery))
print(next(litery))
print(next(litery))
