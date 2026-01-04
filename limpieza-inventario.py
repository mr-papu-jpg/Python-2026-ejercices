objetos = ["pocion", "antidoto", "pocion", "pokeball", "antidoto", "bayas"]

print(f"Lista de objetos antes del set: {objetos}")
print("----------------")

objetos_set= set()

for x in objetos:
    objetos_set.add(x)


print(f"Lista de objetos despues del set: {objetos_set}")
