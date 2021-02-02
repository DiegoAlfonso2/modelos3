from model.solucion import Solucion
from model.planta import Planta
from model.maceta import Maceta
from model.accion import Accion

class TestSolucion():
  def test_solucion_vacia_factible(self):
    sol = Solucion()
    assert sol.es_solucion_factible()
  
  def test_solucion_unica_accion_factible(self):
    sol = Solucion()
    # Nombre de la especie, color RGBA, evolucion del tamanio
    lechuga = Planta('Lechuga', (0, 255, 0, 255), [2, 2, 4, 4, 6, 6])
    # Identificador de la maceta, ancho en cm, largo en cm
    jardinera = Maceta('Jardinera', 30, 60)
    # Planta, maceta, posicion (x,y), semana
    accion = Accion(lechuga, jardinera, (15, 15), 1)
    sol.agregar_accion(accion)
    assert sol.es_solucion_factible()