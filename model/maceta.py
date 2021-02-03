class Maceta():
  def __init__(self, identificador, ancho, largo):
    self.identificador = identificador
    self.ancho = ancho
    self.largo = largo
  def puede_plantarse_planta_en_posicion(self, planta, posicion):
    x, y = posicion
    for tamanio in planta.crecimiento:
      borde_izq, borde_der, borde_sup, borde_inf = planta.bordes_en_posicion(posicion, tamanio)
      if borde_izq < 0 or borde_der > self.ancho or borde_sup < 0 or borde_inf > self.largo:
        return False
    return True
