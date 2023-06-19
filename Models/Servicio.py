class Servicio:
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo
        
        
    
    def get_nombre(self):
        return self.nombre
        
    def get_costo(self):
        return self.costo
    
   
    
    def set_nombre(self, newName):
        self.nombre = newName
        
    def set_costo(self, newCosto):
        self.costo = newCosto
    

        
        
    def __str__(self, index):
        formatName = ' '.join(word.capitalize() for word in self.nombre.strip().split())
        return (f"\n{index}. {formatName}, Costo: ${self.costo}")
        
        
    