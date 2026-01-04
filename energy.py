energias =[10, 50, 35, 75, 55, 100, 200]

print(energias)
print()

energias_max = list()

for x in energias:
    if x >= 50:
        energias_max.append(x)
        print(f"{x} fue aceptado para energias_max.\n")
    else:
        print(f"{x} fue denegado para energias_max.\n")

energias_ord = energias_max

for x in range(len(energias_ord)):
    for y in range(len(energias_ord)):
        if energias_ord[y] > energias_ord[y - 1]:
            aux= energias_ord[y]
            energias_ord[y]= energias_ord[y-1]
            energias_ord[y-1]=aux

print(energias_ord)
