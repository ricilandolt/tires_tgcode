import requests
import pandas as pd
import re 
df = pd.read_csv("TG-Automobil.txt", encoding='cp1252',sep='\t', on_bad_lines="skip" )
prepdf = df.loc[df['01 Fahrzeugart'].str.contains('PERSONENWAGEN'),:]
prepdf = df.loc[:,['Typengenehmigungsnummer','70 Reifen Felgen','69 Reifen Felgen','71 Reifen Felgen','54 Achsgarantie v von',
'54 Achsgarantie v bis',
'54 Achsgarantie h von',
'54 Achsgarantie h bis','19 Fahrzeug Vmax mech von',
'19 Fahrzeug Vmax mech bis',
'19 Fahrzeug Vmax autom von',
'19 Fahrzeug Vmax autom bis']]
prepdf.fillna('', inplace = True)
prepdf['string'] =  prepdf[['69 Reifen Felgen', '70 Reifen Felgen','71 Reifen Felgen']].apply(' '.join, axis = 1)

axispattern = '([vh]\\s*[=/+]+?h?)'
rimpattern = '([0-9]?\\s?[0-9.,/]+\\s*([xJX]{1,2})([0-9.]{1,3})\\s*ET\\s?[-+0-9.]+)'
dimpattern = r"""((v|h|v(\+|/)h)=)?\s*?([0-9]{2,3}/[0-9]{2,3}\s*\(?Z?\)?RF?\s?([0-9]{2,3})C?\s*X?L?\s*\(?([0-9]{2,3}[A-Z])?\)?\s?(M\+S)?\s?([0-9]{2,3}[A-Z])?).*?"""
res = prepdf.string.str.split(dimpattern)

#for every string of the three dim extracted strings there are three rims strings extracted 
tyres = pd.concat([res.str.get(i) for i in range(4,len(res[res.index[0]]),9)])
rims = pd.concat([res.str.get(i).str.findall(rimpattern) for i in range(9,len(res[res.index[0]]),9)])

axis = [res.str.get(i) for i in range(2,len(res[res.index[0]]),9)]
tgcodes = pd.concat([prepdf.Typengenehmigungsnummer for i in range(len(axis))])
for i in range(len(axis)-1): 
    axis[i+1] = axis[i+1].combine_first(axis[i])
axis = pd.concat([ax.fillna('v+h').str.findall('([vh])') for ax in axis])

nesteddf = pd.DataFrame({'tgcode':tgcodes, 'tyres':tyres, 'rims':rims, 'axis':axis})

tgdf = nesteddf.explode('rims')
tgdf.rims = tgdf.rims.str.get(0)
tgdf = tgdf.explode('axis')
tgdf = tgdf[~tgdf['tyres'].isnull()].drop_duplicates()

tgdf.to_csv('tgdata.csv',index = False, sep = ';')