from model.algoritmo import Algoritmo
from model.planta import Planta
from model.maceta import Maceta
from model.funcion_fitness import FuncionFitness
from drawing.graficador_soluciones import GraficadorSoluciones
from functools import reduce

class TestAlgoritmo():
  def test_algoritmo_una_maceta_dos_plantas(self):
    fitness = FuncionFitness()
    lechuga = Planta('Lechuga', (0, 255, 0, 255), [2, 2, 4, 4, 6, 6], 0.25, 180)
    zanahoria = Planta('Zanahoria', (255, 0, 0, 255), [2, 2, 2, 2, 2], 0.05, 45)
    jardinera = Maceta('Jardinera', 30, 60)
    # Si la cantidad de zanahoria no es al menos la mitad en kg de la cosecha total, bajo el funcional un 40%
    penalizacion = self.penalizacion_porcentaje_minimo_planta(zanahoria, 0.5, 0.6)
    fitness.agregar_penalizacion(penalizacion)
    algoritmo = Algoritmo(8, fitness)
    solucion, valor = algoritmo.obtener_solucion_optima([lechuga, zanahoria], [jardinera])
    print('El fitness de la mejor solucion obtenida es', valor)
    graficador = GraficadorSoluciones([jardinera])
    graficador.graficar_solucion(solucion)

  def test_algoritmo_dos_macetas_dos_plantas(self):
    fitness = FuncionFitness()
    lechuga = Planta('Lechuga', (0, 255, 0, 255), [2, 2, 4, 4, 6, 6], 0.25, 180)
    zanahoria = Planta('Zanahoria', (255, 0, 0, 255), [2, 2, 2, 2, 2], 0.05, 45)
    jardinera = Maceta('Jardinera', 30, 60)
    grande = Maceta('MacetaGrande', 60, 60)
    # Si la cantidad de zanahoria no es al menos la mitad en kg de la cosecha total, bajo el funcional un 40%
    penalizacion = self.penalizacion_porcentaje_minimo_planta(zanahoria, 0.5, 0.6)
    fitness.agregar_penalizacion(penalizacion)
    algoritmo = Algoritmo(8, fitness)
    solucion, valor = algoritmo.obtener_solucion_optima([lechuga, zanahoria], [jardinera, grande])
    print('El fitness de la mejor solucion obtenida es', valor)
    graficador = GraficadorSoluciones([jardinera])
    graficador.graficar_solucion(solucion)
  #TODO metodo repetido
  def penalizacion_porcentaje_minimo_planta(self, planta, porcentaje, porc_penalizacion):
    def penalizacion(fitness, solucion):
      peso_total_cosecha = reduce(lambda x,y: x+y, map(lambda accion: accion.planta.produccion_por_planta, solucion.acciones),0)
      if not peso_total_cosecha:
        return 0
      peso_planta = reduce(lambda x,y: x+y, map(lambda accion: accion.planta.produccion_por_planta, filter(lambda accion: accion.planta == planta, solucion.acciones)),0)
      return fitness if float(peso_planta) / peso_total_cosecha >= porcentaje else fitness * porc_penalizacion
    return penalizacion
