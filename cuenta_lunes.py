# -*- coding: utf-8 -*-
"""
Este programa calcula la cantidad de lunes entre dos fechas

"""

from datetime import datetime, timedelta

fecha_ini = datetime(2024, 11, 1)
fecha_fin = datetime(2024, 11, 30)

num_dias_mes = (fecha_fin - fecha_ini).days + 1
dia_1 = fecha_ini.weekday()
num_lunes = 0

# 0: lunes; 1:martes; ...

for i in range(num_dias_mes):
    if ((fecha_ini + timedelta(days = i)).weekday()) == 0:
        num_lunes = num_lunes + 1
        
print(num_lunes)


# FIn de la primera parte


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.bcv.org.ve/')

bcvBS = BeautifulSoup(html, 'html.parser')

cambio = bcvBS.find('div', {'id':'dolar'}).find('strong').get_text()

print(cambio)

