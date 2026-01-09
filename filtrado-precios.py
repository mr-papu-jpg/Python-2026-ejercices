precios=[100, 250, 80, 1500, 400, 20, 130]

#solo incluir los precios menores a 200
ofertas= [n for n in precios if n < 200]

#incluir un 10% de descuento adicional
descuento=[n - ((n * 10)/100) for n in ofertas]

print(f"Precios: {precios}")
print(f"Ofertas: {ofertas}")
print(f"Descuentos: {descuento}")
