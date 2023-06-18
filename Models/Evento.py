class Evento:
    def __init__(self, fecha, cliente, servicio, senia, costo, estado):
        self.fecha = fecha
        self.cliente = cliente
        self.servicio = servicio
        self.senia = senia
        self.costo = costo
        self.estado = estado
        
    def get_cliente(self):
        return self.cliente
    
    def get_fecha(self):
        return self.fecha
    
    def get_costo(self):
        return self.costo
    
    def get_servicio(self):
        return self.servicio
    
    def get_estado(self):
        return self.estado
    
    def get_senia(self):
        return self.senia
        
    def set_cliente(self, newCliente):
        self.cliente = newCliente
    
    def set_fecha(self, newFecha):
        self.fecha = newFecha
        
    def set_senia(self, newSenia):
        self.senia = newSenia
    
    def set_costo(self, newCosto):
        self.costo = newCosto
        
    def set_servicio(self, newServicio):
        self.servicio = newServicio
        
    def set_estado(self, newEstado):
        self.cliente = newEstado
        
        
    def calcular_senia(self):
        return round(int(self.costo) * 0.3)

        
    def __str__(self):
        return (f"\nFecha: {self.fecha}, Cliente: {self.cliente}, Servicios: {self.servicio}, Costo: {self.costo}")
        
