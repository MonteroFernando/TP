#EJERCICIO 1
def Crear_Archivo_Texto(ruta,nombre_archivo,contenido):
    '''Escribir una función que permita crear un archivo de texto con algún contenido. 
        La ruta de acceso al archivo y su contenido deben ser pasados por parámetro. 
        Si el archivo ya existía, sobrescribirlo.'''
    nruta=ruta+nombre_archivo
    with open(nruta,'w') as archivo:
        archivo.write(contenido)

#ejemplo
ruta = './'
nombre_archivo = 'textoj1.txt'
contenido = 'Este es el contenido del Ejercicio nro 1'

Crear_Archivo_Texto(ruta,nombre_archivo,contenido)

#EJERCICIO 2
def Agragar_Contenido_Archivo(ruta,contenido):
    '''Escribir una función que permita agregar contenido a un archivo de texto. 
        La ruta de acceso al archivo y el contenido a agregar deben ser pasados por parámetro.'''
    with open(ruta,'a') as archivo:
        archivo.write(contenido)
#ejemplo
ruta=ruta+nombre_archivo
contenido='\nEste es el contenido de Ejercicio 2'

Agragar_Contenido_Archivo(ruta,contenido)

#EJERCICIO 3
def Mostar_Contenido(ruta):
    '''Escribir una función que permita mostrar todo el contenido de un archivo de texto.
        La ruta de acceso al archivo debe ser pasada por parámetro.'''
    with open(ruta,'r') as archivo:
        contenido=archivo.read()
        return contenido
    
#ejemplo
print(f'El contenido del archivo en {ruta} es: \n{Mostar_Contenido(ruta)}')

#EJERCICIO 4
def Contar_Caracteres(ruta):
    '''Escriba una función que devuelva la cantidad de caracteres de un archivo de texto. 
        la ruta de acceso al archivo debe ser pasada por parámetro.
        No se debe tener en cuenta el caracter '\n'.'''
    contador=0
    with open(ruta,'r') as archivo:
        contenido=archivo.read()
        return (len(contenido)-1)#-1 porque cuenta un 0 al final del archivo
#ejemplo        
print(f'La cantidad de caracteres del archivo es: {Contar_Caracteres(ruta)}')

# EJERCICIO 5
def Contar_Lineas(ruta):
    '''Escribir una función que devuelva la cantidad de líneas que tiene un archivo de texto.
        La ruta de acceso del archivo debe ser pasada por parámetro.'''
    with open(ruta,'r') as archivo:
        contenido=archivo.readlines()
        return(len(contenido))
#ejemplo
print(f'La cantidad de lineas del archivo es: {Contar_Lineas(ruta)}')

#EJERCICIO 6
def Devolver_Linea(ruta,linea):
    '''Escribir una función que devuelva la n-ésima línea de un archivo de texto. 
        La ruta de acceso del archivo y el número de línea deben ser pasados por parámetro.
        Si el archivo tiene menos cantidad de líneas de lo que se pide debe mostrar un mensaje por pantalla informándolo.'''
    with open(ruta,'r') as archivo:
        contenido=archivo.readlines()
        if len(contenido)<linea:
            print('el arhivo posee menos linead de la consultada')
        elif linea<=0:
            print('La linea ingreada debe ser mayo a 0')
        else:
            return(contenido[linea-1])
#ejemplo
print(f'El contenido de la linea ingresada es:\n>{Devolver_Linea(ruta,0)}')
#EJERCICIO 7
class Archivo():
    '''Definir una clase que maneje un archivo. 
        El nombre (ruta) del archivo debe establecerse al crear un objeto de la clase.
        La clase debe implementar:

        *Un método que cree el archivo. Si el archivo ya existe lo sobrescribe. 
         Opcionalmente puede recibir un parámetro con contenido para incluir en el archivo.
        *Un método que permita agregar contenido al archivo.
        *Un método que muestre todo el contenido del archivo por pantalla.
        *Un método que devuelva la cantidad total de caracteres del archivo, sin contar el caracter \n. 
         Extra: hacer que este sea el método especial __len__().
        *Una propiedad de solo lectura que devuelva la cantidad total de líneas del archivo.
         Instancie un objeto de la clase y utilice sus métodos.'''
    def __init__(self,ruta,contenido):
        '''Constructor'''
        self.ruta=ruta
        self.__lineas=0
        self.crear()
        self.agregar(contenido)
        self.set_clineas()
    def crear(self):
        '''Crea un arvhico si existe lo sobrescribe'''
        with open(self.ruta,'w') as archivo:
            archivo.write("")
    def agregar(self,contenido):
        '''Agrega al archivo el contenido pasado como parametro'''
        with open(self.ruta,'a') as archivo:
            archivo.writelines(contenido)
    def ver_contenido(self):
        '''Muestra el contenido del archivo'''
        with open(self.ruta,'r') as archivo:
            contenido=""
            for linea in archivo:
                contenido+=linea
            return '"'+contenido[:-1]+'"'
    def __len__(self):
        '''Metodo especial len'''
        with open(self.ruta,'r') as archivo:
            contenido=archivo.read()
        return len(contenido)-1
    #metodo Getter
    def get_lineas(self):
        return self.__lineas
    #metodo Setter
    def set_clineas(self):
        with open(self.ruta,'r') as archivo:
            text=archivo.readlines()
            self.__lineas=len(text)
    
#ejemplo
ruta='./ejercicio7.txt'
contenido=['Esta es la primer linea del archivo para el ejercicio7\n','Esta es la segunda linea\n','Esta es la tercer linea\n']

texto=Archivo(ruta,contenido)


print(f'Detalle del archivo creado:\n*Ruta: {ruta}\n*Contenido:\n{texto.ver_contenido()}\n*Cantidad de caracteres {len(texto)}\n*Cantidad de lineas:{texto.get_lineas()}')



        






        



    










