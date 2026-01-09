def configurar_personaje(nivel):
    if nivel < 1 or nivel > 100:
        raise ValueError("Nivel fuera de rango")
    try:
        print(f"nivel: {nivel}")
    except ValueError as err:
        print(f"Error: {err}")


configurar_personaje(123)
configurar_personaje(35)
