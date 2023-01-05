from tatuador import Tatuador

class TatuadorNuevo(Tatuador):
    
    tiempoExperiencia = int
    
    def __init__(self, nombre, edad, telefono, trabajo, tiempoExperiencia):
        super().__init__(nombre, edad, telefono, trabajo)
        
        self.tiempoExperiencia  = tiempoExperiencia