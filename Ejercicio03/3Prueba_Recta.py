from clase_recta import Recta

if __name__ == "__main__":

#Aqui esta la parte que imprimiria el script de la parte del __str__ de la clase Recta"
    punto1 =  int(input(Punto()))
    punto2 = int(input(Punto()))
    recta1 = (punto1,punto2).ecuacion
    pendiente1= recta1.pendiente
    ordenada1 = recta1.ordenada_origen
#Se escribe los parametros inciales
  print("Los puntos ingresados son", punto1, punto2)
  print("La ecuación de la recta es:", recta1)
  print("La pendiente de la recta es:", pendiente1)
  print("La ordenada al origen es:", ordenada1 ) 

#Menu adicional para el resto de funciones que se quieran realizar
    while(True):
        print(" \n[0] Salir"+
           "\n[1] Comprobar si un punto pertenece a la recta  " +
           "\n[2] Comprobar si dos rectas son paralelas "+
           "\n[3] Comprobar si dos rectas son perpendiculares"+
           "\n[4] Encontrar la intersección entre dos rectas")      
        opcion = int(input("Escribe una opción adicional a realizar:"))

        if opcion == 0:
            print("Fin del programa")
            break
        elif opcion == 1:
            print("El punto ingresado")
            x3 = float(input("Dame primer coordenada: "))
            y3 = float(input("Dame segunda coordenada: "))
            punto3 =  Punto(x3,y3)
            punto_pertenece = punto3.esta_en_recta

            print("¿El punto esta en la recta?:", punto_pertenece)
            
        elif opcion == 2:
            print("Criterio de paralelismo")
            x3 = float(input("Dame primer coordenada: "))
            y3 = float(input("Dame segunda coordenada: "))
            punto3 =  Punto(x3,y3)
            x4 = float(input("Dame primer coordenada: "))
            y4 = float(input("Dame segunda coordenada: "))
            punto4 =  Punto(x4,y4)

            pendiente_iguales = (punto3,punto4).rectas_paralelas

            print("¿Las rectas son paralelas?:", pendiente_iguales)

        elif opcion == 3:
            print("Criterio de perpendicularidad")
            x3 = float(input("Dame primer coordenada: "))
            y3 = float(input("Dame segunda coordenada: "))
            punto3 =  Punto(x3,y3)
            x4 = float(input("Dame primer coordenada: "))
            y4 = float(input("Dame segunda coordenada: "))
            punto4 =  Punto(x4,y4)

            rectas_perpendiculares = (punto3,punto4).rectas_perpendiculares

            print("¿Las rectas son perpendiculares?:", rectas_perpendiculares)

            
        elif opcion == 4:
            print("Punto de intersección")
            x3 = float(input("Dame primer coordenada: "))
            y3 = float(input("Dame segunda coordenada: "))
            punto3 =  Punto(x3,y3)
            x4 = float(input("Dame primer coordenada: "))
            y4 = float(input("Dame segunda coordenada: "))
            punto4 =  Punto(x4,y4)

            x = (punto3,punto4).rectas_perpendiculares
            y = (punto3,punto4).rectas_perpendiculares
            punto_cruze = Punto(x,y)

            print("Las rectas son paralelas:", punto_cruze)
   
        else:
            print("Escribe una opción válida")
