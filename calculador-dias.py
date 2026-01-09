from datetime import datetime, date, timedelta

print("### Introdusca fecha de nacimiento ###")
print("------------")
dia=int(input(">>Dia: "))
mes=int(input(">>Mes: "))
anio=int(input(">>Anio: "))
print("------------")

hoy_aux= datetime.now()
hoy= date(hoy_aux.year, hoy_aux.month, hoy_aux.day)
nacimiento= date(anio, mes, dia) 
dias_prueba= timedelta(days=10000)

dias_vividos= hoy - nacimiento
fecha_pred= hoy_aux + dias_prueba

print(f"\n>>El dia de hoy: {hoy.strftime("%d/%m/%Y")}\n")
print(f"Dias vividos: {dias_vividos}")
print(f"Segundos vividos: {dias_vividos.total_seconds()}")
print(f"Fecha que llegaras cuando hayas vovido 10,000 dias: \n{fecha_pred.strftime("%d/%m/%Y")}")
