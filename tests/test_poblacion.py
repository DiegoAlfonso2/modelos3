from model.poblacion import Poblacion
from model.solucion import Solucion
from model.maceta import Maceta
from model.planta import Planta
from model.accion import Accion
from model.funcion_fitness import FuncionFitness
from drawing.graficador_soluciones import GraficadorSoluciones
import random_helper

class TestPoblacion():
  maceta1 = Maceta('PoblacionMaceta1', 30, 60)
  planta1 = Planta('Planta1', (255,0,0,128), [2, 2, 4, 4, 6, 6, 6])
  def test_cruzar_soluciones_sin_interseccion(self):
    pob = Poblacion()
    sol1 = Solucion()
    sol2 = Solucion()
    accion1 = Accion(self.planta1, self.maceta1, (10, 10), 1)
    accion2 = Accion(self.planta1, self.maceta1, (40, 40), 2)
    sol1.agregar_accion(accion1)
    sol2.agregar_accion(accion2)
    sol3 = pob.cruzar_soluciones(sol1, sol2)
    GraficadorSoluciones([self.maceta1]).graficar_solucion(sol3)
    assert accion1 in sol3.acciones
    assert accion2 in sol3.acciones
    
  def test_cruzar_soluciones_interseccion_gana_accion1(self):
    pob = Poblacion(choice_function=lambda x: x[1])
    sol1 = Solucion()
    sol2 = Solucion()
    accion1 = Accion(self.planta1, self.maceta1, (10, 10), 1)
    accion2 = Accion(self.planta1, self.maceta1, (10, 20), 2)
    accion3 = Accion(self.planta1, self.maceta1, (45, 45), 1)
    sol1.agregar_accion(accion1)
    sol2.agregar_accion(accion2)
    sol1.agregar_accion(accion3)
    sol3 = pob.cruzar_soluciones(sol1, sol2)
    GraficadorSoluciones([self.maceta1]).graficar_solucion(sol3)
    assert accion1 in sol3.acciones
    assert accion2 not in sol3.acciones
    assert accion3 in sol3.acciones

  def test_cruzar_soluciones_interseccion_gana_accion2(self):
    pob = Poblacion(choice_function=lambda x: x[0])
    sol1 = Solucion()
    sol2 = Solucion()
    accion1 = Accion(self.planta1, self.maceta1, (10, 10), 1)
    accion2 = Accion(self.planta1, self.maceta1, (10, 20), 2)
    accion3 = Accion(self.planta1, self.maceta1, (45, 45), 1)
    sol1.agregar_accion(accion1)
    sol2.agregar_accion(accion2)
    sol1.agregar_accion(accion3)
    sol3 = pob.cruzar_soluciones(sol1, sol2)
    GraficadorSoluciones([self.maceta1]).graficar_solucion(sol3)
    assert accion1 not in sol3.acciones
    assert accion2 in sol3.acciones
    assert accion3 in sol3.acciones

  def test_mutar_solucion_agregar_accion(self):
    choice = random_helper.inicializador_random([1, 0, 1])
    randint = random_helper.inicializador_random([8, 22])
    pob = Poblacion(choice_function=lambda x: x[choice()], randint_function=lambda i, r=0: randint())
    sol = Solucion()
    planta2 = Planta('Planta2', (0, 128, 128, 128), [4, 4, 4, 4])
    accion1 = Accion(self.planta1, self.maceta1, (45, 45), 1)
    sol.agregar_accion(accion1)
    accion_esperada = Accion(planta2, self.maceta1, (8, 22), 2)
    assert accion_esperada not in sol.acciones
    resultado_mutacion = pob.mutar_solucion_agregar_accion(sol, [self.planta1, planta2], [self.maceta1])
    assert resultado_mutacion != sol
    assert accion1 in resultado_mutacion.acciones
    assert accion_esperada in resultado_mutacion.acciones
  
  def test_mutar_solucion_agregar_accion_sin_forzar_azar(self):
    pob = Poblacion()
    sol = Solucion()
    planta2 = Planta('Planta2', (0, 128, 128, 128), [4, 4, 4, 4], semanas_validas_plantacion=[1,2,9,10])
    accion1 = Accion(self.planta1, self.maceta1, (45, 45), 1)
    sol.agregar_accion(accion1)
    resultado_mutacion = pob.mutar_solucion_agregar_accion(sol, [self.planta1, planta2], [self.maceta1])
    GraficadorSoluciones([self.maceta1]).graficar_solucion(resultado_mutacion)
  
  def test_crear_poblacion_aleatoria(self):
    cantidad_pobladores = 100
    pob = Poblacion(cantidad_pobladores)
    planta2 = Planta('Planta2', (0, 128, 128, 128), [4, 4, 4, 4], semanas_validas_plantacion=[1,2,9,10])
    pob.crear_poblacion_aleatoria([self.planta1, planta2], [self.maceta1])
    # for sol in pob.soluciones:
    #   GraficadorSoluciones([self.maceta1]).graficar_solucion(sol)
  
  def test_crear_poblacion_sembrada(self):
    pob = Poblacion()
    planta2 = Planta('Planta2', (0, 128, 128, 128), [4, 4, 4, 4], semanas_validas_plantacion=[1,2,9,10])
    pob.crear_poblacion_sembrada([self.planta1, planta2], [self.maceta1])
    for sol in pob.soluciones:
      GraficadorSoluciones([self.maceta1]).graficar_solucion(sol)
  
  def test_seleccion_y_cruce(self):
    cantidad_pobladores = 100
    pob = Poblacion(cantidad_pobladores)
    planta2 = Planta('Planta2', (0, 128, 128, 128), [4, 4, 4, 4], semanas_validas_plantacion=[1,2,9,10])
    pob.crear_poblacion_aleatoria([self.planta1, planta2], [self.maceta1])
    pob.crear_poblacion_sembrada([self.planta1, planta2], [self.maceta1])
    fitness = FuncionFitness()
    for i in range(50):
      if i % 10 == 0:
        print(i)
      generacion2 = pob.seleccionar_y_cruzar(fitness)
      pob.soluciones = generacion2
    for solucion in generacion2:
      GraficadorSoluciones([self.maceta1]).graficar_solucion(solucion)
  
  def test_mutar_poblacion(self):
    cantidad_pobladores = 100
    pob = Poblacion(cantidad_pobladores)
    planta2 = Planta('Planta2', (0, 128, 128, 128), [4, 4, 4, 4], semanas_validas_plantacion=[1,2,9,10])
    pob.crear_poblacion_aleatoria([self.planta1, planta2], [self.maceta1])
    pob.crear_poblacion_sembrada([self.planta1, planta2], [self.maceta1])
    pob.mutar_poblacion(0.02, [self.planta1, planta2], [self.maceta1])