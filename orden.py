class Orden:
    contador_ordenes=0#atributo de clase contador
    def __init__(self,computadoras):#constructor
        Orden.contador_ordenes+=1#incrementamos el contador
        self._id_orden=Orden.contador_ordenes#atributo privado id orden
        self._computadoras=computadoras#atributo privado computadoras
    
    def agregar_computadora(self,computadora):#metodo agregar computadora
        self._computadoras.append(computadora)#agregamos la computadora a la lista de computadoras
    
    def __str__(self):#metodo str
        computadoras_str=''#variable computadoras str
        for computadora in self._computadoras:#recorremos la lista de computadoras
            computadoras_str+=computadora.__str__()#agregamos la computadora a la variable computadoras str
        return f'''
            Orden: {self._id_orden}
            Computadoras: {computadoras_str}
        '''#retornamos la variable computadoras str
        









