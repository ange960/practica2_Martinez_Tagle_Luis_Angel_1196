print("")#imprime el espacio en blanco 
print("Martinez Tagle Luis Angel 3w nom.1196 este programa da el factorial de un numero entero")#imprime el nombre del programador 
print("")#imprime espacio en blanco 
def calcular_factorial(n):
    """
    Calcula el factorial de un número entero no negativo.

    :param n: Un entero no negativo.
    :return: El factorial de n.
    """
    if n == 0 or n == 1:
        return 1  # El factorial de 0 y 1 es 1
    else:
        factorial = 1  # Inicializa el factorial
        for i in range(2, n + 1):
            factorial *= i  # Multiplica el valor acumulado por el número actual
        return factorial  # Devuelve el resultado final

def main():
    """
    Función principal que solicita al usuario un número entero positivo
    y muestra su factorial.
    """
    while True:
        try:
            # Solicita al usuario un número entero
            numero = int(input("Introduce un entero positivo: "))
            if numero < 0:
                print("Por favor, introduce un número entero positivo.")#imprime el mensaje 
            else:
                break  # Sale del bucle si la entrada es válida
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número entero.")#imprime el mensaje 

    # Calcula el factorial del número ingresado
    resultado = calcular_factorial(numero)
    # Muestra el resultado en consola
    print(f"El factorial de {numero} es {resultado}.")

if __name__ == "__main__":
    # Ejecuta la función principal solo si el script se ejecuta directamente
    main()