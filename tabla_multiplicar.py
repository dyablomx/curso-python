#numero=int(input("Ingrese un número para generar su tabla de multiplicar: "))
for numero in range(1, 11):    
    for multiplicador in range(1, 11):
    
        resultado = numero * multiplicador
        
        print(f"{numero} x {multiplicador} = {resultado}")