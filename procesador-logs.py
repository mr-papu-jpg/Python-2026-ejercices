def filtrador(contenito):
    log_aux= list(map(lambda x: x.strip() , contenito))
    errs= list(filter(lambda linea: linea.startswith("ERROR"), log_aux))
    list_errores=list()
    for error in errs:
        list_errores.append(error)
    return list_errores

def procesar_log(nombre_archivo, funcion_filtro):
    with open(nombre_archivo, "r") as archivo:
        contenido= archivo.readlines()
        log=funcion_filtro(contenido)
        print(log)

procesar_log("servidor.txt", filtrador)
