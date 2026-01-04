ficha_pokemon={
    "nombre": "Pikachu",
    "tipo": "Electrico",
    "nivel": 1
}

print(type(ficha_pokemon))
print("\n_-----------------_")
print(f"Nivel del pokemon: {ficha_pokemon["nivel"]}")

ficha_pokemon["nivel"]= 2
ficha_pokemon["hp"]= 100

print("\n_-----------------_")

print(ficha_pokemon)
