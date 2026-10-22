alumnos = ["Ana", "Carlos", "Luis", "María"]

print(alumnos)
print(alumnos[0])
print(alumnos[1])

alumnos[1] = "Pedro"
print(alumnos)

#append agrega un elemento al final de la lista
alumnos.append("Sofia")
print(alumnos)

#remove elimina un elemento de la lista
alumnos.remove("Luis")
print(alumnos)

#len devuelve la cantidad de elementos en la lista
print(f"Total de alumnos: {len(alumnos)}")