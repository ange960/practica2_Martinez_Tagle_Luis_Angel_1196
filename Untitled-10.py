print("")#imprime el espacio en blanco 
print("Martinez Tagle Luis Angel 3w nom.1196 escribe  una función que tome un carácter y devuelva True si es una vocal")#imprime el nombre del programador 
print("")#imprime espacio en blanco

def es_vocal(caracter):
    """
    Verifica si un carácter es una vocal.

    Parámetros:
    caracter (str): El carácter a verificar.

    Retorna:
    bool: True si el carácter es una vocal, False en caso contrario.
    """
    return caracter.lower() in 'aeiouáéíóú'

def main():
    char = input("Ingrese un carácter: ")
    print(es_vocal(char))

if __name__ == "__main__":
    main()
