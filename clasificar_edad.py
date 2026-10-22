edad = int(input("¿Cuántos años tienes? "))

if edad < 0:
    print("La edad no puede ser negativa.")
elif edad == 0:
    print("Eres un recién nacido.")
elif edad < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")
