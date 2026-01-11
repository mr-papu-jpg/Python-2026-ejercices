import re

def es_valida(matricula):
    verificar=re.match(r"^\d{4}[A-Z]{3}$", matricula)
    
    if verificar:
        print(f"{matricula}: Es valida")
    else:
        print(f"{matricula}: No es valida")

es_valida("1234ABC")
