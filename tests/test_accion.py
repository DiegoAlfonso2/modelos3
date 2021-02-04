from model.accion import Accion
from model.maceta import Maceta
from model.planta import Planta

class TestAccion():
  maceta = Maceta('Maceta prueba', 30, 30)
  planta = Planta('Planta', (), [1, 1, 1, 1])
  planta2 = Planta('Planta', (), [3, 3, 3, 3])
  lechuga = Planta('Lechuga', (0, 255, 0, 255), [1, 1, 5, 5, 10])
  jardinera = Maceta('Jardinera', 60, 60)
  def test_crear_accion_valida_planta_tamanio_1_en_borde(self):
    Accion(self.planta, self.maceta, (0,0), 1)
    Accion(self.planta, self.maceta, (0,29), 1)
    Accion(self.planta, self.maceta, (29,0), 1)
    Accion(self.planta, self.maceta, (29,29), 1)
    Accion(self.planta2, self.maceta, (2,2), 1)
    Accion(self.planta2, self.maceta, (2,27), 1)
    Accion(self.planta2, self.maceta, (27,2), 1)
    Accion(self.planta2, self.maceta, (27,27), 1)
    assert True
  def test_crear_accion_invalida_por_planta_superpuesta_esq_sup_izq(self):
    """Valida que no se pueda plantar una planta en una maceta si en algun momento de su
    crecimiento se va a chocar con las paredes de la maceta"""
    # maceta = Maceta('Maceta prueba', 30, 30)
    planta = Planta('Planta', (), [5, 5, 5, 5])
    planta2 = Planta('Planta', (), [1, 1, 4, 4])
    try:
      accion = Accion(planta, self.maceta, (1,1), 1)
      assert False
    except ValueError as err:
      pass
    try:
      accion = Accion(planta2, self.maceta, (1,1), 1)
      assert False
    except ValueError as err:
      pass
  def test_se_superpone_con(self):
    accion2 = Accion(self.lechuga, self.jardinera, (20, 12), 2)
    accion4 = Accion(self.lechuga, self.jardinera, (20, 12), 5)
    assert accion4.se_superpone_con(accion2)