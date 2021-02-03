class Planta():
  def __init__(self, nombre, color, crecimiento):
    self.nombre = nombre
    self.color = color
    self.crecimiento = crecimiento
  def bordes_en_posicion(self, posicion, tamanio_semanal):
    """Devuelve la coordenada de los bordes en una supuesta maceta. Recibe la posicion
    en la que se planto y el tamanio que tiene en ese momento
    """
    x, y = posicion
    borde_izq = x - tamanio_semanal + 1
    borde_der = x + tamanio_semanal - 1
    borde_sup = y - tamanio_semanal + 1
    borde_inf = y + tamanio_semanal - 1
    return (borde_izq, borde_der, borde_sup, borde_inf)