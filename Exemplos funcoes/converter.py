weight = float(input("Entre com a massa: "))
unit = str(input("Entre com a unidade em Kilogramas ou Libras (K ou L): "))
rep = weight

if unit == "K" or unit == "k": #Transformar Kg em Lb
    weight = weight * 2.205
    print(f"A massa indicada ({rep}Kgs), será de {weight:.1f}Lbs")
elif unit == "L" or unit == "l": #Transformar Lb em Kg
    weight = weight / 2.205
    print(f"A massa indicada ({rep}Lbs), será de {weight:.1f}Kgs")
else:
    print(f"{unit} não é válido!")