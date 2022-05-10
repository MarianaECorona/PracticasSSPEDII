'''
*******
*
* Practica 7 TDA : Pila 
* SSPEDII seccion D11
* Corona Yanez Mariana Elizabeth
*
*******
'''
#Pila de Libros
#Implementacion usando una lista ligada

import os

#Clase nodo
class Book:
    def __init__(self, book):
        self.book = book
        self.next = None

#Pila 
class Stack:
    #Inicializa
    def __init__(self):
        self.head = Book("head")
        self.size = 0

    #Vacia
    def empty(self):
        return self.size == 0
    
    #Agregar
    def push(self,book):
        book = Book(book)
        book.next = self.head.next
        self.head.next = book
        self.size += 1
    
    #Remover
    def pop(self):
        if self.empty():
            pass
        removed = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return removed.book

    #Tope
    def top(self):
        if self.empty():
            pass
        return self.head.next.book
    
    #Main

if __name__ == "__main__":
    stack = Stack()
    
    stack.push("1984")
    print("Libro apilado\n")
    stack.push("Juego de Tronos")
    print("Libro apilado\n")
    stack.push("Persona Normal")
    print("Libro apilado\n")
    stack.push("Viaje al centro de la Tierra")
    print("Libro apilado\n")

    remove = stack.pop()
    print(f"Remover: {remove}\n")
    remove = stack.pop()
    print(f"Remover: {remove}\n")

    top =  stack.top()
    print(f"Libro en el tope: {top}")
