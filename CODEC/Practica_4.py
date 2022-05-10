'''
*******
*
* Practica 4 CODEC
* SSPEDII seccion D11
* Corona Yanez Mariana Elizabeth
*
*******
'''

import os
from msvcrt import getch
def pause():
    print("PRESIONA [ENTER]PARA CONTINUAR...")
    getch()

while True:
    os.system("cls")
    print("""" Bienvenido\n
    1)Encriptar
    2)Descriptar
    3)Salir\n\n
    """)
    op = int(input("[OPCION]: "))
    if op == 1:
        #Abrir el archivo
        file = open("cancion.txt", "r")
        #Leer el archivo
        text = file.read().rstrip('\n')
        #Numero de espacios recorridos
        key = 3

        def encryptCaesar(text,key):
            result = ""
            for i in range(len(text)):
                char = text[i]#caracter x linea
                #Caso espacio
                if char == ' ':
                    result += ' '#Agregar espacio
                #Caso Mayusculas
                elif char.isupper():
                    #result += chr((ord(char) + key-65) % 27 + 65)
                    result+=char#Dejar la mayuscula
                #Caso salto de linea
                elif char == '\n':
                    result+='\n'#Agregar los saltos
                #Caso minusculas
                else:
                    result += chr((ord(char) + key - 97) % 27 + 97)#Encriptado
            return result

        #Archivo con info encriptada
        caesar= open("cifrado.txt","w")
        caesar.write(encryptCaesar(text,key))#Escribir archivo
        caesar.close()
        file.close()
        print("Archivo Cifrado")
        pause()

    if op == 2:
        #Abrir el archivo
        file = open("cifrado.txt", "r")
        #Leer el archivo
        text = file.read().rstrip('\n')
        #Numero de espacios recorridos
        key = -3

        def desencryptCaesar(text,key):
            result = ""
            for i in range(len(text)):
                char = text[i]#caracter x linea
                #Caso espacio
                if char == ' ':
                    result += ' '#Agregar espacio
                #Caso Mayusculas
                elif char.isupper():
                    #result += chr((ord(char) + key-65) % 27 + 65)
                    result+=char#Dejar la mayuscula
                #Caso salto de linea
                elif char == '\n':
                    result+='\n'#Agregar los saltos
                #Caso minusculas
                else:
                    result += chr((ord(char) + key - 97) % 27 + 97)#Desncriptado
            return result
        
        #Archivo con info desencriptada
        caesar= open("decifrado.txt","w")
        caesar.write(desencryptCaesar(text,key))#Escribir archivo
        caesar.close()
        file.close()
        print("Archivo Decifrado")
        pause()

    if op == 3:
        break