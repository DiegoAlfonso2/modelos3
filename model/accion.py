class Accion():
  def __init__(self, planta, maceta, posicion, semana):
    if not maceta.puede_plantarse_planta_en_posicion(planta, posicion):
      raise ValueError()
    self.planta = planta
    self.maceta = maceta
    self.posicion = posicion
    self.semana = semana
  def __hash__(self):
    return hash(planta, maceta, posicion, semana)
  def __eq__(self, other):
    return (self.planta, self.maceta, self.posicion, self.semana) == (other.planta, other.maceta, other.posicion, other.semana)
  def __ne__(self, other):
    return not(self == other)
  def se_superpone_con(self, otra):
    if self.maceta != otra.maceta:
      return False
    for semana_desde_plantada, tamanio_planta in enumerate(self.planta.crecimiento):
      # Es "absoluta", relativa al inicio del anio, cuenta desde la semana 1
      semana_bajo_analisis = self.semana + semana_desde_plantada
      if semana_bajo_analisis < otra.semana or semana_bajo_analisis >= otra.semana + len(otra.planta.crecimiento):
        continue
      tamanio_otra = otra.planta.crecimiento[semana_bajo_analisis - otra.semana]
      x_planta, y_planta = self.posicion
      x_otra, y_otra = otra.posicion
      bordes_planta = self.planta.bordes_en_posicion((x_planta, y_planta), tamanio_planta)
      bordes_otra = otra.planta.bordes_en_posicion((x_otra, y_otra), tamanio_otra)
      if se_superponen_espacialmente(bordes_planta, bordes_otra):
        return True
    return False

def se_superponen_espacialmente(bordes, bordes_otra):
  borde_izq, borde_der, borde_sup, borde_inf = bordes
  otra_borde_izq, otra_borde_der, otra_borde_sup, otra_borde_inf = bordes_otra
  return se_superponen_en_eje_horizontal(bordes, bordes_otra) and se_superponen_en_eje_vertical(bordes, bordes_otra)

def se_superponen_en_eje_horizontal(bordes, bordes_otra):
  borde_izq, borde_der, borde_sup, borde_inf = bordes
  otra_borde_izq, otra_borde_der, otra_borde_sup, otra_borde_inf = bordes_otra
  return borde_izq <= otra_borde_der and borde_der >= otra_borde_der or \
          borde_der >= otra_borde_izq and borde_izq <= otra_borde_izq

def se_superponen_en_eje_vertical(bordes, bordes_otra):
  borde_izq, borde_der, borde_sup, borde_inf = bordes
  otra_borde_izq, otra_borde_der, otra_borde_sup, otra_borde_inf = bordes_otra
  return borde_sup <= otra_borde_inf and borde_inf >= otra_borde_inf or \
          borde_inf >= otra_borde_sup and borde_sup <= otra_borde_sup