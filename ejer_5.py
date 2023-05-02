#Ejercicio_5

def romano_a_decimal(num_romano):
    valores={'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    decimal=0

    for i in(len(num_romano)):
       if i > 0 and valores[num_romano[i]] > valores[num_romano[i-1]]:
        decimal+=valores[num_romano[i]]-2*[num_romano[i-1]]
       else:
        decimal+=valores[num_romano[i]]
    return ("El valor decimal del número romano es:"), decimal
