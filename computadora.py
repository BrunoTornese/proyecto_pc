from teclado import  teclado
from mouse import mouse
from monitor import Monitor
class Computadora:#Clase Computadora
    contador_computadoras = 0#atributo de clase contador
    def __init__(self, nombre, monitor, teclado, mouse):#constructor
        Computadora.contador_computadoras += 1#incrementamos el contador
        self._id_computadora = Computadora.contador_computadoras#atributo privado id computadora
        self._nombre = nombre#atributo privado nombre
        self._monitor = monitor#atributo privado monitor
        self._teclado = teclado#atributo privado teclado
        self._mouse = mouse#atributo privado mouse


    def __str__(self):#metodo str
        return f'''
        {self._nombre}: {self._id_computadora} 
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Mouse: {self._mouse}
        '''#retornamos los atributos de la computadora

if __name__ == '__main__':#si el archivo se ejecuta directamente
    teclado1=teclado('redragon','USB')#creamos un objeto teclado
    mouse1=mouse('razer','USB')#creamos un objeto mouse
    monitor1=Monitor('redragon',24)#creamos un objeto monitor
    computadora1=Computadora('pc gamer',monitor1,teclado1,mouse1)#creamos un objeto computadora
    print(computadora1)#imprimimos el objeto computadora
    teclado2=teclado('logtech','USB')#creamos un objeto teclado
    mouse2=mouse('redragon','USB')#creamos un objeto mouse
    monitor2=Monitor('asus',27)#creamos un objeto monitor
    computadora2=Computadora('pc gamer 2',monitor2,teclado2,mouse2)#creamos un objeto computadora
    print(computadora2)#imprimimos el objeto computadora
