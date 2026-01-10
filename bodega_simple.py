import json

inventario= {"manzanas":10, "peras": 5}

with open("inventario.json", "w") as f:
    json.dump(inventario, f, indent=4)
    #el indent ayuda a que sea legible

with open("inventario.json", "r") as f:
    mi_diccionario= json.load(f)
    print(mi_diccionario)


print("\n--------------\n")

#prueba y practica propia
inventario_2= {"naranjas": 23, "mangos": 8}

with open("inventario.json", "w") as f:
    json.dump(inventario_2, f, indent=4)

with open("inventario.json", "r") as f:
    mi_diccionario= json.load(f)
    print(mi_diccionario)

#prueba para aniadir

"""
with open("inventario.json", "a") as f:
    json.dump(inventario, f, indent=4)

with open("inventario.json", "r") as f:
    mi_diccionario= json.load(f)
    print(mi_diccionario)
"""
#por alguna razon no funciona

diccionario_completo= {}


for key, value in inventario.items():
    diccionario_completo[key]=value

for key, value in inventario_2.items():
    diccionario_completo[key]=value

with open("inventario.json", "w") as f:
    json.dump(diccionario_completo, f, indent=4)

with open("inventario.json", "r") as f:
    mi_diccionario= json.load(f)
    print(mi_diccionario)
