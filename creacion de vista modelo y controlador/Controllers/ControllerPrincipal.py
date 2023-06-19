import os
import sys
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
            elif ingreso == '2':
                ingreso = 2
                self.limpiar_consola()                
            elif ingreso == '3':
                ingreso = 3
                self.limpiar_consola()               
            elif ingreso == '4':
                ingreso = 4
                self.limpiar_consola()                
            elif ingreso == '5':
                ingreso = 5
                self.limpiar_consola()                     
            elif ingreso == '6':
                ingreso = 6
                self.limpiar_consola()                
            elif ingreso == '7':
                ingreso = 7      
                self.limpiar_consola()                
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
        
        
    
    
                    
    
    def limpiar_consola(self):
        os.system('cls') 
        #os.system('clear')
        
             
