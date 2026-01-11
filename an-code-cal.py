import re

operacion= "150+30-50*2/10"

operacion_formateada= re.split(r"[+\-*/]", operacion)

print(operacion_formateada)
