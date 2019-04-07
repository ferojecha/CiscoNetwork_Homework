
#  Aunque no hace falta definir estas funciones porque python ya las trae incorporadas, lo hacemos por "practicar"
def suma(a,b):
	return(a+b)
def rest(a,b):
	return(a-b)
def mult(a,b):
	return(a*b)
def div(a,b):
	return(a/b)
def exp(a,b):
	return(a**b)

# Definimos la funcion que realizará todo el trabajo para poder llamarla posteriormente si queremos volver a realizar otra operación
def inp():
	# ============================================================================================================================================|
	# Esta cabecera sirve para que el programa no avance si los valores introducidos no son válidos
	try:
		global a 
		a = float(input("Introduce un número (a): "))
		global b
		b = float(input("Introduce otro número (b): "))
		global operacion
		operacion = int(input("¿Qué operación deseas realizar:\n(1) Suma \n(2) Resta \n(3) Multiplicación \n(4) División \n(5) Exponencial\n"))
	except:
		print("Valor/es inválido/s\n")
		inp()
	# ============================================================================================================================================|
	if operacion == 1:
		print("El resultado a + b es: ", suma(a,b), "\n")
	elif operacion == 2:
		print("El resultado a - b es: ", rest(a,b), "\n")
	elif operacion == 3:
		print("El resultado a x b es: ", mult(a,b), "\n")
	elif operacion == 4:
		print("El resultado a / b es: ", div(a,b), "\n")
	elif operacion == 5:
		print("El resultado a ^ b es: ", exp(a,b), "\n")                                                                                          
# ================================================================================================================================================|
inp() # Llamamos a la funcion propiamente, si no no se invocaría por el mero hecho de haberla definido                                            |
# ================================================================================================================================================|
# Dejamos abierta la posibilidad de realizar otro cálculo, siempre que el usuario lo solicite
r = input("Deseas realizar otra operacion? y/n:\n")
while r == "y":
	inp()
	r = input("Deseas realizar otra operacion? y/n:\n")
print("Nos vemos!")
# exit()




