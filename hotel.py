
usuarios_db = {}

class Usuario:
    def __init__(self, nombre, email, contraseña):
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña

    @classmethod
    def crear_cuenta(cls, nombre, email, contraseña):
        if email in usuarios_db:
            print("Error: Ya existe una cuenta con este correo.")
        else:
            nuevo_usuario = cls(nombre, email, contraseña)
            usuarios_db[email] = nuevo_usuario
            print(f"Cuenta creada exitosamente para {nombre}.")

    @classmethod
    def iniciar_sesion(cls, email, contraseña):
        usuario = usuarios_db.get(email)
        if usuario and usuario.contraseña == contraseña:
            print(f"Inicio de sesión exitoso. Bienvenido {usuario.nombre}!")
            return True
        else:
            print("Error: Correo o contraseña incorrectos.")
            return False

    @classmethod
    def cambiar_contraseña(cls, email, contraseña_actual, nueva_contraseña):
        usuario = usuarios_db.get(email)
        if usuario and usuario.contraseña == contraseña_actual:
            usuario.contraseña = nueva_contraseña
            print("Contraseña cambiada exitosamente.")
        else:
            print("Error: La contraseña actual es incorrecta.")

class SistemaDeReservas:
    pass

class Reserva:
    pass

class Habitacion:
    pass

