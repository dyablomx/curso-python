#reemplazar range(1, 11) por range(1, 101) para que vaya del 1 al 100
for fizzbuzz in range(1, 101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("FizzBuzz")
    elif fizzbuzz % 3 == 0:
        print("Fizz")
    elif fizzbuzz % 5 == 0:
        print("Buzz")
    else:
        print(fizzbuzz)