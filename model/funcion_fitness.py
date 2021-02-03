class FuncionFitness():
  def __init__(self):
    penalizaciones = []
  def calcular_fitness_de_solucion(self, solucion):
    if not solucion.es_solucion_factible():
      return 0
    fitness = 0
    for accion in solucion.acciones:
      planta = accion.planta
      fitness += planta.produccion_por_planta * planta.precio
    return fitness