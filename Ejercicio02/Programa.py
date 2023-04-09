texto = "Creo que el <h1>principito</h1> aprovechó la migración de una bandada de pájaros silvestres para su evasión.<br> La mañana de la partida, puso en orden el planeta.<br> Deshollinó cuidadosamente sus volcanes en actividad, de los cuales poseía dos, que le eran muy útiles para calentar el desayuno todas las mañanas.<hr>Tenía, además, un volcán extinguido. <hr>Deshollinó también el volcán extinguido, pues, como él decía, nunca se sabe lo que puede ocurrir. <br>Si los volcanes están bien deshollinados, arden sus erupciones, lenta y regularmente. <hr><hr>Las erupciones volcánicas son como el fuego de nuestras chimeneas. <br>Es evidente que en nuestra Tierra no hay posibilidad de deshollinar los volcanes;<br> los hombres somos demasiado pequeños.<hr>Por eso nos dan tantos disgustos."



"""
2.3

Falta generalizar, pués el código está pénsado exclusivamente para el texto que dieron, pero no para cualquiera,
las ideas en general van bien, pero hay que tener cuidado con qué estamos modificando y que realmente no queremos modificar

"""
texto_como_lista = texto.split()
lista_para_h1 = []

for palabra in texto_como_lista:
     
    if "<h1>" in palabra:
        """
        Aquí vamos a tener un problema porque no se está pensando en general,
        al separar por espacios implica que si ingresamos algo como '<h1>principito ejemplo</h1>'
        sólo se reemplaza la primer etiqueta y se pone en mayúscula sólo la primer palabra de de toda
        la parte que queríamos cambiar a mayúscula, No hay quedarnos con un mismo texto que no abarca todos los
        casos.

        Además no se borraría la etiqueta del final si hay un espacio entre el resto
        """
        palabra = palabra.replace("<h1>","").replace("</h1>","").upper()
        lista_para_h1.append(palabra)
    else:
        lista_para_h1.append(palabra)

TextoNormalizado = " ".join(lista_para_h1)

"""
Bien
"""
TextoNormalizado = TextoNormalizado.replace("<br>","\n").replace("<hr>", "\n"+80*"-"+"\n ")

palabras_por_renglon = TextoNormalizado.split("\n")

def quitarEspacios(palabra):
    if palabra[0]==" ":
        palabra = palabra.replace(" ", "", 1)
    
    return palabra

listaFinal = []

for renglon in palabras_por_renglon:
    listaFinal.append(quitarEspacios(renglon))

textoProcesado = "\n".join(listaFinal)

def dividir_cadena(input_str):
    # Dividimos la cadena en dos listas
    """
    Lo que hacen aquí es quitar los \n que había, por lo que las etiquetas html ya dejan de tener sentido
    """
    words = input_str.split()

    # Inicializamos la lista vacía
    lines = []

    # Recorremos las palabras y las agregamos a las líneas hasta que la línea cuente con 80 palabras
    line = ""

    """
    La idea iba bien pero al final sólo revisan que el texto no se pase de 80 caracteres por línea,
    sin embargo, no están los saltos de las etiquetas.
    """
    for word in words:
        if len(line) + len(word) + 1 <= 80:
            line += word + " "
        else:
            lines.append(line.strip())
            line = word + " "

    # Agregamos la última línea
    lines.append(line.strip())

    # Regresamos la lista de líneas como una cadena separada en líneas 
    return "\n".join(lines)

textoFinal = dividir_cadena(textoProcesado)

print(textoFinal)



