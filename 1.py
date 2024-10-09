print("")
print("Martinez Tagle Luis Angel 3w 1196 este programa te saluda cada vez que se lo pidas ")
def saludar():
    """Función que muestra el saludo 'Hey amigos!'."""
    print("Hey amigos!")

def main():
    while True:
        try:
            # Solicitar al usuario cuántas veces quiere el saludo
            veces = int(input("¿Cuántas veces quieres recibir el saludo? (ingresa un número entero positivo): "))
            
            # Validar que el número sea positivo
            if veces <= 0:
                print("Por favor, ingresa un número entero positivo.")
                continue
            
            # Mostrar el saludo la cantidad de veces solicitada
            for _ in range(veces):
                saludar()
            
            # Salir del bucle después de saludar
            break
            
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

# Llamar a la función principal
if __name__ == "__main__":
    main()
