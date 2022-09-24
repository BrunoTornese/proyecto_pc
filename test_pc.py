from teclado import teclado
from mouse import mouse
from monitor import Monitor
from computadora import Computadora
from orden import Orden

teclado1=teclado('redragon','USB')#creamos un objeto teclado
mouse1=mouse('razer','USB')#creamos un objeto mouse
monitor1=Monitor('redragon',24)#creamos un objeto monitor
computadora1=Computadora('pc gamer',monitor1,teclado1,mouse1)#creamos un objeto computadora


teclado2=teclado('logtech','USB')#creamos un objeto teclado
mouse2=mouse('redragon','USB')#creamos un objeto mouse
monitor2=Monitor('asus',27)#creamos un objeto monitor
computadora2=Computadora('pc gamer 2',monitor2,teclado2,mouse2)#creamos un objeto computadora


computadoras=[computadora1,computadora2]#creamos una lista de computadoras
orden1=Orden(computadoras)#creamos un objeto orden
print(orden1)#imprimimos el objeto orden

