import random
import model.constantes as constantes
from model.solucion import Solucion
from model.accion import Accion

class Poblacion():
  def __init__(self, cantidad_de_pobladores=100, semanas=constantes.SEMANAS, rand_function=random.uniform, choice_function=random.choice, randint_function=random.randint):
    self.cantidad_pobladores = cantidad_de_pobladores
    self.soluciones = []
    self.semanas = semanas
    self.random = rand_function
    self.choice = choice_function
    self.randint = randint_function

  def cruzar_soluciones(self, sol1, sol2):
    # TODO refactor
    sol_cruce = Solucion()
    acciones_en_conflicto = [item for item in sol1.determinar_interseccion_con(sol2)] + [item for item in sol2.determinar_interseccion_con(sol1)]
    conflictos_eliminados = []
    for accion in sol1.acciones:
      sol_cruce.agregar_accion(accion)
    for accion in sol2.acciones:
      sol_cruce.agregar_accion(accion)
    while not sol_cruce.es_solucion_factible():
      conflicto_a_eliminar = self.choice(acciones_en_conflicto)
      conflictos_eliminados.append(conflicto_a_eliminar)
      acciones_en_conflicto.remove(conflicto_a_eliminar)
      sol_cruce = Solucion()
      for accion in sol1.acciones:
        if not accion in conflictos_eliminados:
          sol_cruce.agregar_accion(accion)
      for accion in sol2.acciones:
        if not accion in conflictos_eliminados:
          sol_cruce.agregar_accion(accion)
    return sol_cruce
  
  def mutar_solucion_agregar_accion(self, solucion, plantas, macetas):
    mutacion = Solucion()
    # TODO aca se rompe el encapsulamiento
    mutacion.acciones = solucion.acciones[:]
    for intento in range(50):
      planta = self.choice(plantas)
      maceta = self.choice(macetas)
      tamanio_maximo_planta = max(planta.crecimiento)
      if tamanio_maximo_planta * 2 > maceta.ancho or tamanio_maximo_planta * 2 > maceta.largo:
        continue
      x_pos = self.randint(tamanio_maximo_planta - 1, maceta.ancho - tamanio_maximo_planta)
      y_pos = self.randint(tamanio_maximo_planta - 1, maceta.largo - tamanio_maximo_planta)
      semana = self.choice(planta.semanas_validas)
      accion_nueva = Accion(planta, maceta, (x_pos, y_pos), semana)
      mutacion.agregar_accion(accion_nueva)
      if mutacion.es_solucion_factible():
        break
      mutacion.acciones = solucion.acciones[:]
    return mutacion
  
  def mutar_solucion_eliminar_accion(self, solucion):
    mutacion = Solucion()
    mutacion.acciones = solucion.acciones[:]
    mutacion.acciones.remove(self.choice(mutacion.acciones))
    return mutacion
  
  def crear_poblacion_aleatoria(self, plantas, macetas):
    for i in range(self.cantidad_pobladores):
      nueva_solucion = Solucion()
      for j in range(self.randint(1, 30)):
        nueva_solucion = self.mutar_solucion_agregar_accion(nueva_solucion, plantas, macetas)
      self.soluciones.append(nueva_solucion)

  def crear_poblacion_sembrada(self, plantas, macetas):
    for maceta in macetas:
      for planta in plantas:
        tamanio_maximo_planta = max(planta.crecimiento)
        if tamanio_maximo_planta * 2 > maceta.ancho or tamanio_maximo_planta * 2 > maceta.largo:
          continue
        for semana in planta.semanas_validas:
          nueva_solucion = Solucion()
          for x in range(tamanio_maximo_planta - 1, maceta.largo - tamanio_maximo_planta + 1, tamanio_maximo_planta * 2):
            for y in range(tamanio_maximo_planta - 1, maceta.largo - tamanio_maximo_planta + 1, tamanio_maximo_planta * 2):
              accion = Accion(planta, maceta, (x, y), semana)
              nueva_solucion.agregar_accion(accion)
          self.soluciones.append(nueva_solucion)
  
  def seleccionar_y_cruzar(self, funcion_fitness):
    soluciones_puntuadas = list(map(lambda x: (x, funcion_fitness.calcular_fitness_de_solucion(x)), self.soluciones))
    mejor_solucion, maximo_fitness = max(soluciones_puntuadas, key=lambda x: x[1])
    pasan_a_siguiente_generacion = list(map(lambda l: l[0], filter(lambda x: self.random(0,1) <= float(x[1]) / maximo_fitness, soluciones_puntuadas)))
    hijos = []
    while len(pasan_a_siguiente_generacion) + len(hijos) < self.cantidad_pobladores:
      padre1 = self.choice(pasan_a_siguiente_generacion)
      padre2 = self.choice(pasan_a_siguiente_generacion)
      hijos.append(self.cruzar_soluciones(padre1, padre2))
    return pasan_a_siguiente_generacion + hijos