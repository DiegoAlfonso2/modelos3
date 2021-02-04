SEMANAS = 10

class Solucion():
  def __init__(self):
    self.acciones = []
  def es_solucion_factible(self):
    for ix, accion in enumerate(self.acciones[:-1]):
      for otra_accion in self.acciones[ix + 1:]:
        if accion.se_superpone_con(otra_accion):
          return False
    return True
  def agregar_accion(self, accion):
    self.acciones.append(accion)
  def determinar_interseccion_con(self, otra):
    interseccion = {}
    for accion in self.acciones:
      for otra_accion in otra.acciones:
        if accion.se_superpone_con(otra_accion):
          if accion not in interseccion:
            interseccion[accion] = []
          interseccion[accion].append(otra_accion)
    return interseccion