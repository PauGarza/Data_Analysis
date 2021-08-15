# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 14:34:59 2020

@author: pauli
"""
import pandas as pd
import numpy as np

trayectoria="C:\\Users\\pauli\\OneDrive\\Documentos\\DAI\\Proyecto2\\Data"

demographics=pd.read_csv(trayectoria+"\\Demographics.csv",encoding='UTF-8')
education=pd.read_csv(trayectoria+"\\Education.csv",encoding='UTF-8')
equity=pd.read_csv(trayectoria+"\\Equity.csv",encoding='UTF-8')
economic=pd.read_csv(trayectoria+"\\Economic.csv",encoding='UTF-8')
women=pd.read_csv(trayectoria+"\\Women.csv",encoding='UTF-8')
print(demographics)
print(education)
print(equity)
print(economic)
print(women)

#sacar las columas que voy a utilizar por tabla
demo=demographics.loc[:, ['Countries','LifeExpectancy1970', 'LifeExpectancy00', 'LifeExpectancy18']] 
edu=education.loc[:, ['Countries','CLowerM', 'CLowerF', 'LiteracyM', 'LiteracyF']] 
equ=equity.loc[:, ['Countries','Gini', 'Palma', 'GDP']] 
eco=economic.loc[:, ['Countries','GDPTotal', 'GDPHealth', 'GDPEducation', 'GDPSocial']] 
wom=women.loc[:, ['Countries','SIGI','EducationM', 'EducationF', 'FinancialM', 'FinancialF']]
print(demo)
print(edu)
print(equ)
print(eco)
print(wom)

#sacar países sin Nan
demo_datos=demo.dropna()
edu_datos=edu.dropna()
equ_datos=equ.dropna()
eco_datos=eco.dropna()
wom_datos=wom.dropna()
print(demo_datos)
print(edu_datos)
print(equ_datos)
print(eco_datos) 
print(wom_datos)

#ver qué países tiene los datos para una idea general
demo_edu=pd.merge(demo_datos, edu_datos, on ='Countries')
de_equ=pd.merge(demo_edu, equ_datos, on ='Countries')
dee_eco=pd.merge(demo_edu, eco_datos, on ='Countries')
todas=pd.merge(dee_eco, wom_datos, on ='Countries')
print(list(todas['Countries']))


#tablas con solo los paíeses que se usarán
p_demo=demo.query("Countries=='Italy' or Countries=='Mexico' or Countries=='Pakistan' or Countries=='New Zealand' or Countries=='Ghana'")
p_edu=edu.query("Countries=='Italy' or Countries=='Mexico' or Countries=='Pakistan' or Countries=='New Zealand' or Countries=='Ghana'")
p_equ=equ.query("Countries=='Italy' or Countries=='Mexico' or Countries=='Pakistan' or Countries=='New Zealand' or Countries=='Ghana'")
p_eco=eco.query("Countries=='Italy' or Countries=='Mexico' or Countries=='Pakistan' or Countries=='New Zealand' or Countries=='Ghana'")
p_wom=wom.query("Countries=='Italy' or Countries=='Mexico' or Countries=='Pakistan' or Countries=='New Zealand' or Countries=='Ghana'")
print(p_demo)
print(p_edu)
print(p_equ)
print(p_eco)
print(p_wom)


#promedios, máximos y mínimos 

#Expectativa de vida 2018
print(p_demo["LifeExpectancy18"].mean()) #74.2
print(p_demo["LifeExpectancy18"].min()) #64.0
print(p_demo['Countries'][(p_demo['LifeExpectancy18']== min(p_demo['LifeExpectancy18']) )])
print(p_demo["LifeExpectancy18"].max()) #83.0
print(p_demo['Countries'][(p_demo['LifeExpectancy18']== max(p_demo['LifeExpectancy18']) )])

#tasa de alfabetización Hombres 
print(p_edu["LiteracyM"].mean()) #93.2
print(p_edu["LiteracyM"].min()) #80.0
print(p_edu['Countries'][(p_edu['LiteracyM']== min(p_edu['LiteracyM']) )])
print(p_edu["LiteracyM"].max()) #100.0
print(p_edu['Countries'][(p_edu['LiteracyM']== max(p_edu['LiteracyM']) )])

#tasa de alfabetización mujeres 
print(p_edu["LiteracyF"].mean()) #88.4
print(p_edu["LiteracyF"].min()) #66.0
print(p_edu['Countries'][(p_edu['LiteracyF']== min(p_edu['LiteracyF']) )])
print(p_edu["LiteracyF"].max()) #100.0
print(p_edu['Countries'][(p_edu['LiteracyF']== max(p_edu['LiteracyF']) )])

#Gini (coeficiente de desigualdad económica) mientras más bajo, menos desigualdad
print(p_equ["Gini"].mean()) #37.7
print(p_equ["Gini"].min()) #33.0
print(p_equ['Countries'][(p_equ['Gini']== min(p_equ['Gini']) )])
print(p_equ["Gini"].max()) #43.5
print(p_equ['Countries'][(p_equ['Gini']== max(p_equ['Gini']) )])

#GDP per capita (current US$)
print(p_equ["GDP"].mean()) #17437.82
print(p_equ["GDP"].min()) #1466.8
print(p_equ['Countries'][(p_equ['GDP']== min(p_equ['GDP']) )])
print(p_equ["GDP"].max()) #42260.1
print(p_equ['Countries'][(p_equ['GDP']== max(p_equ['GDP']) )])

#Gasto total como % del GDP
print(p_eco["GDPTotal"].mean()) #28.1
print(p_eco["GDPTotal"].min()) #17.6
print(p_eco['Countries'][(p_eco['GDPTotal']== min(p_eco['GDPTotal']) )])
print(p_eco["GDPTotal"].max()) #41.5
print(p_eco['Countries'][(p_eco['GDPTotal']== max(p_eco['GDPTotal']) )])

#SIGI Social Institutions and Gender Index 
print(list(p_wom.query("SIGI=='Very low'")['Countries'])) #['Italy', 'New Zealand']
print(list(p_wom.query("SIGI=='Medium'")['Countries'])) #['Ghana']
print(list(p_wom.query("SIGI=='Very high'")['Countries'])) #['Pakistan']

#Inclusión financiera Hombres como %
print(p_wom["FinancialM"].mean()) #66.6
print(p_wom["FinancialM"].min()) #35.0
print(p_wom['Countries'][(p_wom['FinancialM']== min(p_wom['FinancialM']) )])
print(p_wom["FinancialM"].max()) #99.0
print(p_wom['Countries'][(p_wom['FinancialM']== max(p_wom['FinancialM']) )])

#Inclusión financiera Mujeres como %
print(p_wom["FinancialF"].mean()) #57.0
print(p_wom["FinancialF"].min()) #7.0
print(p_wom['Countries'][(p_wom['FinancialF']== min(p_wom['FinancialF']) )])
print(p_wom["FinancialF"].max()) #99.0
print(p_wom['Countries'][(p_wom['FinancialF']== max(p_wom['FinancialF']) )])

#reemplazar los SIGI a números para que sea más fácil graficar
p_wom.SIGI = p_wom.SIGI.replace({"Very low": 1, "Low": 2, "Medium": 3, "High": 4, "Very high": 5})
print(p_wom)

#plot

#hacer un df con todo
demo_edu=pd.merge(p_demo, p_edu, on ='Countries')
de_equ=pd.merge(demo_edu, p_equ, on ='Countries')
dee_eco=pd.merge(de_equ, p_eco, on ='Countries')
p_todas=pd.merge(dee_eco, p_wom, on ='Countries')
print(list(p_todas))

p_todas = p_todas.sort_values('SIGI')
print(p_todas)

#graficar SIGI vs. Expectativa de vida 2018
p_todas.plot(kind="bar",x='Countries',y='LifeExpectancy18',title="SIGI vs. Expectativa de vida")

#graficar SIGI vs. tasa de alfabetización Hombres y Mujeres
p_todas.plot(x='Countries', y=['LiteracyM','LiteracyF' ], kind="bar", title="SIGI vs. Tasa de Alfabetización")

#SIGI vs. Gini
p_todas.plot(kind="bar",x='Countries',y='Gini',title="SIGI vs. Gini")

#SIGI vs GDP per capita (current US$)
p_todas.plot(kind="bar",x='Countries',y='GDP',title="SIGI vs. GDP")

#SIGI vs GDP gasto
p_todas.plot(kind="bar",x='Countries',y='GDPTotal',title="SIGI vs. GDP Gasto")

#SIGI vs Inclusión financiera Mujeres como %
p_todas.plot(x='Countries', y=['FinancialM','FinancialF' ], kind="bar", title="SIGI vs. Inclusión financiera")

#histograma
historial=p_demo["LifeExpectancy18"].hist(bins=10)
historial=p_eco.hist(bins=10)
historial=p_edu.hist(bins=10)
historial=p_equ.hist(bins=10)
historial=p_wom.hist(bins=10)

#histograma SIGI
histo_sigi=p_wom.loc[:, ['Countries','SIGI']]
historial=histo_sigi.hist(bins=5)

#obtener la diferencia de EducationM - EducationF
dif = pd.pivot_table(p_wom,index=["Countries"],values=['EducationM', 'EducationF'],aggfunc=np.sum)
dif["Diferencia_Edu"] = dif["EducationM"]-  dif["EducationF"]
dif

#histograma de la diferencia
histo_dif=dif.loc[:, ['Diferencia_Edu']]
histo_dif
historial=histo_dif.hist(bins=5)