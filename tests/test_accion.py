from model.accion import Accion
from model.maceta import Maceta
from model.planta import Planta

class TestAccion():
  def test_crear_accion_valida_planta_tamanio_1_en_borde(self):
    maceta = Maceta('Maceta prueba', 30, 30)
    planta = Planta('Planta', (), [1, 1, 1, 1])
    planta2 = Planta('Planta', (), [3, 3, 3, 3])
    Accion(planta, maceta, (0,0), 1)
    Accion(planta, maceta, (0,29), 1)
    Accion(planta, maceta, (29,0), 1)
    Accion(planta, maceta, (29,29), 1)
    Accion(planta2, maceta, (2,2), 1)
    Accion(planta2, maceta, (2,27), 1)
    Accion(planta2, maceta, (27,2), 1)
    Accion(planta2, maceta, (27,27), 1)
    assert True
  def test_crear_accion_invalida_por_planta_superpuesta_esq_sup_izq(self):
    """Valida que no se pueda plantar una planta en una maceta si en algun momento de su
    crecimiento se va a chocar con las paredes de la maceta"""
    maceta = Maceta('Maceta prueba', 30, 30)
    planta = Planta('Planta', (), [5, 5, 5, 5])
    planta2 = Planta('Planta', (), [1, 1, 4, 4])
    try:
      accion = Accion(planta, maceta, (1,1), 1)
      assert False
    except ValueError as err:
      pass
    try:
      accion = Accion(planta2, maceta, (1,1), 1)
      assert False
    except ValueError as err:
      pass
    