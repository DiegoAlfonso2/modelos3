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