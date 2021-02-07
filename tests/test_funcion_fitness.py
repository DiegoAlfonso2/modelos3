from functools import reduce
from model.funcion_fitness import FuncionFitness
from model.solucion import Solucion
from model.planta import Planta
from model.maceta import Maceta
from model.accion import Accion

class TestFuncionFitness():
  def test_fitness_solucion_factible_unica_accion(self):
    fitness = FuncionFitness()
    sol = Solucion()
    # Nombre de planta, color, crecimiento, produccion por planta, precio por kg
    lechuga = Planta('Lechuga', (0, 255, 0, 255), [2, 2, 4, 4, 6, 6], 0.25, 180)
    jardinera = Maceta('Jardinera', 30, 60)
    accion = Accion(lechuga, jardinera, (15, 15), 1)
    sol.agregar_accion(accion)
    assert fitness.calcular_fitness_de_solucion(sol) == 45
  
  def test_fitness_solucion_factible_dos_acciones_misma_planta(self):
    fitness = FuncionFitness()
    sol = Solucion()
    # Nombre de planta, color, crecimiento, produccion por planta, precio por kg
    lechuga = Planta('Lechuga', (0, 255, 0, 255), [2, 2, 4, 4, 6, 6], 0.25, 180)
    jardinera1 = Maceta('Jardinera 1', 30, 60)
    jardinera2 = Maceta('Jardinera 2', 30, 60)
    accion1 = Accion(lechuga, jardinera1, (15, 15), 1)
    accion2 = Accion(lechuga, jardinera2, (15, 15), 1)
    sol.agregar_accion(accion1)
    sol.agregar_accion(accion2)
    assert fitness.calcular_fitness_de_solucion(sol) == 90
    
  def test_fitness_solucion_factible_dos_acciones_distinta_planta(self):
    fitness = FuncionFitness()
    sol = Solucion()
    lechuga = Planta('Lechuga', (0, 255, 0, 255), [2, 2, 4, 4, 6, 6], 0.25, 180)
    zanahoria = Planta('Zanahoria', (255, 0, 0, 255), [2, 2, 2, 2, 2], 0.05, 45)
    jardinera = Maceta('Jardinera', 30, 60)
    accion1 = Accion(lechuga, jardinera, (10, 10), 1)
    accion2 = Accion(zanahoria, jardinera, (10, 20), 1)
    sol.agregar_accion(accion1)
    sol.agregar_accion(accion2)
    assert fitness.calcular_fitness_de_solucion(sol) == 47.25
  
  def test_fitness_solucion_no_factible(self):
    fitness = FuncionFitness()
    sol = Solucion()
    lechuga = Planta('Lechuga', (0, 255, 0, 255), [2, 2, 4, 4, 6, 6], 1, 1)
    jardinera = Maceta('Jardinera', 30, 60)
    accion1 = Accion(lechuga, jardinera, (8, 8), 1)
    accion2 = Accion(lechuga, jardinera, (8, 8), 1)
    sol.agregar_accion(accion1)
    sol.agregar_accion(accion2)
    assert fitness.calcular_fitness_de_solucion(sol) == 0

  def penalizacion_porcentaje_minimo_planta(self, planta, porcentaje, porc_penalizacion):
    def penalizacion(fitness, solucion):
      peso_total_cosecha = reduce(lambda x,y: x+y, map(lambda accion: accion.planta.produccion_por_planta, solucion.acciones))
      peso_planta = reduce(lambda x,y: x+y, map(lambda accion: accion.planta.produccion_por_planta, filter(lambda accion: accion.planta == planta, solucion.acciones)),0)
      return fitness if float(peso_planta) / peso_total_cosecha >= porcentaje else fitness * porc_penalizacion
    return penalizacion

  def test_fitness_penalizacion(self):
    fitness = FuncionFitness()
    sol = Solucion()
    lechuga = Planta('Lechuga', (0, 255, 0, 255), [2, 2, 4, 4, 6, 6], 0.25, 180)
    zanahoria = Planta('Zanahoria', (255, 0, 0, 255), [2, 2, 2, 2, 2], 0.05, 45)
    jardinera = Maceta('Jardinera', 30, 60)
    # Si la cantidad de zanahoria no es al menos la mitad en kg de la cosecha total, bajo el funcional un 40%
    penalizacion = self.penalizacion_porcentaje_minimo_planta(zanahoria, 0.5, 0.6)
    accion1 = Accion(lechuga, jardinera, (10, 10), 1)
    accion2 = Accion(lechuga, jardinera, (10, 30), 1)
    sol.agregar_accion(accion1)
    sol.agregar_accion(accion2)
    fitness.agregar_penalizacion(penalizacion)
    assert fitness.calcular_fitness_de_solucion(sol) == 54