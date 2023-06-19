class VistaEvento:
    def ingreso_fecha(self):
        return input("\nIngrese el día (en número) en que le gustaria realizar el evento en el mes de Julio: ")
    
    def error_ingreso(self):
        return input("\nError de ingreso, presione una tecla para volver a intentarlo: ")
        
    def evento_ocupado(self):
        print("\nLa fecha ya se encuentra reservada")
        
    def fecha_libre_proxima(self, dia):
        return input(f"\nLa fecha próxima que le podemos brindar es el {dia}, ¿desea reservarla? Si - No (1 - Salir): ")
    
    def ultima_fecha_libre(self, dia):
        return input(f"\nLa última fecha que le podemos brindar es el {dia}, ¿desea reservarla? Si - No (1 - Salir): ")
    
    def evento_guardado(self):
        return input("\nSe guardó con exito su día. presione 1 para volver al menu principal: ")
    
    def senia_evento(self, monto, total):
        print(f"\nPara finalizar la reserva, debe abonar una seña de ${monto}, en concepto del 30% del total ${total}")
        return input("\nIngrese el monto solicitado (1 - Salir): ")
    
    def error_senia(self):
        print("\nError en el ingreso del monto de la seña, vuelva a intentarlo")
        
    def error_documentacion(self):
        return input("\nDebe seleccionar una fecha para realizar la reserva (1 - continuar): ")
    
    def reserva_exito(self):
        return input("\nSe realizó con éxito la reserva, presione una tecla para volver al menu de opciones: ")
    
    def fecha_evento(self, fecha):
        print(f"\nLa fecha del evento que se cancelara es {fecha}")
        
    def cancelacion_evento(self):
        return input("\n¿Desea cancelar el evento? Si - No: ")
    
    def confirmacion_cancelacion(self):
        return input("\nSe cancelo su evento, quedamos a disposición. Presione una tecla para continuar, muchas gracias. ")

    def error_buscar_dni(self):
        return input("\nNo se logro encontrar el dni ingresado, presione 1 para volver a intentar o cualquier tecla para salir: ") 
    
    def fecha_reservada(self, fecha):
        return input(f"\nUsted ya reservo la fecha {fecha}, presione 1 para modificarla o cualquier tecla para continuar: ")
    
    def devolucion_reserva(self, monto, total):
        return input(f"\nSe le devolvera ${monto}, correspondiente al 20% del total de la seña abonada ${total}, presione una tecla para continuar: ")
    
    def cancelacion_fuera_fecha(self, fecha):
        print(f"\nLa fecha del evento es el {fecha}. como faltan menos de 15 dias para el mismo, no se le devolvera el 30% de la seña.")
        
    