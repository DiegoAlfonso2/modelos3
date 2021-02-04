from drawing.graficador_soluciones import GraficadorSoluciones
from model.accion import Accion
from model.maceta import Maceta
from model.planta import Planta
from model.solucion import Solucion

class TestGraficadorSoluciones():
  def test_graficar_acciones_en_maceta_vacia(self):
    maceta = Maceta('Jardinera', 30, 60)
    graficador = GraficadorSoluciones([maceta])
    graficador.graficar_maceta(maceta, [])
  
  def test_graficar_una_accion_en_maceta(self):
    maceta = Maceta('Jardinera2', 30, 60)
    graficador = GraficadorSoluciones([maceta])
    planta = Planta('Lechuga', (0, 255, 0, 255), [2, 2, 5, 5, 10, 10, 10])
    accion = Accion(planta, maceta, (20, 20), 2)
    graficador.graficar_maceta(maceta, [accion])

  def test_graficar_varias_acciones(self):
    maceta = Maceta('Jardinera3', 60, 60)
    graficador = GraficadorSoluciones([maceta])
    lechuga = Planta('Lechuga', (0, 255, 0, 128), [2, 2, 5, 5, 10, 10, 10])
    zanahoria = Planta('Zanahoria', (255, 128, 44, 128), [2, 2, 2, 2, 2, 2, 2, 2])
    repollo = Planta('Repollo', (216, 215, 159), [2, 3, 4, 5, 6, 6])
    accion = Accion(lechuga, maceta, (20, 20), 2)
    accion2 = Accion(zanahoria, maceta, (15, 15), 1)
    accion3 = Accion(repollo, maceta, (40, 50), 4)
    graficador.graficar_maceta(maceta, [accion, accion3, accion2])
    
