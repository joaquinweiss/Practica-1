from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators1 = ["+","-","*","/"]
operators2 = ["+","-","*"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
j=0
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
       # Se eligen números y operador al azar
	number_1 = randrange(10)
	number_2 = randrange(10)
	if(number_2 == 0):
		operator = choice(operators2)
	else:
		operator = choice(operators1)
	# Se imprime la cuenta.
	print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
	# Le pedimos al usuario el resultado
	result = float(input("resultado: "))
	if(operator== "+"):
		sol = number_1 + number_2
	elif(operator== "-"):
		sol = number_1 - number_2
	elif(operator== "/"):
		sol = number_1 / number_2
	else:
		sol = number_1 * number_2
	if(sol == result):
		print("Correcto")
		j=j+1
	else:
		print("Incorrecto")
	
	
# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")
print(f"\n Acertaste {j} resultados.")













