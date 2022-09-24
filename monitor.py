class Monitor:#calse monitor
    contador_monitor = 0#atributo de clase contador
    def __init__(self, marca, tamaño):#constructor
        Monitor.contador_monitor += 1#incrementamos el contador
        self._id_monitor = Monitor.contador_monitor#atributo privado id monitor
        self._marca = marca#atributo privado marca
        self._tamaño = tamaño#atributo privado tamaño
    
    def __str__(self):#sobreescribimos el metodo str
        return f'Id: {self._id_monitor}, Marca: {self._marca}, Tamaño: {self._tamaño}'

if __name__ == '__main__':#si el archivo se ejecuta directamente
    Monitor1= Monitor('Redragon','24')#creamos un objeto de la clase monitor
    Monitor2= Monitor('Asus','27')#creamos un objeto de la clase monitor
    print(Monitor1)#imprimimos el objeto
    print(Monitor2)#imprimimos el objeto



