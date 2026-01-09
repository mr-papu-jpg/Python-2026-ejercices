def obtener_elemento(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        print("Indice fuera de rango")
    except Exception as e :
        print(f"Algo salio mal: el error fue un {e}")
    else:
        print("Archivo leido con exito")

#Prueba de la funcion

list_1=[1, 2, 3, 4, 5]
list_2=[9, 8, 7, 6, 5, 4, 3]

obtener_elemento(list_1, 5)
obtener_elemento(list_2, "r")
print(obtener_elemento(list_2, 5))
