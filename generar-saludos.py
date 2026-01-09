def generar_saludo(saludo):
    return lambda nombre : f"{saludo} {nombre}"

saludo_formal= generar_saludo("Bienvenido")
print(saludo_formal("Juan"))

