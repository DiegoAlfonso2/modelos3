from model.poblacion import Poblacion
import model.constantes as constantes

class Algoritmo():
  def __init__(self, cantidad_iteraciones, funcion_fitness, probabilidad_de_mutacion=0.02):
    self.cantidad_iteraciones = cantidad_iteraciones
    self.funcion_fitness = funcion_fitness
    self.mejor_solucion = None
    self.fitness_mejor_solucion = 0
    self.probabilidad_de_mutacion = probabilidad_de_mutacion
  def obtener_solucion_optima(self, plantas, macetas):
    pob = Poblacion(cantidad_de_pobladores=constantes.CANT_POBLADORES, semanas=constantes.SEMANAS)
    pob.crear_poblacion_aleatoria(plantas, macetas)
    pob.crear_poblacion_sembrada(plantas, macetas)
    self.mejor_solucion, self.fitness_mejor_solucion = pob.obtener_mejor_poblador(self.funcion_fitness)
    for i in range(self.cantidad_iteraciones):
      pob.seleccionar_cruzar_y_reemplazar(self.funcion_fitness)
      pob.mutar_poblacion(self.probabilidad_de_mutacion, plantas, macetas)
      mejor_solucion, fitness_mejor_solucion = pob.obtener_mejor_poblador(self.funcion_fitness)
      if fitness_mejor_solucion > self.fitness_mejor_solucion:
        self.mejor_solucion = mejor_solucion
    return self.mejor_solucion, self.fitness_mejor_solucion