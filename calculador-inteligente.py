def dividir_elementos(elm1, elm2):
    try:
        return elm1 / elm2
    except ZeroDivisionError:
        print("No se puede calcular entre 0")
    finally:
        print("calculo finalizado")

print(dividir_elementos(4, 0))
print(dividir_elementos(4, 2))
