import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Pokemon.csv')

## removing the # and Total columns from the dataframe
df.drop(df.columns[[0,1,4,11,12]], axis=1, inplace=True)


## renaming the column names 'Type 1' and 'Type 2' to Type_1 and Type_2
df = df.rename(columns={'Type 1': 'Type_1', 'Type 2': 'Type_2'})
df.fillna(value='missing', axis=1, inplace=True)

## we now create two dataframes, single and dual
single = df[df['Type_2'].str.contains('missing')]

dual = df[~df['Type_2'].str.contains('missing')]


hp_single = round(np.sum(single['HP'].values, axis = 0) / single.shape[0])
atk_single = round(np.sum(single['Attack'].values, axis = 0) / single.shape[0])
def_single = round(np.sum(single['Defense'].values, axis = 0) / single.shape[0])
spatk_single = round(np.sum(single['Sp. Atk'].values, axis = 0) / single.shape[0])
spdef_single = round(np.sum(single['Sp. Def'].values, axis = 0) / single.shape[0])
speed_single = round(np.sum(single['Speed'].values, axis = 0) / single.shape[0])

hp_dual = round(np.sum(dual['HP'].values, axis = 0) / dual.shape[0])
atk_dual = round(np.sum(dual['Attack'].values, axis = 0) / dual.shape[0])
def_dual = round(np.sum(dual['Defense'].values, axis = 0) / dual.shape[0])
spatk_dual = round(np.sum(dual['Sp. Atk'].values, axis = 0) / dual.shape[0])
spdef_dual = round(np.sum(dual['Sp. Def'].values, axis = 0) / dual.shape[0])
speed_dual = round(np.sum(dual['Speed'].values, axis = 0) / dual.shape[0])

##x = np.array([1,2])
##y = np.array([hp_single,hp_dual])
##plt.bar(x[0],y[0],color='r',label = 'Single',width = 0.2)
##plt.bar(x[1],y[1],color='b', label = 'Dual',width = 0.2)
##plt.xlabel("Type(Single/Dual)",fontsize = 12)
##plt.ylabel("HP",fontsize = 12)
##plt.legend()
##plt.show()

##x = np.array([1,2])
##y = np.array([atk_single,atk_dual])
##plt.bar(x[0],y[0],color='r',label = 'Single',width = 0.2)
##plt.bar(x[1],y[1],color='b', label = 'Dual',width = 0.2)
##plt.xlabel("Type(Single/Dual)",fontsize = 12)
##plt.ylabel("Attack",fontsize = 12)
##plt.legend()
##plt.show()

##x = np.array([1,2])
##y = np.array([def_single,def_dual])
##plt.bar(x[0],y[0],color='r',label = 'Single',width = 0.2)
##plt.bar(x[1],y[1],color='b', label = 'Dual',width = 0.2)
##plt.xlabel("Type(Single/Dual)",fontsize = 12)
##plt.ylabel("Defense",fontsize = 12)
##plt.legend()
##plt.show()

##x = np.array([1,2])
##y = np.array([spatk_single,spatk_dual])
##plt.bar(x[0],y[0],color='r',label = 'Single',width = 0.2)
##plt.bar(x[1],y[1],color='b', label = 'Dual',width = 0.2)
##plt.xlabel("Type(Single/Dual)",fontsize = 12)
##plt.ylabel("Special Attack",fontsize = 12)
##plt.legend()
##plt.savefig('spatk_sd.png')
##plt.show()

##x = np.array([1,2])
##y = np.array([spdef_single,spdef_dual])
##plt.bar(x[0],y[0],color='r',label = 'Single',width = 0.2)
##plt.bar(x[1],y[1],color='b', label = 'Dual',width = 0.2)
##plt.xlabel("Type(Single/Dual)",fontsize = 12)
##plt.ylabel("Special Defense",fontsize = 12)
##plt.legend()
##plt.savefig('spdef_sd.png')
##plt.show()

x = np.array([1,2])
y = np.array([speed_single,speed_dual])
plt.bar(x[0],y[0],color='r',label = 'Single',width = 0.2)
plt.bar(x[1],y[1],color='b', label = 'Dual',width = 0.2)
plt.xlabel("Type(Single/Dual)",fontsize = 12)
plt.ylabel("Speed",fontsize = 12)
plt.legend()
plt.savefig('speed_sd.png')
plt.show()
