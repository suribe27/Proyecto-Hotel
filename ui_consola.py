
from hotel import Usuario

class UIConsola:
    def mostrar_menu(self):
        while True:
            print("\n--- Menú ---")
            print("1. Crear cuenta")
            print("2. Iniciar sesión")
            print("3. Cambiar contraseña")
            print("4. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                self.crear_cuenta()
            elif opcion == '2':
                self.iniciar_sesion()
            elif opcion == '3':
                self.cambiar_contraseña()
            elif opcion == '4':
                print("Saliendo del sistema.")
                break
            else:
                print("Opción no válida, por favor selecciona nuevamente.")

    def crear_cuenta(self):
        nombre = input("Ingresa tu nombre: ")
        email = input("Ingresa tu correo: ")
        contraseña = input("Ingresa tu contraseña: ")
        Usuario.crear_cuenta(nombre, email, contraseña)

    def iniciar_sesion(self):
        email = input("Ingresa tu correo: ")
        contraseña = input("Ingresa tu contraseña: ")
        Usuario.iniciar_sesion(email, contraseña)

    def cambiar_contraseña(self):
        email = input("Ingresa tu correo: ")
        contraseña_actual = input("Ingresa tu contraseña actual: ")
        nueva_contraseña = input("Ingresa tu nueva contraseña: ")
        Usuario.cambiar_contraseña(email, contraseña_actual, nueva_contraseña)

    def ejecutar_app(self):
        self.mostrar_menu()
