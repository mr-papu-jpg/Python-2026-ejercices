niveles=[5, 12, 18, 25, 30]
x=0

while x < len(niveles):
    if niveles[x] < 18:
        print(f"pokemon de nivel {x} Aun no puede evolucionar")
    else:
        print(f"pokemon de nivel {x} esta listo para evolucionar")
    x+=1

