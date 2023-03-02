class Personaje:
  '''Clase que representa un personaje de juego'''
  def __init__(self,nombre):
    '''Genera los atributos del personaje, tomando el nombre ingresado por parametro'''
    self.nombre=nombre
    self.vida=100
    self.nivel=1
    self.experiencia=1
    self.fuerza=1
 
  def recibir_golpe(self,golpe):
    '''Actualiza la vida del personaje tomando el valor del golpe introducido como parametro'''
    if self.vida>golpe:
      self.vida-=golpe
      print(f'{self.nombre}: Golpe recibido, queda {self.vida} de vida')
    else:
      self.vida=0
      print(f'{self.nombre}: Game Over')
 
  def reponer_vida(self,vida):
    '''Actuliza la vida del personaje, reponiendo el valor ingresado como parametro, no puede ser mayor a 100'''
    if (self.vida+vida)>100:
      print(f'{self.nombre}: Valor ingresado no valido, la vida no puede ser mayor a 100')
    elif self.vida==0:
      print(f'{self.nombre}: Game Over')
    else:
      self.vida+=vida
      print(f'Vida repuesta, queda {self.vida} de vida')
  
  def golpear(self,nombre):
    '''Actualiza la vida del enemigo (ingresado como parametro), tomando el valor del golpe introducido como parametro'''
    if self.vida==0:
      print(f'{self.nombre}: Game Over')
    else:
      nombre.recibir_golpe(self.fuerza)
    if nombre.vida==0:
      print(f'{self.nombre}: Has matado a un enemigo')
      self.ganar_exp(1)
      
  def ganar_exp(self,x):
    '''Incrementa la experiencia al valor introducido como parametro'''
    self.experiencia+=x
    self.fuerza+=x
    if self.experiencia>10 or self.fuerza>10:
      self.experiencia-=10
      self.fuerza-=10
      print(f'{self.nombre}: Ganaste {x} puntos de experiencia y fuerza')
      self.subir_nivel(1)
    else:
      print(f'{self.nombre}: Ganaste {x} puntos de experiencia y fuerza')
  def subir_nivel(self,x):
    '''Incrementa el Nivel sumando el valor ingresado como parametro'''
    self.nivel+=x
    if self.nivel>=10:
      self.nivel=1
      self.experiencia=1
      self.fuerza=1
      self.vida=100
      print( f'{self.nombre}: Nivel máximo alcanzado, felicidades {self.nombre}! Reseteando.')
    else:
      print (f'{self.nombre}: Level up! Estás en el nivel {self.nivel}')
  def mostrar_detalle(self):
    print (f'Nombre del personaje: {self.nombre}*vida:{self.vida}*exp:{self.experiencia}*fuerza:{self.fuerza}*nivel{self.nivel}')
