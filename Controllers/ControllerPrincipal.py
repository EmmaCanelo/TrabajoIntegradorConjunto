import os
import sys
from datetime import date, datetime, timedelta
from Views.VistaPrincipal import VistaPrincipal
from Views.VistaCliente import VistaCliente
from Views.VistaServicio import VistaServicio
from Views.VistaEvento import VistaEvento
from Models.Servicio import Servicio
from Models.Evento import Evento
from Models.Cliente import Cliente

class ControllerPrincipal:
    def __init__(self):
        self.servicio = Servicio(nombre='', costo='')
        self.evento = Evento(fecha="", cliente="", servicio="", senia="", costo="", estado="")
        self.cliente = Cliente(nombre="", apellido="", dni="", direccion="", telefono="")
        self.vistaCliente = VistaCliente()
        self.vistaPrincipal = VistaPrincipal()
        self.vistaServicio = VistaServicio()
        self.vistaEvento = VistaEvento()
        self.listaServicio = []
        self.listaEvento = []
        self.listaServiciosTemporales = []
        self.ingresoFecha=0
        self.ingresoSenia = 0
        
        
    def reset_variables(self):
        self.servicio = Servicio(nombre='', costo='')
        self.evento = Evento(fecha="", cliente="", servicio="", senia="", costo="", estado="")
        self.cliente = Cliente(nombre="", apellido="", dni="", direccion="", telefono="")
        self.vistaCliente = VistaCliente()
        self.vistaPrincipal = VistaPrincipal()
        self.vistaServicio = VistaServicio()
        self.vistaEvento = VistaEvento()
        self.listaServicio = []
        self.listaEvento = []
        self.listaServiciosTemporales = []
        self.ingresoFecha=0
        self.ingresoSenia = 0
    
        
    def menu_principal(self):
        self.limpiar_consola()
        self.iniciar_servicio()
        self.iniciar_evento()
        self.vistaPrincipal.menu_presentacion()
        self.vistaPrincipal.menu_opciones()
        ingreso = 1
        while ingreso >= 1 and ingreso <= 6:
            ingreso = self.vistaPrincipal.ingreso_menu()
            if ingreso == '0':
                ingreso = 0
                self.limpiar_consola()
                self.vistaPrincipal.saludo_final()
                sys.exit()
            elif ingreso == '1':
                ingreso = 1
                self.mostrar_servicios()
                self.menu_principal()
            elif ingreso == '2':
                ingreso = 2
                self.limpiar_consola()
                self.listaServicio = self.servicios_para_elegir()
                self.menu_principal()
            elif ingreso == '3':
                ingreso = 3
                self.limpiar_consola()
                self.modificar_servicios_seleccionados()   
            elif ingreso == '4':
                ingreso = 4
                self.limpiar_consola()
                self.consultar_disponibilidad()
                self.menu_principal()
            elif ingreso == '5':
                ingreso = 5
                self.limpiar_consola()
                costo = self.calcular_costo()
                self.mostrar_costo(costo,self.evento.get_costo())
                self.menu_principal()            
            elif ingreso == '6':
                ingreso = 6
                self.limpiar_consola()
                self.carga_nombre()
                self.carga_apellido()
                self.carga_dni()
                self.carga_direccion()
                self.carga_telefono()
                self.carga_senia()
                self.menu_principal()      
            elif ingreso == '7':
                ingreso = 7      
                self.limpiar_consola()
                self.cancelar_evento()
                self.menu_principal() 
            elif ingreso == '8':
                ingreso = 8      
                self.limpiar_consola()
                self.verificar_reserva()
                #self.menu_principal() 
            else:
                self.vistaPrincipal.error_ingreso()
                ingreso = 1
            
            
    def iniciar_servicio(self):
        try:
            self.listaServicio = []
            with open("servicios.txt", 'r') as file:
                file.seek(0)
                archivo = file.readlines()
                for line in archivo:
                    item = line.strip().split(';')
                    self.servicio = Servicio(item[0], item[1])
                    self.listaServicio.append(self.servicio) 
            return self.servicio                    
        except Exception as e:
            print(f"A ocurrido el siguiente error: {e}")
        
        
    def iniciar_evento(self):
        try:
            with open("eventos.txt", 'r') as file:
                file.seek(0)
                archivo = file.readlines()
                for line in archivo:
                    item = line.strip().split(';')
                    self.evento = Evento(item[0], item[1], item[2], item[3], item[4], item[5])
                    self.listaEvento.append(self.evento) 
        except Exception as e:
            print(f"A ocurrido el siguiente error: {e}")    
        
        
    
    def total_lineas_archivo(self):
        try:
            with open("servicios.txt", 'r') as file:
                lineas = file.readlines()
                return len(lineas)
        except Exception as e:
            print(f"A ocurrido el siguiente error: {e}")
        
        
        
    def servicios_elegidos(self, estado):
        try:
            with open("servicios.txt", 'r') as file:
                archivo = file.readlines()
                cont = 0
                for index, line in enumerate(archivo):
                    linea = line.strip().split(';')
                    for index2, servicio in enumerate(self.listaServiciosTemporales):
                        if int(servicio) == (index+1):
                            if estado == 1:
                                self.vistaServicio.servicios_elegidos(linea[0])
                            else:
                                cont += 1
                                self.vistaServicio.servicios_para_eliminar(cont, linea[0])
                            break
        except Exception as e:
            print(f"A ocurrido el siguiente error: {e}")
        
        
    def servicios_para_elegir(self):
        self.vistaServicio.titulo_menu()
        for index, servicio in enumerate(self.listaServicio):
            print(servicio.__str__(index+1))
        ingreso = 1
        total = self.total_lineas_archivo()
        if len(self.listaServiciosTemporales) > 0:
            self.vistaServicio.titulo_servicios_elegidos()
            self.servicios_elegidos(1)      
        while ingreso >= 1 and ingreso <= total:
            ingreso = self.vistaServicio.ingreso_menu()
            if ingreso.isdigit():
                if ingreso != '0':
                    ingreso = int(ingreso)
                    if ingreso >= 1 and ingreso <= total:
                        if ingreso not in self.listaServiciosTemporales :
                            self.listaServiciosTemporales.append(ingreso)                            
                        else:
                            self.vistaServicio.error_valor_duplicado()            
                        ingresoSeguimiento = 'x'
                        while ingresoSeguimiento != 'no' and ingresoSeguimiento != 'si':
                            ingresoSeguimiento = self.vistaServicio.consulta_seguimiento()                        
                            if ingresoSeguimiento.lower() == 'si':
                                ingreso = 1
                                self.limpiar_consola()
                                self.servicios_para_elegir()
                            elif ingresoSeguimiento.lower() == 'no':                             
                                self.menu_principal()
                            else:
                                self.vistaServicio.error_ingreso()
                                ingresoSeguimiento = 'x'
                                ingreso = 1
                    else:
                        self.vistaServicio.error_ingreso()
                        ingreso = 1
                else:
                    self.menu_principal()
            else:
                self.vistaServicio.error_ingreso()
                ingreso = 1
                    
    
    def limpiar_consola(self):
        os.system('cls') 
        #os.system('clear')
        
                 
    def mostrar_servicios(self):
        self.limpiar_consola()
        self.vistaServicio.titulo_menu()
        for index, servicio in enumerate(self.listaServicio):
            print(servicio.__str__(index+1))
        ingreso = 0
        while ingreso != 1: 
            ingreso = self.vistaServicio.vista_atras()
            if ingreso.isdigit():
                ingreso = int(ingreso)
                if ingreso == 1:
                    return 
                else:
                    self.vistaServicio.error_ingreso()
                    ingreso = 0
            else:
                self.vistaServicio.error_ingreso()
                ingreso = 0
                
                
                
    def modificar_servicios_seleccionados(self):
        self.limpiar_consola()
        if self.listaServiciosTemporales == []:
            self.vistaServicio.seleccion_vacia()
            self.menu_principal()
        else:
            self.vistaServicio.titulo_servicios_elegidos()
            self.servicios_elegidos(2)                                
            estado = True
            while estado:
                ingreso = self.vistaServicio.seleccion_eliminar_servicios()
                if ingreso.isdigit():
                    if ingreso == '0':
                        self.menu_principal()    
                    else:
                        if int(ingreso) > 0 and int(ingreso) <= len(self.listaServiciosTemporales):                                
                            for index, servicio in enumerate(self.listaServiciosTemporales):
                                if int(ingreso) == (index+1):
                                    self.listaServiciosTemporales.pop(index)
                                    break
                            self.modificar_servicios_seleccionados()
                        else:
                            self.vistaServicio.error_ingreso()                            
                else:
                    self.vistaServicio.error_ingreso()
            
                          
                
    def calcular_costo(self):        
        costo = 0
        for index, item in enumerate(self.listaServicio):
            for index2, servicio in enumerate(self.listaServiciosTemporales):
                if (index+1) == int(servicio):
                    costo += int(item.get_costo())
                    break                    
        total = (costo + 10000) * 1.21
        self.evento.set_costo(total)
        return costo
        
        
        
    def mostrar_costo(self, costo, total):
        self.vistaServicio.mostrar_costo(costo, '10000', total)
        ingreso = 0
        while ingreso == 0:
            ingreso = self.vistaServicio.vista_atras()
            if ingreso.isdigit():
                ingreso = int(ingreso)
                if ingreso == 1:
                    return 
                else:
                    self.vistaServicio.error_ingreso()
                    ingreso = 0
            else:
                self.vistaServicio.error_ingreso()
                ingreso = 0
                
                
                
    def consultar_disponibilidad(self):
        if self.ingresoFecha == 0:            
            ingreso = 1
            while str(ingreso).isdigit():
                ingreso = self.vistaEvento.ingreso_fecha()
                if ingreso.isdigit():
                    if  int(ingreso) >= 1 and int(ingreso) <= 31:
                        for index, evento in enumerate(self.listaEvento):
                            if (index+1) == int(ingreso):
                                estado = evento.get_estado()
                                if estado == '1':
                                    self.vistaEvento.evento_ocupado()
                                    for indexLibre, eventoLibre in enumerate(self.listaEvento):
                                        if indexLibre > index :
                                            estadoLibre = eventoLibre.get_estado()
                                            if estadoLibre == '0':
                                                ingresoLibre = 'x'
                                                while ingresoLibre != 'si' and ingresoLibre != 'no':
                                                    if (indexLibre+1) < len(self.listaEvento):
                                                        ingresoLibre = self.vistaEvento.fecha_libre_proxima(eventoLibre.get_fecha())
                                                        if ingresoLibre.lower() == 'si':
                                                            fecha = indexLibre+1
                                                            self.ingresoFecha = fecha
                                                            self.menu_principal()
                                                        elif ingresoLibre.lower() == 'no':
                                                            break
                                                        elif ingresoLibre == '1':
                                                            self.menu_principal()
                                                        else:
                                                            self.vistaEvento.error_ingreso()
                                                            ingresoLibre = 'x'
                                                    else:
                                                        ingresoLibre = self.vistaEvento.ultima_fecha_libre(eventoLibre.get_fecha())
                                                        if ingresoLibre.lower() == 'si':
                                                            fecha = indexLibre+1
                                                            self.ingresoFecha = fecha                                                            
                                                            self.menu_principal()
                                                        elif ingresoLibre.lower() == 'no':
                                                            self.menu_principal()
                                                        elif ingresoLibre == '1':
                                                            self.menu_principal()
                                                        else:
                                                            self.vistaEvento.error_ingreso()
                                                            ingresoLibre = 'x'
                                else:
                                    fecha = index+1
                                    self.ingresoFecha = fecha                                                        
                                    ingresoReserva = 'x'
                                    while ingresoReserva != '1':
                                        ingresoReserva = self.vistaEvento.evento_guardado()
                                        if ingresoReserva == '1':
                                            self.menu_principal()
                                        else:
                                            ingreso = 'x'
                                            self.vistaEvento.error_ingreso()   
                    else:                        
                        self.vistaEvento.error_ingreso()
                        self.limpiar_consola()   
                        self.consultar_disponibilidad()
                else:
                    self.vistaEvento.error_ingreso()    
                    self.limpiar_consola()   
                    self.consultar_disponibilidad()
        else:
            fecha = str(self.ingresoFecha)+"/07/2023"
            ingreso = self.vistaEvento.fecha_reservada(fecha)
            if ingreso == '1':
                self.ingresoFecha = 0
                self.limpiar_consola()
                self.consultar_disponibilidad()
            else:
                return
                
                
                
    def carga_nombre(self):
        ingreso = 1
        while ingreso == 1:
            nombre = self.vistaCliente.carga_nombre()
            if nombre.isspace() or len(nombre) == 0:
                self.vistaCliente.error_ingreso()
            elif nombre != '1': 
                self.cliente.set_nombre(nombre)
                ingreso = 0
            else:
                self.menu_principal()
                
    
    
    def carga_apellido(self):
        ingreso = 1
        while ingreso == 1:
            apellido = self.vistaCliente.carga_apellido()
            if apellido.isspace() or apellido.isdigit() or len(apellido) == 0:
                self.vistaCliente.error_ingreso()
            elif apellido != '1': 
                self.cliente.set_apellido(apellido)
                ingreso = 0
            else:
                self.menu_principal()
                
                
                
    def carga_dni(self):
        ingreso = 1
        while ingreso == 1:
            dni = self.vistaCliente.carga_dni()
            if dni.isspace() or len(dni) == 0:
                self.vistaCliente.error_ingreso()
            elif dni != '1': 
                estado = self.verifica_dni(dni)
                if estado:    
                    self.vistaCliente.dni_usado()
                    self.menu_principal()
                else:
                    self.cliente.set_dni(dni)
                    ingreso = 0
            else:
                self.menu_principal()   
          
                
                 
    def verifica_dni(self, dni):
        estado = False
        for evento in self.listaEvento:            
            if evento.get_cliente() == dni:
                estado = True
        return estado
                 
    
    
    def carga_telefono(self):
        ingreso = 1
        while ingreso == 1:
            telefono = self.vistaCliente.carga_telefono()
            if telefono.isspace() or len(telefono) == 0:
                self.vistaCliente.error_ingreso()
            elif telefono != '1': 
                self.cliente.set_telefono(telefono)
                ingreso = 0
            else:
                self.menu_principal()  
                
                
                
    def carga_direccion(self):
        ingreso = 1
        while ingreso == 1:
            direccion = self.vistaCliente.carga_direccion()
            if direccion.isspace() or len(direccion) == 0:
                self.vistaCliente.error_ingreso()
            elif direccion != '1': 
                self.cliente.set_direccion(direccion)
                ingreso = 0
            else:
                self.menu_principal()  
                
                
                
    def carga_senia(self):    
        self.calcular_costo()
        ingreso = 1
        while ingreso == 1:
            reserva = self.vistaEvento.senia_evento(self.evento.calcular_senia(), self.evento.get_costo())
            if reserva.isdigit():
                if int(reserva) != self.evento.calcular_senia() and reserva != '1':
                    self.vistaEvento.error_senia()
                elif reserva != '1': 
                    estado = self.verificar_datos_ingresados()
                    if estado:
                        self.menu_principal()
                    else:
                        self.ingresoSenia = reserva
                        self.cargar_evento() 
                        self.cargar_cliente()
                        self.vistaEvento.reserva_exito()
                        self.reset_variables()
                        ingreso = 0
                else:
                    self.menu_principal() 
            else:
                self.vistaEvento.error_senia()
        
        
        
    def verificar_datos_ingresados(self):
        estado = False
        if self.cliente.get_nombre() == '' or self.cliente.get_apellido() == '' or self.cliente.get_telefono() == '' or self.cliente.get_direccion() == '' or self.cliente.get_dni() == '':
            self.vistaEvento.error_documentacion()
            estado = True
        if self.listaServiciosTemporales == []:
            self.vistaServicio.error_documentacion()
            estado = True
        if self.ingresoFecha == 0:
            self.vistaEvento.error_documentacion()
            estado = True
        return estado
       
       
        
    def cargar_evento(self):
        try:
            with open("eventos.txt", "r+") as archivo:
                lineas = archivo.readlines()
                lineas_modificadas = []
                for index, linea in enumerate(lineas):
                    if index == (self.ingresoFecha-1):
                        if self.ingresoFecha < 10 :
                            fecha = "0" + str(self.ingresoFecha) + "/07/2023"
                        else:
                            fecha = str(self.ingresoFecha) + "/07/2023"
                        lineas_modificadas.append(str(fecha)+";"+ str(self.cliente.get_dni())+";"+ str(self.listaServiciosTemporales)+";"+self.ingresoSenia+";"+ str(self.evento.get_costo())+";"+ "1\n")
                    else:
                        lineas_modificadas.append(linea)               
                archivo.seek(0)                
                archivo.writelines(lineas_modificadas)
                archivo.truncate() 
        except Exception as e:
            print(f"A ocurrido el siguiente error: {e}")    
            
            
          
    def cargar_cliente(self):
        try:
            with open("clientes.txt", "a+") as archivo:
                lineas = archivo.readlines()
                estado = False
                for linea in lineas:
                    campos = linea.split(";")
                    if campos[2].strip().split(".") == self.cliente.get_dni().strip().split("."):
                        estado = True
                if estado == False:
                    nueva_linea = f"{self.cliente.get_nombre()};{self.cliente.get_apellido()};{self.cliente.get_dni()};{self.cliente.get_direccion()};{self.cliente.get_telefono()}\n"
                    archivo.write(nueva_linea)                
        except Exception as e:
            print(f"A ocurrido el siguiente error: {e}")        
                
                
                
    def cancelar_evento(self):
        self.limpiar_consola()
        dni = self.vistaCliente.carga_dni()
        estado = False
        if dni != '1':
            for evento in self.listaEvento:
                if evento.get_cliente() == dni:
                    estado = True
                    estadoVerificacion = self.verificar_cancelacion(evento.get_fecha())
                    if estadoVerificacion:                        
                        self.vistaEvento.fecha_evento(evento.get_fecha())
                        valueCancel = 'x'
                        while valueCancel == 'x':
                            estadoCancelacion = self.vistaEvento.cancelacion_evento()
                            if estadoCancelacion.lower() == 'si':  
                                self.calcular_costo()         
                                monto = self.calcular_devolucio(evento.get_cliente())
                                self.vistaEvento.devolucion_reserva(str(monto), evento.get_senia())
                                self.vistaEvento.confirmacion_cancelacion()
                                self.eliminar_evento(evento.get_fecha())
                                self.reset_variables()
                                valueCancel = 'ok'
                                return                         
                            elif estadoCancelacion.lower() == 'no':
                                return
                            else:
                                valueCancel = 'x'
                                self.vistaEvento.error_ingreso()
                    else:                    
                        self.vistaEvento.cancelacion_fuera_fecha(evento.get_fecha())
                        estadoCancelacion = self.vistaEvento.cancelacion_evento()
                        if estadoCancelacion.lower() == 'si': 
                            self.eliminar_evento(evento.get_fecha())
                            self.reset_variables()
                            valueCancel = 'ok'
                            return 
                        elif estadoCancelacion.lower() == 'no':
                            return
                        else:
                            valueCancel = 'x'
                            self.vistaEvento.error_ingreso()    
                            self.cancelar_evento()                      
                    
            if estado == False:
                ingreso = self.vistaEvento.error_buscar_dni()
                if ingreso == '1':
                    self.limpiar_consola()
                    self.cancelar_evento()
                else:
                    self.menu_principal()        
        else:
            self.menu_principal()
                
    
    
    def calcular_devolucio(self, dni):
        for evento in self.listaEvento:  
            if dni in evento.get_cliente():
                return float(evento.get_senia())*0.20    

  
  
    def verificar_cancelacion(self, fecha):
        try: 
            fechaActual = date.today()
            fechaEvento = datetime.strptime(fecha, "%d/%m/%Y").date()
            diferencia = abs((fechaActual - fechaEvento).days)
            fechaActual_str = fechaActual.strftime("%d/%m/%Y")
            fechaEvento_str = fechaEvento.strftime("%d/%m/%Y")
            if diferencia >= 15:
                return True
            else:                
                return False
        except Exception as e:
            print(f"A ocurrido el siguiente error: {e}")   



    def eliminar_evento(self, fecha):        
        try:
            with open("eventos.txt", "r+") as archivo:
                lineas = archivo.readlines()
                lineas_modificadas = []
                for index, linea in enumerate(lineas):
                    campos = linea.strip().split(";")
                    fechaRegistrada = campos[0]
                    if fechaRegistrada == fecha: 
                        if index < 9 :
                            fecha = "0" + str(index + 1) + "/07/2023"
                        else:
                            fecha = str(index + 1) + "/07/2023"
                        lineas_modificadas.append(str(fecha)+";"+"0"+";"+"0"+";"+"0"+";"+"0"+";"+"0\n")
                    else:
                        lineas_modificadas.append(linea)               
                archivo.seek(0)                
                archivo.writelines(lineas_modificadas)
                archivo.truncate() 
        except Exception as e:
            print(f"A ocurrido el siguiente error: {e}")    



    def verificar_reserva(self): 
        self.limpiar_consola()
        estado = True
        while estado:       
            dni = self.vistaCliente.carga_dni()
            if dni == "1":
                self.menu_principal()
            elif dni.isdigit():
                estadoDni = True
                for evento in self.listaEvento:
                    if dni == evento.get_cliente():
                        estadoDni = False
                        self.vistaCliente.evento_reservado(evento.get_fecha())
                        cont = 0
                        for index, servicio in enumerate(self.listaServicio):
                            for i in evento.get_servicio():
                                if str(index+1) == i:
                                    cont += 1
                                    self.vistaServicio.servicios_para_eliminar(cont, servicio.get_nombre())
                        break
                if estadoDni:
                    estado3 = True
                    while estado3:    
                        ingreso2 = self.vistaCliente.error_sin_evento()
                        if ingreso2 == "1":
                            self.verificar_reserva()
                        elif ingreso2 == "0":
                            self.menu_principal()
                        else:
                            self.vistaEvento.error_ingreso()
                estado2 = True                    
                while estado2:
                    ingreso = self.vistaCliente.vista_atras()
                    if ingreso == "1":
                        self.menu_principal()
                    else:
                        self.vistaCliente.error_ingreso()
            else:
                self.vistaCliente.error_ingreso()