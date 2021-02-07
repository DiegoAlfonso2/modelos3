from model.poblacion import Poblacion
import model.constantes as constantes

class Algoritmo():
  def __init__(self, cantidad_iteraciones, funcion_fitness):
    self.cantidad_iteraciones = cantidad_iteraciones
    self.funcion_fitness = funcion_fitness
    self.mejor_solucion = None
    self.fitness_mejor_solucion = 0
  def obtener_solucion_optima(self, plantas, macetas):
    pob = Poblacion(cantidad_de_pobladores=constantes.CANT_POBLADORES, semanas=constantes.SEMANAS)
    pob.crear_poblacion_aleatoria(plantas, macetas)
    pob.crear_poblacion_sembrada(plantas, macetas)
    self.mejor_solucion, self.fitness_mejor_solucion = pob.obtener_mejor_poblador(self.funcion_fitness)
    
    # //mientras no se cumpla la condicion de parada
    #   // encontrar P(t) a partir de P(t-1) (seleccion y cruce)
    #   // modificar P(t)
    #   // evaluar P(t)
    return self.mejor_solucion, self.fitness_mejor_solucion