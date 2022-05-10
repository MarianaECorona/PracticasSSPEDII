'''
*******
*
* Practica 7 TDA : Cola 
* SSPEDII seccion D11
* Corona Yanez Mariana Elizabeth
*
*******
'''
#Cola aplicada a un horario
#implemetancion usando una lista ligada

import os

#Nodo 
class Schedule:
    def __init__(self,activity):
        self.activity = activity
        self.next = None
#Cola
class Queue:
    #inicializar 
    def __init__(self):
        self.front = Schedule("front")
        self.back = Schedule("back")
        self.front =  self.back = None
    #vacia
    def empty(self):
        return self.front == None
    #Encolar
    def enqueue(self,activity):
        temp = Schedule(activity)

        if self.back == None:
            self.front = self.back = temp
            return
        self.back.next = temp
        self.back = temp
    #Desencolar
    def dequeue(self):
        if self.empty():
            pass
        temp = self.front
        self.front = temp.next

        if self.front == None:
            self.back = None
    #frente
    def front_queue(self):
        return self.front.activity
    #ultimo
    def back_queue(self):
        return self.back.activity

    #Representacion en cadena 
    def __str__(self):
        cur = self.front
        out = ""
        while cur:
            out += str(cur.activity) + " -> "
            cur = cur.next
        return out[:-3]
    
#main 
if __name__ == '__main__':
    queue = Queue()
    
    queue.enqueue('Desayunar')
    print("Actividad agragada\n")
    queue.enqueue('Pasear al perro')
    print("Actividad agragada\n")
    queue.enqueue('Revisar correos')
    print("Actividad agragada\n")
    queue.enqueue('Junta')
    print(f"Cola:\n {queue}")

    queue.dequeue()
    print("Actividad removida\n")
    queue.dequeue()
    print("Actividad removida\n")

    print("Actividad siguiente:\n")
    print(queue.front_queue())
    
    
