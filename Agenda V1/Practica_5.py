'''
*******
*
* Practica 5 Agenda V1 
* SSPEDII seccion D11
* Corona Yanez Mariana Elizabeth
*
*******
'''
import os
from msvcrt import getch

class Student:
    def __init__(self, id, name, major):
        self.id = id
        self.name = name
        self.major = major

class Agenda:
    #Inicializar
    def __init__(self):
        self.students = []
    
    #Archivo:
    #Crear
    def createFile(self):
        file = open("agenda.txt", "a")
        file.close()
    #Escribir
    def writeFile(self):
        file = open("agenda.txt", "w")
        self.students.sort()
        for student in self.students:
            file.write(student+"\n")
        file.close()
    #Cargar
    def loadAgenda(self):
        file = open("agenda.txt", "r")
        line = file.readline()
        if line:
            while line:
                if line[-1] == '\n':#Separar
                    line = line[:-1]
                self.students.append(line)
                line = file.readline()
        file.close()

    def addStudent(self):
        id =input("Codigo: ")
        name = input("Nombre: ")
        major = input("Carrera: ")
        self.students.append(id+"$"+name+"$"+major)#delimitar con $

    def printStudent(self):
        self.students.sort()
        for student in self.students:
            std = student.split('$')#Separar los datos delimitados
            print("*-*-*-*-*-*-*-*-*-*-*")
            print("Codigo: "+std[0])
            print("Nombre: "+std[1])
            print("Carrera: "+std[2])
            print("*-*-*-*-*-*-*-*-*-*-*")
    #Esperar entrada para continuar
    def pause(self):
        print("PRESIONA [ENTER]PARA CONTINUAR...")
        getch()

def menu():
    agenda = Agenda()
    #Crear y cargar el archivo
    agenda.createFile()
    agenda.loadAgenda()
    
    while True:
        os.system("cls")
        print(""" 
        \n******Bienvenido selecciona una opcion*******\n
        1)Agregar un estudiante
        2)Mostrar lista de estudiantes
        3)Salir\n\n
        """)

        try:
            controller = int(input("[OPCION]: "))
        except:
            print("Opcion Invalida")
            input("[OPCION]: ")
            continue

        if controller == 1:
            agenda.addStudent()
            agenda.pause()

        if controller == 2:
            agenda.printStudent()
            agenda.pause()

        if controller == 3:
            agenda.writeFile()
            break
        
if __name__ == "__main__":
    menu()
