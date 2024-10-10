print("")#imprime el espacio en blanco 
print("Martinez Tagle Luis Angel 3w nom.1196 calcula el area de un circulo y volumen ")#imprime el nombre del programador 
print("")#imprime espacio en blanco
import math

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_volumen_cilindro(radio, altura):
    area_base = calcular_area_circulo(radio)
    return area_base * altura

def main():
    # Solicitar al usuario los valores
    radio = float(input("Ingrese el radio del círculo: "))
    altura = float(input("Ingrese la altura del cilindro: "))
    
    # Calcular área y volumen
    area = calcular_area_circulo(radio)
    volumen = calcular_volumen_cilindro(radio, altura)
    
    # Mostrar resultados
    print(f"El área del círculo es: {area:.2f} unidades cuadradas") #imprime el mensaje 
    print(f"El volumen del cilindro es: {volumen:.2f} unidades cúbicas") #imprime el mensaje 

if __name__ == "__main__":
    main()
