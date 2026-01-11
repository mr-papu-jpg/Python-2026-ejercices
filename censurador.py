import re

texto= "Ang 302462395 , Anbll 567006729 , Papa 020630027"

texto_censurado= re.sub(r"\d{9}", "#CENSURADO#", texto)

print(texto_censurado)
