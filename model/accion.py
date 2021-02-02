class Accion():
  def __init__(self, planta, maceta, posicion, semana):
    if not maceta.puede_plantarse_planta_en_posicion(planta, posicion):
      raise ValueError()
    self.planta = planta
    self.maceta = maceta
    self.posicion = posicion
    self.semana = semana