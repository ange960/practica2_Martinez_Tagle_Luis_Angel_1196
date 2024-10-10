
print("")#imprime el espacio en blanco 
print("Martinez Tagle Luis Angel 3w nom.1196 escribir una funcion sum()   ")#imprime el nombre del programador 
print("")#imprime espacio en blanco

def suma(lista):
    return sum(lista)  # Usa la función incorporada

def multip(lista):
    resultado = 1
    for num in lista:
        resultado *= num
    return resultado

def main():
    numeros = [1, 2, 3, 4]
    print("La suma es:", suma(numeros)) #imprime el mensaje
    print("La multiplicación es:", multip(numeros)) #imprime el mensaje 

if __name__ == "__main__":
    main()
