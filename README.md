# RAMON
DESCRIPCION

Generalidades

RAMON es un programa desarrollado en Python versión 3.X, el cuál se compone de dos aplicaciones:

•	RAMON_endpoint. Agente liviano con la capacidad de consultar información del sistema operativo Linux Ubuntu y resguardarla en un archivo con extensión.csv. Este programa viene con un script en BASH para que se ejecute automáticamente RAMON_endpoint una vez al día.

•	RAMON_API. Aplicación con la capacidad de recopilar la información generada por los agentes y centralizarla en un archivo ya sea de tipo .csv o formato JSON, adicionalmente la aplicación esta en capacidad de guardar la información en una base de datos mySQL.

Requerimientos

Los requerimientos para la instalación de RAMON se enumeran a continuación.

Tabla 1 Requerimientos RAMON_endpoint
HARDWARE	SOFTWARE
2 GHz dual core processor	Python reléase 3.x 
4 GiB RAM (system memory)	Sistema operativo Linux Ubuntu
25 GB of hard-drive space	Aplicación FTP 
	Librerias Python (getpass, platform, os, socket, psutil, datetime)
	BASH 5.x

Tabla 2 Requerimientos RAMON_API
HARDWARE	SOFTWARE
2 GHz dual core processor	Python reléase 3.x 
4 GiB RAM (system memory)	Sistema operativo Linux Ubuntu
25 GB of hard-drive space	Libreria (ftplib, pandas, csv, json)

INSTALACIÓN

Para la instalación se deben cumplir con los anteriores requerimientos, se debe garantizar que exista alcanzabilidad IP entre el servidor RAMON_API y todos los servidores que tengan instalado el agente RAMON_endpoint, deben otorgarse permisos en equipos de ciberseguridad y red para el protocolo TCP puertos 20 y 21.

Los pasos para el inicio de instalación se describen a continuación:

1.	Descargar los archivos:
a.	RAMON_endpoint.py
b.	RAMON_API.py
c.	RAMON_persistent.sh
2.	Validar el valor hash de los dos archivos para verificar su integridad:
a.	$shasum -a 256 RAMON_endpoint.py 
El valor debe ser: 59ff55da91f72d5aa66f2ffa3bd20d52f2a398656dd93ff8ee051614d7af8532
b.	$shasum -a 256 RAMON_API.py
El valor debe ser: 69154574314cbbd4e550184d81a0c95871ae9c1f9bc3a71c03f09cb223c027be
c.	$shasum -a 256 RAMON_persistent.sh
El valor debe ser: ba66c9ce5f5d8bb97ab0f5d55fc7fdeaace2b2596f2916c0691136b6af66103f
3.	Verificar cumplimiento de los requerimientos de instalación.

4.	Comprobar la conectividad entre los agentes y la API central, ejecutando los siguientes comandos desde el servidor que va a contener la aplicación RAMON_API.py:
a.	$ ping “server_ip_address”
b.	$ telnet “server_ip_adress” 21

Una vez culminan los anteriores pasos seguimos con la instalación de la aplicación RAMON_endpoint.py en los servidores en los cuales vamos a obtener la información de compliance requerida, a continuación se describen las actividades:

1.	Habilitar un usuario y contraseña para el servicio FTP, esta información después será configurada en la aplicación RAMON_API.py.
2.	Crear la siguiente carpeta en el home del usuario creado en el paso anterior:
a.	/home/user/Documents/ramon/
3.	Guardar los archivos RAMON_persisten.sh y RAMON_endpoint.py en la carpeta anterior.
4.	Otorgar permisos de ejecución a las anteriores aplicaciones.

Una vez culminan los anteriores pasos seguimos con la instalación de la aplicación RAMON_API.py en el servidor central el cuál va a recopilar la información de los agentes, a continuación se describen las actividades:

1.	Crear la siguiente carpeta en el home del usuario creado en el paso anterior:
a.	/home/user/Documents/ramonapi/
2.	Guardar el archivo RAMON_API.py en la carpeta anterior.
3.	Otorgar permisos de ejecución a la aplicación RAMON_API.py

OPERACIÓN

A continuación se explican los pasos para el uso de RAMON.

1.	Conéctese remotamente o localmente a la línea de comando del servidor donde este desplegado el agente.
2.	Vaya al directorio “/ramon” creado en la instalación y ubíquese en el directorio.
3.	Se procederá a ejecutar un script que va a extraer los resultados automáticamente una vez al día, para esto ejecute el script:
a.	$ ./RAMON_persistent.sh
4.	Verifique que se ha generado el archivo con el siguiente formato:
a.	<IP de servidor>_<AAAA-MM-DD>.csv
5.	Conéctese remotamente o localmente a la línea de comando del servidor que tiene la aplicación RAMON_API.py
6.	Vaya al directorio “/ramonapi” creado en la instalación y ubíquese en el directorio.
7.	Para la extracción del archivo que contiene toda la información de los servidores, ejecute:
a.	Python3 RAMON_API.py
8.	En la carpeta que esta ubicado se generaran los siguientes archivos:
a.	consolidado.csv
b.	consolidad.json
9.	
