# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# # korzystając z funkcji random oraz date_range możemy wygenerować szereg czasowy danych
# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2015', periods=1000))
# # funkcja biblioteki Pandas generująca skumulowana sumę kolejnych elementów
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
#
#
# data = {'Kraj': ['Belgia',  'Indie',  'Brazylia', 'Polska'],
# 'Stolica': ['Bruksela',  'New Delhi',  'Brasilia', 'Warszawa'],
# 'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
# 'Populacja': [11190846, 1303171035, 207847528, 38675467]}
# df = pd.DataFrame(data, columns=['Kraj',  'Stolica', 'Kontynent', 'Populacja'])
# print(df)
#
# grupa = df.groupby(['Kontynent']).agg({'Populacja':['sum']})
# print(grupa)
# wykres = grupa.plot.bar()
# wykres.set_ylabel('Mld')
# wykres.set_xlabel('Kontynent')
# wykres.legend()
# plt.title('Populacja z podziałem na kontynenty')
# plt.show()

#
# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_csv('dane.csv', delimiter=';')
# grupa = df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia':['sum']})
# # wykres kołowy z wartościami procentowymi sformatowanymi z dokładnością do 2 miejsc po przecinku
# wykres = grupa.plot.pie(subplots=True, autopct='%.2f', fontsize=20, figsize=(12, 8))
# plt.title('Suma zamównień dla sprzedawcy')
# plt.show()
#


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# korzystając z funkcji random oraz date_range możemy wygenerować szereg czasowy danych
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2015', periods=1000))
# funkcja biblioteki Pandas generująca skumulowana sumę kolejnych elementów
ts = ts.cumsum()
#rzutowanie Serien na DataFrame
df = pd.DataFrame(ts)
# dodanie nowej kolumny i wykorzystanie funkcji rolling do stworzenia kolejnych wartości średniej kroczącej
df['MA'] = df.rolling(window=50).mean()
df.plot()
plt.show()

