from dispositivo_entrada import *#importamos la clase padre
class teclado(dispositivo_entrada):#clase hija
    contador_teclado = 0#atributo de clase
    def __init__(self, marca, tipo_entrada):#constructor
        teclado.contador_teclado += 1#incrementamos el contador
        self._id_teclado = teclado.contador_teclado#atributo privado id teclado
        super().__init__(marca, tipo_entrada)#llamamos al constructor de la clase padre

    def __str__(self) -> str:
        return f'Id: {self._id_teclado}, Marca: {self._marca}, Tipo de entrada: {self._tipo_entrada}'#sobreescribimos el metodo str


if __name__ == '__main__': #si el archivo se ejecuta directamente
    Teclado1= teclado('Razer','USB')#creamos un objeto de la clase teclado
    Teclado2= teclado('Logitech','Inalambrica')#creamos un objeto de la clase teclado
    print(Teclado1)#imprimimos el objeto
    print(Teclado2)#imprimimos el objeto