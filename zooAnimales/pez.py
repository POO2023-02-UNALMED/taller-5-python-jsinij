from zooAnimales.animal import Animal

class Pez(Animal):

    _listado = []
    salmones = 0
    bacalaos = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        self._listado.append(self)
        
    @staticmethod
    def cantidadPeces():
        return len(Pez._listado)
    
    @staticmethod
    def movimiento():
        return "volar"
                
    def setListado(listado):
        Pez._listado = listado
        
    def getListado():
        return Pez._listado
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
        
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas
        
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones += 1 
        return cls(nombre, edad, "oceano", genero, "rojo", 6)

    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        cls.bacalaos += 1 
        return cls(nombre, edad, "oceano", genero, "gris", 6)
    