print("")#imprime el espacio en blanco 
print("Martinez Tagle Luis Angel 3w nom.1196 definir una funcion que tome tres numeros  ")#imprime el nombre del programador 
print("")#imprime espacio en blanco

def mayor_de_tres(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    n1, n2, n3 = map(float, input("Ingrese tres números separados por espacios: ").split())
    print(f"El mayor de los tres números es: {mayor_de_tres(n1, n2, n3)}") #imprime el masaje 

if __name__ == "__main__":
    main()
