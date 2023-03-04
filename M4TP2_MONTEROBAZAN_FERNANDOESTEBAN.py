#EJERCICIO 1
import os
def Ingresar_Cadena(ruta=None):
    '''Crea una función que permite al usuario ingresar por teclado cuantas cadenas quiera e ir 
    almacenándolas como líneas en un archivo de texto. 
        La ruta de acceso del archivo se debe pasar por parámetro. 
        El archivo debe crearse si no existe y cada nueva línea debe agregarse 
    al final del archivo.
    Solicita reiteradamente al usuario por una nueva cadena hasta que decida no continuar.'''
    control = ""
    if ruta is None:
        return print('Se debe ingresar la ruta del archivo como parametro')
    if not os.path.isfile(ruta):
        print(os.path.isfile(ruta))
        i=input('presione una tecla para contunuar')
        with open(ruta,'w') as archivo:
            pass
    with open(ruta,'a') as archivo:
        while control.lower() not in ['no','n']:
            cadena=input('Ingrese la cadena a ingresar: ')
            cadena=cadena + '\n'
            archivo.write(cadena)
            control=input('¿Desea seguir ingresado cadenas?')
    
#ejemplo
ruta='./textoTP2M4E1.txt'
Ingresar_Cadena(ruta)
#EJERCICIO 2





