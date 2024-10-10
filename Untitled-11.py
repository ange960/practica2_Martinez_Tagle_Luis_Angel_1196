print("")#imprime el espacio en blanco 
print("Martinez Tagle Luis Angel 3w nom.1196 Que saque la distancia dirigida entre dos puntos ")#imprime el nombre del programador 
print("")#imprime espacio en blanco


def distancia_dirigida(punto1, punto2):
    return ((punto2[0] - punto1[0])**2 + (punto2[1] - punto1[1])**2)**0.5

def main():
    x1, y1 = map(float, input("Ingrese las coordenadas del primer punto (x1, y1): ").split())
    x2, y2 = map(float, input("Ingrese las coordenadas del segundo punto (x2, y2): ").split())
    distancia = distancia_dirigida((x1, y1), (x2, y2))
    print(f"La distancia dirigida es: {distancia:.2f}")

if __name__ == "__main__":
    main()
