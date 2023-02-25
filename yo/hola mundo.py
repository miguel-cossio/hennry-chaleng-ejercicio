# ejercicoi 1
# Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e 
# imprimir por pantalla
ciudadesDelMundo=["madrid", "La Paz", "vogota", "verlin", "tokio"];
print(ciudadesDelMundo);



# 2) Imprimir por pantalla el segundo elemento de la lista
print (ciudadesDelMundo[1])

# 3) Imprimir por pantalla del segundo al cuarto elemento
print (ciudadesDelMundo[1:4])

# 4 Visualizar el tipo de dato de la lista

print(type(ciudadesDelMundo))
#Visualizar todos los elementos de la lista a partir del tercero de manera genérica,
# es decir, sin explicitar la posición del último elemento
print(ciudadesDelMundo[0:])

# 5)Visualizar los primeros 4 elementos de la lista
print(ciudadesDelMundo[:4])

# 6)Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún 
# tipo de error?
ciudadesDelMundo.append("ciudad de andresotopia")
ciudadesDelMundo.append("ciudad de mexico")

# 7)Agregar otra ciudad, pero en la cuarta posición
ciudadesDelMundo.insert(3, 'Quito')
print(ciudadesDelMundo)

# 8) Concatenar otra lista a la ya creada
new_list=["new yorck", "las vegas"]
ciudadesDelMundo.extend(new_list)
print(ciudadesDelMundo)
# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada.
# ¿Se nota alguna particularidad?
print(ciudadesDelMundo.index("ciudad de andresotopia"))
# ¿Qué pasa si se busca un elemento que no existe?

# Eliminar un elemento de la lista
ciudadesDelMundo.remove("ciudad de andresotopia")
print(ciudadesDelMundo)
# ¿Qué pasa si el elemento a eliminar no existe?

# Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
ultimo = ciudadesDelMundo.pop()
print(ultimo)

# Mostrar la lista multiplicada por 4
print(ciudadesDelMundo*4)

# Crear una tupla que contenga los números enteros del 1 al 20
enteros = tuple(range(1, 21))
print(enteros)
# Imprimir desde el índice 10 al 15 de la tupla
print(enteros[9:15])
# Evaluar si los números 20 y 30 están dentro de la tupla
print(20 in enteros)
print(30 in enteros)

# Con la lista creada en el punto 1, validar la existencia del elemento 'París' 
# y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
if "paris" in ciudadesDelMundo:
    print("si esta la ciudad")
else :
    ciudadesDelMundo.append("paris")
    print("se agrego la ciudad de paris")

# Mostrar la cantidad de veces que se encuentra un elemento específico dentro de 
# la tupla y de la lista
print(enteros.count(10))
print(ciudadesDelMundo.count("paris"))
# Convertir la tupla en una lista
list=[enteros]
print(list)

# Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
a, b, c, *sobrante = enteros
print(a)  
print(b)  
print(c) 


# Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave 
# "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".
diccionario={"ciudad": ciudadesDelMundo, 
             "País": ['Brasil','Paraguay','Ecuador','Uruguay','Chile','Perú','Venezuela','Colombia','Méjico','Uruguay','España','Italia','Francia'], 
'Continente' : ['América','América','América','América','América','América','América','América','América','América','Europa','Europa','Europa']}

# Imprimir las claves del diccionario
print(diccionario.keys())
# Imprimir las ciudades a través de su clave

