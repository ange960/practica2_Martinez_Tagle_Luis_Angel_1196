print("")#imprime espacio en blanco 
print("Martinez Tagle Luis Angel 3w no.1196 este programa despliega un saludo con tu nombre ")#imprime nombre del programador
print("")#imprime el espacio en blanco 
def saludar(nombre):
    """
    Función que muestra un saludo personalizado.

    Parámetros:
    nombre (str): El nombre de la persona a saludar.

    Devuelve:
    None: Imprime el saludo en la consola.
    """
    print(f"¡Hola {nombre}!") #imprime el mensaje 

def main():
    """
    Función principal que maneja la interacción con el usuario.

    Solicita al usuario que ingrese su nombre y llama a la
    función saludar() para mostrar el saludo personalizado.
    """
    # Solicitar al usuario que ingrese su nombre
    nombre = input("Por favor, ingresa tu nombre: ")
    
    # Llamar a la función saludar con el nombre ingresado
    saludar(nombre)

# Llamar a la función principal
if __name__ == "__main__":
    main()
