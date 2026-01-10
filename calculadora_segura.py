def calcualdora_segura():
    n1= int(input("Ingrese un numero: "))
    n2= int(input("Ingrese un numero: "))
    sig= input("ingrese la operacion: ")
    sum= lambda n1, n2: n1+n2
    res= lambda n1, n2: n1-n2
    mult= lambda n1, n2: n1*n2
    div= lambda n1, n2: n1/n2
    run_calculo= True

    while run_calculo:
        try:
            if sig == "+":
                print(sum(n1, n2))
                run_calculo= False
            elif sig == "-":
                print(res(n1, n2))
                run_calculo= False
            elif sig == "*":
                print(mult(n1, n2))
                run_calculo= False
            elif sig == "/":
                print(div(n1, n2))
                run_calculo= False
            else:
                raise NameError("SignoError")
        except Exception as err:
            if err == ValueError:
                print(f"Error en el valor: {err}")
            elif err == ZeroDivisionError:
                print(f"Error, 0 no es divisible: {err}")
            else:
                print(f"Creaste un nuevo error, es: {err}")
        finally:
            print(">>Cierre de operacion.")


n1= int(input("Ingrese un numero: "))
n2= int(input("Ingrese un numero: "))
sig= input("ingrese la operacion: ")

calcualdora_segura()

