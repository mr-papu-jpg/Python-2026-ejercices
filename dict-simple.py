users = {
    "Pepe": 24585,
    "Angstart": 1109,
    "Ronaldo": 222
}

busqueda=input(">>Elige un nobre se usuario a buscar: ")

if busqueda in users:
    print("Acceso concedido :3")
    print(users[busqueda])
else:
    print("Usuario no encontrado")
