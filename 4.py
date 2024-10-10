print("")#imprime el espacio en blanco 
print("Martinez Tagle Luis Angel 3w nom.1196 calcula el total de una factura ")#imprime el nombre del programador 
print("")#imprime espacio en blanco
def main():
    # Solicita la cantidad sin IVA y el porcentaje de IVA
    cantidad_sin_iva = float(input("Cantidad sin IVA: "))
    porcentaje_iva = float(input("Porcentaje de IVA: "))
    
    # Calcula el total de la factura
    total_factura = cantidad_sin_iva * (1 + porcentaje_iva / 100)
    
    # Muestra el total
    print(f"Total con IVA: {total_factura:.2f}")

if __name__ == "__main__":
    main()  # Ejecuta la función principal
