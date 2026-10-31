def is_armstrong_number(number):
    suma = 0
    longitud = len(str(number))
    aux = number
    for i in range(len(str(aux))):
        digito = aux % 10
        suma += digito ** longitud
        aux //= 10
        
    if number == suma:
        return True
    else:
        return False

print(is_armstrong_number(153))