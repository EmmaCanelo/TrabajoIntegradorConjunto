class Cliente:
    def __init__(self, nombre, apellido, dni, direccion, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
        self.direccion = direccion
        
    
    def get_nombre(self):
        return self.nombre
    
    def get_apellido(self):
        return self.apellido
    
    def get_dni(self):
        return self.dni
    
    def get_telefono(self):
        return self.telefono
    
    def get_direccion(self):
        return self.direccion
    
    
    def set_nombre(self, newNombre):
        self.nombre = newNombre
    
    def set_apellido(self, newApellido):
        self.apellido = newApellido
    
    def set_dni(self, newDni):
        self.dni = newDni
    
    def set_telefono(self, newTelefono):
        self.telefono = newTelefono
    
    def set_direccion(self, newDireccion):
        self.direccion = newDireccion
    
    
    def __str__(self):
        return (f"\nCLIENTE: Nombre: {self.nombre}, Apellido: {self.apellido}, Dni: {self.dni}, Telefono: {self.telefono}, Direccion: {self.direccion}")