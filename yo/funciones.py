# Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es
def primo_o_no (numero):
    divisores=[]
    for div in range(1,numero+1):
        if numero % div==0:
            divisores.append(div)
    if len(divisores) >= 3:
        
        return False
    else:
        
        return True
print(primo_o_no(10))
# # 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista 
# # de números y devuelva sólo aquellos que son primos en otra lista
# def extrae_primos_de_lista(lista):
#     lista_primo=[]
#     for elemnto in lista:
#         if primo_o_no(elemnto):
#             lista_primo.append(elemnto)
            
#     return lista_primo
# lis=[25,23245,23452,35,2345,235,2345,2345,2345,3,2,1,11]
# extraer_primo = extrae_primos_de_lista(lis)
# print(extraer_primo)
# # 5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin
# # Fórmula 1 : (°C × 9/5) + 32 = °F
# # Fórmula 2 : °C + 273.15 = °K
# # Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destinolista
lista=["hola", "a", "todos","hola", "a", "todos"]
print(lista.count("hola"))

