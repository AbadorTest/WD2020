# import numpy as np
#
# # inicjalizacja tablicy
# a = np.arange(2)
# print(a)
# # wypisanie typu zmiennej tablicy (nie jej elementów) - ndarray
# print(type(a))
# # sprawdzenie typu danych tablicy
# print(a.dtype)
# # inicjalizacja tablicy z konkretnym typem danych
# a = np.arange(2, dtype='int64')
# print(a.dtype)
# # zapisanie kopii tablicy jako tablicy z innym typem
# b = a.astype('float')
# print(b)
# # wypisanie rozmiarów tablicy
# print(b.shape)
# # można też sprawdzić ilość wymiarów tablicy
# print(a.ndim)
#
# # stworzenie tablicy wielowymiarowej może wyglądać tak
# # parametrem przekazywanym do funkcji array jest obiekt, który zostanie skonwertowany na tablicę
# # może to być Pythonowa lista
# m = np.array([np.arange(2), np.arange(2)])
# print(m)
# # ponownie typem jest ndarray
# print(type(m))
# # wypisanie rozmiarów tablicy
# print(m.shape)
# # można też sprawdzić ilość wymiarów tablicy
# print(m.ndim)
# import numpy as np
#
# # możemy w łatwy sposób stworzyć macierz danego rozmiaru wypełnioną zerami lub jedynkami
# zera = np.zeros((5,5))
# print(zera)
# jedynki = np.ones((4,4))
# print(jedynki)
# # warto sprawdzić jaki jest domyślny typ danych takich tablic
# # można również stworzyć "pustą" macierz o podanych wymiarach, która wcale pusta nie jest
# # wartości umieszczane są losowe
# pusta = np.empty((2, 2))
# print(pusta)
#
# # do elementów tablic możemy odwołać się tak jak do elementów np. listy czyli podając indeksy
# poz_1 = pusta[1, 1]
# poz_2 = pusta[0, 1]
# print(poz_1)
#
# # funkcja arange potrafi również tworzyć ciągi liczb zmiennoprzecinkowych
# liczby = np.arange(1, 2, 0.1)
# print(liczby)
# # podobnie działa funkcja linspace, której działanie jest równoważne tej samej funkcji w MATLAB-ie
# liczby_lin = np.linspace(1, 2, 5)
# print(liczby_lin)
#
# # sprawdź również działanie funkcji logspace
#
# # a teraz możemy utworzyć dwie macierze, najpierw wartości iterowane są w kolumnie a następnie w wierszu
# z = np.indices((5, 3))
# print(z)
# # wielowymiarowe macierze możemy również generować funkcją mgrid
# x, y = np.mgrid[0:5, 0:5]
# print(x, y)
#
# # podobnie jak w MATLAB-ie możemy tworzyć macierze diagonalne
# mat_diag = np.diag([a for a in range(5)])
# print(mat_diag)
# # w powyższym przykładzie stworzony wektor wartości zostanie umieszczony na głównej przekątnej macierzy
# # możemy podać drugi parametr funkcji diag, który określa indeks przekątnej względem głównej przekątnej,
# # która zostanie wypełniona wartościami podanego wektora
# mat_diag_k = np.diag([a for a in range(5)], -2)
# print(mat_diag_k)
#
# # Numpy jest w stanie stworzyć tablicę jednowymiarową z dodolnego obiektu iterowalnego (iterable)
# z = np.fromiter(range(5), dtype='int32')
# print(z)
# # ciekawą funkcją Numpy jest funkcja frombuffer, dzięki której możemy stworzyć np. tablicę znaków
# marcin = b'Marcin'
# mar = np.frombuffer(marcin, dtype='S1')
# mar_2 = np.frombuffer(marcin, dtype='S2')
# print(mar)
# print(mar_2)
# # powyższa funkcja ma jednak pewną wadę dla Pythona 3.x, która powoduje, że trzeba jawnie określać
# # iż ciąg znaków przekazujemy jako ciąg bajtów co osiągamy poprzez podanie litery 'b' przed wartością
# # zmiennej tekstowej. Można podobny efekt osiągnąć inaczej, sprawdź poniższe przykłady
# marcin = 'Marcin'
# mar_3 = np.array(list(marcin))
# mar_3 = np.array(list(marcin), dtype='S1')
# mar_3 = np.array(list(b'Marcin'))
# mar_3 = np.fromiter(marcin, dtype='S1')
# mar_3 = np.fromiter(marcin, dtype='U1')
# print(mar_3)
# # tablice numpy możemy w prosty sposób do siebie dodawać
# mat = np.ones((2, 2))
# mat2 = np.ones((2, 2))
# mat = mat + mat2
# print(mat)
# # odejmować
# print(mat - mat2)
# # mnożyć
# print(mat * mat)
# # dzielić
# print(mat / mat)
#
import numpy as np
# cięcie (slicing) tablic numpy można wykonać za pomocą wartości z funkcji slice lub range
a = np.arange(10)
s = slice(2, 7, 2)
print(a)
print(s)
print(a[s])
s = range(2, 7, 2)
print(a[s])
# # możemy ciąć tablice również w sposób znany z cięcia list (efekt jak wyżej)
print(a[2:7:2])
# # lub tak
print(a[1:])
print(a[2:5])
# w podobny sposób postępujemy w przypadku tablic wielowymiarowych
mat = np.arange(25)
# teraz zmienimy kształt tablicy jednowymiarowej na macierz 5x5
mat = mat.reshape((5,5))
print(mat)
print(mat[1:])  # od drugiego wiersza
print(mat[:,1])  # druga kolumna jako wektor
print(mat[...,1])  # to samo z wykorzystaniem ellipsis (...)
print(mat[:,1:2])  # druga kolumna jako ndarray
print(mat[:,-1:])  # ostatnia kolumna
print(mat[1:3, 2:4])  # 2 i 3 kolumna dla 3 i 5 wierszu
print(mat[:, range(2,6,2)])  # 3 i 5 kolumna
# bardziej zaawansowane, lecz trudniejsze do zrozumienia cięcie można osiąnąć wg. poniższego przykładu
# y będzie tablicą zawierającą wierzchołki macierzy x
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
rows = np.array([[0, 0]])
cols = np.array([[0, 2], [0,2]])
y = x[rows]
