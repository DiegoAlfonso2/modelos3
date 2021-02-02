class Maceta():
  def __init__(self, identificador, ancho, largo):
    self.identificador = identificador
    self.ancho = ancho
    self.largo = largo
  def puede_plantarse_planta_en_posicion(self, planta, posicion):
    x, y = posicion
    for tamanio_semanal in planta.crecimiento:
      borde_izq = x - tamanio_semanal + 1
      borde_der = x + tamanio_semanal - 1
      borde_sup = y - tamanio_semanal + 1
      borde_inf = y + tamanio_semanal - 1
      if borde_izq < 0 or borde_der > self.ancho or borde_sup < 0 or borde_inf > self.largo:
        return False
    return True
