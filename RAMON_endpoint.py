#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Jun 16 17:49:01 2020
@author: lpico
"""

import getpass
import platform
import os
import socket
import psutil
from datetime import date

PATH = '/home/user/Documents/ramon/server1log.csv'

def write_row(file_, *columns):
    print(*columns, sep='\t', end='\n', file=file_)

with open(PATH, 'a+') as f:
    fecha = date.today()
    servidor =  socket.gethostname()
    procesador = platform.processor()
    for proc in psutil.process_iter():
        try:
            proceso = proc.name()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    usuario = getpass.getuser()
    sistema = platform.platform()
    version = platform.release()
    
    write_row(f,"FECHA", "SERVIDOR", "PROCESADOR", "PROCESOS ACTIVOS", "USUARIOS ACTIVOS", "SISTEMA OPERATIVO", "VERSION SISTEMA OPERATIVO")
    write_row(f,str(fecha), str(servidor), str(procesador), str(proceso), str(usuario), str(sistema), str(version))

archivo = "/home/user/Documents/ramon/server1log.csv"
fechaactual = date.today().strftime('%Y-%m-%d')
host_ip = socket.gethostbyname(socket.gethostname())
nombre_nuevo = f"{host_ip}_{fechaactual}.csv"
os.rename(archivo, nombre_nuevo)

