class VistaPrincipal:
    def menu_presentacion(self):
        print("\nBienvenido a SocialEvent S.A.")
        print("Somos expertos en la organización de Congresos y Eventos.")
        print("¡Haremos de tu evento una experiencia inolvidable!")
        
    def menu_opciones(self):
        print("\nA continuación le brindamos el menu de opciónes:")
        print("1. Ver lista de servicios disponibles")
        print("2. Seleccionar servicios")
        print("3. Modificar servicios")
        print("4. Seleccionar fecha del evento")
        print("5. Ver costo total")
        print("6. Reservar evento")
        print("7. Cancelar reserva")
        print("8. Verificar reserva")
        print("0. Salir")
        
        
    def saludo_final(self):
        print("\n¡Gracias por utilizar nuestro programa de SocialEvent S.A.!")
        print("Esperamos haber cumplido con tus expectativas.")
        print("¡Te deseamos un evento exitoso y lleno de alegría!")
        print("¡Hasta la próxima!\n")
        
        
    def ingreso_menu(self):
        return input("\nPor favor, selecciona una opción: ")  
        

    def error_ingreso(self):
        print("\n***Error de ingreso, vuelva a intentarlo***")
        
        
    def vista_atras(self):
        return input("\nPresione 1 para volver al menu principal: ")