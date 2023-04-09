#Se hace uso de la clase Punto
"""
Revisen bien que lo que importan se mantenga con el mismo nombre (además recuerden que no puede empezar con números)
"""
from clase_punto import Punto
#Se importa numpy para el sistema de ecuaciones
import numpy as np

"""
0
Está todo MUY MUY MUY MUY MUY MAL
Hay errores de sintanxis, coherencia, variables que se usan y no se definen,
constructores mal hechos, uso incorrecto de métodos de Punto.
Parámetros mal definidos.

Ni siquiera los nombres de los archivos que importan coinciden.

"""

#Definimos la clase Recta y todos los atributos que poseera 
class Recta:

    """
    Está mal su constructor.
    Sus atributos no van a tomar el valor que les pasen,
    de hecho no se puede definir un punto porque las x y y no tienen valor
    """
    def __init__(self, p1:object ,p2:object):
        self.p1 = Punto (x1,y1)
        self.p2 = Punto (x2,y2)


    """
    Por qué querríamos pasarle como parámetro los puntos al método de la recta para obtener
    la pendiente si los puntos es como se inicializa la recta?
    """
    def pendiente(self, Punto (x1,y1):object, Punto (x2,y2):object):
        """
        Están creado un atributo, es decir, esta variable self.dist_y (también la de x) serán parte de la clase y no sólo
        varibles dentro del método

        self.p1 (y p2) serán objetos Punto (bueno la idea es que lo sean, pero por el error en el constructor no lo son),
        y como objetos punto si es factible obtener los valores de x y y, pero son atributos privados, no van a poder obtenerlos así.
        Usen los métodos get que se definieron en la clase Punto
        """
        self.dist_y = self.p2.y - self.p1.y
        """
        No tendría que haber identación aquí
        """
	      self.dist_x = self.p2.x - self.p1.x

	"""
        dist_y y dist_x no están definidos, esto no va a servir
        """
        if dist_y < 0 and dist_x < 0:
          self.dist_y = abs(dist_y)
          self.dist_x = abs(dist_x)

        """
        el elif no tiene código dentro
        """
        elif dist_x < 0:
            
        self.dist_y = -(dist_y)
        self.dist_x = abs(dist_x)

        """
        Esta identación?
        """
	      pendiente_recta = dist_y/dist_x
	      return pendiente_recta

	    
    """
    Otro cosntructor?
    Si es posible tener otro contructor y el objeto se inicia dependiendo de los parámetros que se agreguen
    pero este constructor está mal primero por que estamos definiendo la recta a partir de dos puntos, y después porque está
    mal estructurado.
    """
#Se definen los valores para la recta ax+by+c=0        
    def __init__(self,a,b,c):
        """
        dis_y y dis_x no están definidos
        """
        self.a=dist_y
        self.b=dist_x
        self.c= ((dist_y * self.p1.x ) - (dist_x * self.p1.y))

    """
    No hemos visto la estructura try except 
    """
#Obtener ordenada al origen         
    def ordenada_origen (self):
        try:
            return -(self.c/self.a)
        except ZeroDivisionError:
            return None

#criterio de pertenencia a la recta     
    def esta_en_recta(self, punto):
        """
        Los atributos de punto no son públicos.
        """
        if (self.a*punto.x+self.b*punto.y+self.c)==0:
            return True
        else:
            return False
        
#Criterio de paralelismo
    """
    Y dondé definen la pendiente como un objeto?
    
    Pediente1 y pendiente2 no están definidas
        
    """
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
        """
        No son públicos los atrubutos de punto.
        """
        x1,y1 = self.p1.x,self.p1.y
        """
        Identación para qué?
        """
	      x2,y2 = self.p2.x,self.p2.y
	      """
              Aquí se va a quedar literalmente como ((x1,y1), (x2,y2))
              """
	      recta = "((x1,y1), (x2,y2))"
	      """
              Dos return? 
              """
	      return recta
	"""
        dist_y y dist_x no están definidas
        """
        return "m =" + str(dist_y) + "/" + str(dist_x)
        
#Criterio de rectas iguales    
    def __eq__(self, otra_recta:object)->bool:
        return self.a == otra.a and self.b == otra.b and self.c == otra.c
        
