import re

def shear_IPs(name_directory):
    with open(name_directory, "r") as f:
        contenido= f.read()
        shear_cont= re.findall(r"\d{1, 3}\.\d{1, 3}\.\d{1, 3}\.\d{1, 3}\.", contenido)
        print(f"Lista completa: {shear_cont}")

shear_IPs("conexciones.log")

#creo que sirve pero no devuelve la lista.
