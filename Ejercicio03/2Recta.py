#Se hace uso de la clase Punto 
from clase_punto import Punto
#Se importa numpy para el sistema de ecuaciones
import numpy as np

#Definimos la clase Recta y todos los atributos que poseera 
class Recta:
    
    def __init__(self, p1:object ,p2:object):
        self.p1 = Punto (x1,y1)
        self.p2 = Punto (x2,y2)


    def pendiente(self, Punto (x1,y1):object, Punto (x2,y2):object):
        self.dist_y = self.p2.y - self.p1.y
	      self.dist_x = self.p2.x - self.p1.x
        if dist_y < 0 and dist_x < 0:
          self.dist_y = abs(dist_y)
          self.dist_x = abs(dist_x)
        elif dist_x < 0:
        self.dist_y = -(dist_y)
        self.dist_x = abs(dist_x)
	      pendiente_recta = dist_y/dist_x
	      return pendiente_recta

#Se definen los valores para la recta ax+by+c=0        
    def __init__(self,a,b,c):
        self.a=dist_y
        self.b=dist_x
        self.c= ((dist_y * self.p1.x ) - (dist_x * self.p1.y))

#Obtener ordenada al origen         
    def ordenada_origen (self):
        try:
            return -(self.c/self.a)
        except ZeroDivisionError:
            return None

#criterio de pertenencia a la recta     
    def esta_en_recta(self, punto):
        if (self.a*punto.x+self.b*punto.y+self.c)==0:
            return True
        else:
            return False
        
#Criterio de paralelismo 
    def rectas_paralelas (self, pendiente_recta:object, otra_pendiente:object)-> bool: 
        if  pendiente1 == pendiente2
            return True
        else:
            return False

#Criterio de perpendicularidad
    def rectas_perpendiculares (self, pendiente_recta:object, otra_pendiente:object)-> bool: 
        if  pendiente1 == -1/(pendiente2) or -1/(pendiente1) == pendiente2
            return True
        else:
            return False
#Resolver el sistema de ecuaciones para encontrar interseccion         
    def encontrar_interseccion(self, recta1:object, recta2:object)->object:
        self.A = np.array([[self.a,otra.a], [self.b,otra.b ]])
        self.b = np.array([-(self.c), -(otra.c) ])
        self.x = np.linalg.solve(A, b)
        return x

#Parte str
    def __str__(self)->str:
        x1,y1 = self.p1.x,self.p1.y
	      x2,y2 = self.p2.x,self.p2.y
	      recta = "((x1,y1), (x2,y2))"
	      return recta
        return "m =" + str(dist_y) + "/" + str(dist_x)
        
#Criterio de rectas iguales    
    def __eq__(self, otra_recta:object)->bool:

        return self.a == otra.a and self.b == otra.b and self.c == otra.c
        
