from functools import reduce

class FuncionFitness():
  def __init__(self):
    self.penalizaciones = []
  def calcular_fitness_de_solucion(self, solucion):
    if not solucion.es_solucion_factible():
      return 0
    fitness = 0
    for accion in solucion.acciones:
      planta = accion.planta
      fitness += planta.produccion_por_planta * planta.precio
    for penalizacion in self.penalizaciones:
      fitness = penalizacion(fitness, solucion)
    return fitness
  def agregar_penalizacion(self, penalizacion):
    self.penalizaciones.append(penalizacion)
  
def penalizacion_porcentaje_planta(planta, porcentaje, porc_penalizacion, func_comparacion=lambda a,b: a >= b):
  def penalizacion(fitness, solucion):
    peso_total_cosecha = reduce(lambda x,y: x+y, map(lambda accion: accion.planta.produccion_por_planta, solucion.acciones),0)
    if not peso_total_cosecha:
      return 0
    peso_planta = reduce(lambda x,y: x+y, map(lambda accion: accion.planta.produccion_por_planta, filter(lambda accion: accion.planta == planta, solucion.acciones)),0)
    return fitness if func_comparacion(float(peso_planta) / peso_total_cosecha, porcentaje) else fitness * porc_penalizacion
  return penalizacion
