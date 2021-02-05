import random
import model.constantes as constantes
from model.solucion import Solucion
from model.accion import Accion

class Poblacion():
  def __init__(self, semanas=constantes.SEMANAS, rand_function=random.uniform, choice_function=random.choice, randint_function=random.randint):
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
      semana = self.randint(0, self.semanas) + 1
      accion_nueva = Accion(planta, maceta, (x_pos, y_pos), semana)
      mutacion.agregar_accion(accion_nueva)
      if mutacion.es_solucion_factible():
        break
      mutacion.acciones = solucion.acciones[:]
    return mutacion
    
