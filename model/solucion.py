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