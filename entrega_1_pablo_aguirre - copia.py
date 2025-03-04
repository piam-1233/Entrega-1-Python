usuarios = {}

def registrar_usuario():
    """Función para registrar un nuevo usuario."""
    while True:
        usuario = input("Ingrese un nombre de usuario: ")
        if usuario in usuarios:
            print("Este usuario ya existe. Intente con otro nombre.")
        else:
            contraseña = input("Ingrese una contraseña: ")
            usuarios[usuario] = contraseña
            print("Usuario registrado exitosamente.")
            break

def mostrar_usuarios():
    """Función para mostrar los usuarios registrados."""
    if usuarios:
        print("Usuarios registrados:")
        for usuario in usuarios:
            print(f"- {usuario}")
    else:
        print("No hay usuarios registrados aún.")

def login():
    """Función para iniciar sesión."""
    usuario = input("Ingrese su nombre de usuario: ")
    if usuario in usuarios:
        contraseña = input("Ingrese su contraseña: ")
        if usuarios[usuario] == contraseña:
            print("Inicio de sesión exitoso. ¡Bienvenido!")
        else:
            print("Contraseña incorrecta. Intente nuevamente.")
    else:
        print("El usuario no existe. Regístrese primero.")

def menu():
    """Función principal para manejar el programa."""
    while True:
        print("\nMenú:")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Mostrar usuarios registrados")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            login()
        elif opcion == "3":
            mostrar_usuarios()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
menu()
