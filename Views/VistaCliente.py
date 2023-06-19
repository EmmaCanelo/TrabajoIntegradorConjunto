class VistaCliente:
    def ingreso_menu(self):
        return input("\nPor favor, selecciona una opción: ")  

    def error_ingreso(self):        
        print("\n***Error de ingreso, vuelva a intentarlo***")
        
    def vista_atras(self):
        return input("\nPresione 1 para volver al menu principal: ")
    
    def carga_nombre(self):
        return input("\nIngrese su nombre (1- Salir): ")
    
    def carga_apellido(self):
        return input("\nIngrese su apellido (1- Salir): ")
    
    def carga_dni(self):
        return input("\nIngrese su dni (1- Salir): ")
    
    def carga_telefono(self):
        return input("\nIngrese su telefono (1- Salir): ")
    
    def carga_direccion(self):
        return input("\nIngrese su direccion (1- Salir): ")
    
    def error_documentacion(self):
        return input("\nDebe completar todos los campos relacionados a sus datos personales para realizar la reserva (1 - continuar): ")
    
    def error_sin_evento(self):
        return input("\nNo se registran eventos con dicho DNI (1- Volver a intentar, 0 - Salir): ")
    
    def dni_usado(self):
        return input("\nYa se encuantra un evento registrado con este usuario, por el momento solo tomamos pedidos de diferentes personas, presione una tecla para continuar: ")
    
    def evento_reservado(self, fecha):
        print(f"\nLa fecha de su evento esta programada para el {fecha} con los siguientes servicios:")
        
    