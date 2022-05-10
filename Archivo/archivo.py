#Pratica 2: Lectura de Archivos 
#SSPEDII seccion: D11
#Corona Yanez Mariana Elizabeth

#paso 1 abrir el archivo
archivo = open("cancion.txt","r")

#paso 2 procesar el archivo
for linea in archivo:
    print(linea.rstrip("\n"))#Eliminar el salto de linea extra

#paso 3 cerrar el archivo
archivo.close()