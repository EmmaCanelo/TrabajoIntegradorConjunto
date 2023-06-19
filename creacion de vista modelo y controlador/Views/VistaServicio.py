class VistaServicio:
    def titulo_menu(self):
        print("\n¡A continuación le brindamos el listado completo de nuestros servicios!")
        print("\n")    
        
    def ingreso_menu(self):
        print("\n")
        return input("\nIngrese la opcion que más desee, (0 - Salir): ")
    
    def error_ingreso(self):
        print("\nError de ingreso, vuelva a intentarlo")
        
    def consulta_seguimineto(self):
        return input("\n¿Desea continuar elijiendo? Si - No: ")
        
    def error_valor_duplicado(self):
        print("\nUPS! Ya se encuentra almacenado dicho servicio")    
    
    def vista_atras(self):
        print("\n")
        return input("\nPresione 1 para volver al menu principal: ")
    
    def titulo_servicios_elegidos(self):
        print("\nLos servicios elegidos hasta el momento son:")
    
    def servicios_elegidos(self, nombre):
        formatName = ' '.join(word.capitalize() for word in nombre.strip().split())
        print("|"+formatName, end=' ')
        
    def seleccion_vacia(self):
        return input("\nNo se encuentran servicios seleccionados, presione una tecla para volver al menu de opciones: ")
        
    def seleccion_eliminar_servicios(self):
        return input("\nSeleccione el servicio que desee eliminar. Presione 0 para salir: ")
    
    def mostrar_costo(self, gastoServicios, gastoAdm, total):
        print("Detalle costo total: \n")
        print(f"Gasto total servicios:  {gastoServicios}")
        print(f"Gastos administrativos: {gastoAdm}")
        print(f"Iva:                    21%")
        print("                     -----------")
        print(f"Monto total:           ${total}")
        
    def error_documentacion(self):
        return input("\nDebe realizar al menos una seleccion de algún servicio para realizar la reserva (1 - continuar): ")
    
    def servisios_para_eliminar(self, index, nombre):
        print(f"\n{index}. {nombre}")