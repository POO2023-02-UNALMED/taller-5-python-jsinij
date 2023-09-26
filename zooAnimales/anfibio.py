from zooAnimales.animal import Animal

class Anfibio(Animal):

    _listado = []
    ranas = 0
    salamandras = 0
    
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        self._listado.append(self)
        
        
    def setListado(listado):
        Anfibio._listado = listado
        
    def getListado():
        return Anfibio._listado
    
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel
    def getColorPiel(self):
        return self._colorPiel
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso
    def isVenenoso(self):
        return self._venenoso
    
    @classmethod
    def crearRana(cls,nombre, edad, genero):
        cls(nombre, edad, "selva", genero, "rojo", True)
        cls.ranas +=1
        
    @classmethod
    def crearSalamandra(cls,nombre, edad, genero):
        cls(nombre, edad, "selva", genero, "negro y amarillo", False)
        cls.salamandras += 1
    
    @staticmethod
    def cantidadAnfibios():
        return len(Anfibio._listado)
    
    @staticmethod
    def movimiento():
        return "saltar"