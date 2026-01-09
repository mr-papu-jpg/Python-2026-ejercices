from clima_utils import celsius_a_farentheits as c_f 
from clima_utils import farentheits_a_celsius as f_c 

temp_c= int(input("Ingrese temperatura em celsius: "))
temp_f= int(input("Ingrese temperatura en farentheits: "))

c= c_f(temp_c)
f= f_c(temp_f)
print("----------")
print(c)
print(f)
print("----------")
