print("")#imprime el espacio en blanco 
print("Martinez Tagle Luis Angel 3w nom.1196 capturar la direccion email ")#imprime el nombre del programador 
print("")#imprime espacio en blanco

def es_email_valido(email):
    return '@' in email

def main():
    email = input("Ingrese su dirección de correo electrónico: ")
    mensaje = "válida" if es_email_valido(email) else "no válida"
    print(f"La dirección de correo electrónico es {mensaje}.")

if __name__ == "__main__":
    main()
