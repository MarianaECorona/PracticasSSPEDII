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