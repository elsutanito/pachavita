#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:49:01 2020
@author: lpico
"""
import ftplib
from datetime import date

fechaactual = date.today().strftime('%Y-%m-%d')
filename1 = f"192.168.49.145_{fechaactual}.csv"

#Sesion FTP para extraccion de archivos
ftp = ftplib.FTP("192.168.49.145")
ftp.login("user", "password")
ftp.cwd("/home/user/Documents/ramon")

try:
    ftp.retrbinary("RETR " + filename1 ,open(filename1, 'wb').write)
except Exception as e:
       print(str(e))
finally:
    ftp.quit()

#Unificación de archivos en uno solo
import pandas as pd

data1 = pd.read_csv('/home/user/Documents/api/consolidado.csv')
data2 = pd.read_csv(f'192.168.49.145_{fechaactual}.csv')

w=pd.concat([data1, data2])

w.to_csv('/home/lpico/Documents/api/consolidado.csv', index = False , header = True)

#convertir a json
import csv
import json

csvfile = open('/home/user/Documents/api/consolidado.csv', 'r')
jsonfile = open('/home/user/Documents/api/consolidad.json', 'w')

fieldnames = ("Fecha","Servidor","Procesador","Procesos activos", "Usuarios activos", "Sistema Operativo", "Version Sistema Operativo")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)
