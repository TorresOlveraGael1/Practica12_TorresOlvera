# Almacenar en una lista los siguientes precios, 43, 57, 92, 20, 37, 5, 9, y mostrar en pantalla  el menor y el mayor de los precios.

print (" ")
print ("Torres Olvera Gael")
print (" ")

#Valores establecidos para la lista
a = int(input("Ingresa el valor que quieras: "))

b = int(input("Ingresa el valor que quieras: "))

c = int(input("Ingresa el valor que quieras: "))

d = int(input("Ingresa el valor que quieras: "))

e = int(input("Ingresa el valor que quieras: "))

f = int(input("Ingresa el valor que quieras: "))

g = int(input("Ingresa el valor que quieras: "))

Precios = [a, b, c, d, e, f, g] #Juntando los valores solicitados en una linea

# Ordenar la lista de mayor a menor
Precios.sort(reverse=True)

# Imprimir la lista ordenada
print("Lista ordenada de mayor a menor:")
print(Precios)