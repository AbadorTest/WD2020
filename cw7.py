# import numpy as np
# #inicjujemy dane
# a = np.array( [20,30,40,50] )
# b = np.arange( 4 )
# print(a)
# print(b)
# #Wykonujemy operację i zapisujemy do nowej zmiennej
# c = a-b
# print(c)
# #Wykonujemy operację: kwadrat zawartości
# print(b**2)
# #Możemy również zmodyfikować obecne zmienne
# print(a)
# a+=b
# print(a)
# a-=b
# print(a)
# import numpy as np
# b = np.arange(12).reshape(3,4)
# print(b)
# # suma całej macierzy
# print(b.sum())
# # suma każdej z kolumn
# print(b.sum(axis=0))
# # minimum każdego rzędu
# print(b.min(axis=1) )
# # skumulowana suma dla rzędu
# print(b.cumsum(axis=1) )
# import numpy as np
# #inicjujemy dane
# a = np.arange( 3 )
# b = np.arange( 3 )
# print(a.dot(b)) # iloczyn macierzy
# print(np.dot(a,b)) # inny sposób
# import numpy as np
# #Macierz całkowita
# a = np.ones(3, dtype=np.int32)
# print(a.dtype.name)
# #Macierz zmiennoprzecinkowa
# b = np.linspace(0,np.pi,3)
# print(b.dtype.name)
# #Wynikiem jest macierz zmiennoprzecinkowa
# c = a+b
# print(c)
# print(c.dtype.name)
# #Wynikiem jest macierz liczb zespolonych
# d = np.exp(c*1j)
# print(d)
# print(d.dtype.name)
# import numpy as np
# b = np.arange(3)
# print(b)
# print(np.exp(b))
# print(np.sqrt(b))
# c = np.array([2., -1., 4.])
# print(np.add(b, c))
# import numpy as np
# #generujemy macierz 3x2
# b = np.arange(6).reshape(3,2)
# print(b)
# for a in b:
# #iterujemy wzdluż pierwszej osi
#     print(a)
# import numpy as np
# #generujemy macierz 3x2
# b = np.arange(6).reshape(3,2)
# print(b)
# print(b.flat)
# for a in b.flat:
# #iterujemy jakby to była macierz płaska
#     print(a)
# import numpy as np
# #generujemy macierz 1x6
# b = np.arange(6)
# print(b)
# print(b.shape)
# #generujemy macierz 3x3
# c = np.array([np.arange(3), np.arange(3), np.arange(3)])
# print(c)
# print(c.shape)
import numpy as np
#generujemy macierz 1x6
b = np.arange(6)
print(b)
print(b.shape)
#przeksztalacamy ja na macierz 2x3
c = b.reshape((2,3))
print(c)
print(c.shape)
#przeksztalacamy ja na macierz 3x2
d = c.reshape((3,2))
print(d)
print(d.shape)
#spłaszczamy macierz zyskujac pierwotny kształt ze zmiennej b
e = d.ravel()
print(e)
print(e.shape)
#transpozycja macierzy
f = c.T
print(f)
print(f.shape)