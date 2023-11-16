import matplotlib.pyplot as plt
import pandas as pd
from . import postproc


lista = []
for opt in voting.postproc:

lista.append([opt.option], [opt.postproc])

df_votes=pd.DataFrame(lista, columns = ['Option', 'Votes'])

plt.bar(df_votes['Option'], df_votes['Votes'])
plt.show()