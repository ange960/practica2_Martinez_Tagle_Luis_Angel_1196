print("")#imprime el espacio en blanco 
print("Martinez Tagle Luis Angel 3w nom.1196 funcion que de un string ")#imprime el nombre del programador 
print("")#imprime espacio en blanco

def longitud_ultima_palabra(frase):
    """
    Calcula la longitud de la última palabra en una frase.
    
    Parámetros:
    frase (str): La frase de la cual se desea obtener la longitud de la última palabra.

    Retorna:
    int: La longitud de la última palabra.
    """
    return len(frase.strip().split()[-1]) if frase.strip() else 0

def main():
    frase = input("Ingrese una frase: ")
    print(f"La longitud de la última palabra es: {longitud_ultima_palabra(frase)}") #imprime el mensaje 

if __name__ == "__main__":
    main()
