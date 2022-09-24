from dispositivo_entrada import *#importamos la clase padre
class mouse(dispositivo_entrada):#clase hija
    contador_mouse = 0#atributo de clase
    def __init__(self, marca, tipo_entrada):#constructor
        mouse.contador_mouse += 1#incrementamos el contador
        self._id_mouse = mouse.contador_mouse#atributo privado id mouse 
        super().__init__(marca, tipo_entrada)#llamamos al constructor de la clase padre

    def __str__(self) -> str:#sobreescribimos el metodo str
        return f'Id: {self._id_mouse}, Marca: {self._marca}, Tipo de entrada: {self._tipo_entrada}'#sobreescribimos el metodo str



if __name__ == '__main__':#si el archivo se ejecuta directamente
    Mouse1= mouse('Razer','USB')#creamos un objeto de la clase mouse
    Mouse2= mouse('Logitech','Inalambrica')#creamos un objeto de la clase mouse
    print(Mouse1)#imprimimos el objeto
    print(Mouse2)#  imprimimos el objeto

