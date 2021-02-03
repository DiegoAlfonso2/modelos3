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

  def test_solucion_dos_acciones_no_solapadas_espacio_al_mismo_tiempo_factible(self):
    """
      Semana 1
       ______
      |      |
      |  X   |
      |      |
      |    x |
      |______|
    """
    sol = Solucion()
    lechuga = Planta('Lechuga', (0, 255, 0, 255), [2, 2, 4, 4, 6, 6])
    zanahoria = Planta('Zanahoria', (0, 255, 0, 255), [2, 2, 2, 2, 2, 2])
    jardinera = Maceta('Jardinera', 30, 60)
    accion1 = Accion(lechuga, jardinera, (7, 7), 1)
    accion2 = Accion(zanahoria, jardinera, (20, 20), 1)
    sol.agregar_accion(accion1)
    sol.agregar_accion(accion2)
    assert sol.es_solucion_factible()

  def test_solucion_dos_acciones_alineadas_horizontalmente_no_se_solapan_factible(self):
    """
      Semana 1
       ______
      |      |
      |  x   |
      |      |
      |  x   |
      |______|
    """
    sol = Solucion()
    zanahoria = Planta('Zanahoria', (0, 255, 0, 255), [2, 2, 2, 2, 2, 2])
    jardinera = Maceta('Jardinera', 30, 60)
    accion1 = Accion(zanahoria, jardinera, (20, 10), 1)
    accion2 = Accion(zanahoria, jardinera, (20, 40), 1)
    sol.agregar_accion(accion1)
    sol.agregar_accion(accion2)
    assert sol.es_solucion_factible()

  def test_solucion_dos_acciones_coincidentes_espacio_al_mismo_tiempo_no_factible(self):
    sol = Solucion()
    lechuga = Planta('Lechuga', (0, 255, 0, 255), [2, 2, 4, 4, 6, 6])
    jardinera = Maceta('Jardinera', 30, 60)
    accion1 = Accion(lechuga, jardinera, (8, 8), 1)
    accion2 = Accion(lechuga, jardinera, (8, 8), 1)
    sol.agregar_accion(accion1)
    sol.agregar_accion(accion2)
    assert not sol.es_solucion_factible()

  def test_solucion_dos_acciones_solapadas_espacio_al_mismo_tiempo_no_factible(self):
    """
      Semana 1
       ______
      |      |
      | (Xx) |
      |      |
      |      |
      |______|
    """
    sol = Solucion()
    lechuga = Planta('Lechuga', (0, 255, 0, 255), [2, 2, 4, 4, 6, 6])
    zanahoria = Planta('Zanahoria', (0, 255, 0, 255), [2, 2, 2, 2, 2, 2])
    jardinera = Maceta('Jardinera', 30, 60)
    accion1 = Accion(lechuga, jardinera, (8, 8), 1)
    accion2 = Accion(zanahoria, jardinera, (8, 11), 1)
    sol.agregar_accion(accion1)
    sol.agregar_accion(accion2)
    assert not sol.es_solucion_factible()

  def test_solucion_dos_acciones_mismo_espacio_distinto_tiempo_factible(self):
    """
      Semana 1   Semana 2
       ______     ______ 
      |      |   |      |
      |  X   |   |  O   | 
      |      |   |      | 
      |      |   |      | 
      |______|   |______| 
    """    
    sol = Solucion()
    lechuga = Planta('Lechuga', (0, 255, 0, 255), [2, 4, 6])
    zanahoria = Planta('Zanahoria', (0, 255, 0, 255), [2, 2, 2])
    jardinera = Maceta('Jardinera', 30, 60)
    accion1 = Accion(lechuga, jardinera, (8, 8), 1)
    accion2 = Accion(zanahoria, jardinera, (8, 8), 4)
    sol.agregar_accion(accion1)
    sol.agregar_accion(accion2)
    assert sol.es_solucion_factible()

  def test_solucion_dos_acciones_se_solapan_en_un_momento_no_factible(self):
    sol = Solucion()
    lechuga = Planta('Lechuga', (0, 255, 0, 255), [2, 4, 10])
    jardinera = Maceta('Jardinera', 30, 60)
    accion1 = Accion(lechuga, jardinera, (18, 10), 1)
    accion2 = Accion(lechuga, jardinera, (14, 14), 2)
    sol.agregar_accion(accion1)
    sol.agregar_accion(accion2)
    assert not sol.es_solucion_factible()
  
  def test_solucion_dos_acciones_coexisten_sin_solaparse_factible(self):
    sol = Solucion()
    lechuga = Planta('Lechuga', (0, 255, 0, 255), [2, 2, 2, 2, 10])
    jardinera = Maceta('Jardinera', 60, 60)
    accion1 = Accion(lechuga, jardinera, (10, 10), 5)
    accion2 = Accion(lechuga, jardinera, (24, 24), 7)
    sol.agregar_accion(accion1)
    sol.agregar_accion(accion2)
    assert sol.es_solucion_factible()

  def test_solucion_dos_acciones_en_distintas_macetas_factible(self):
    sol = Solucion()
    lechuga = Planta('Lechuga', (0, 255, 0, 255), [2, 2, 2, 2, 10])
    jardinera1 = Maceta('Jardinera 1', 60, 60)
    jardinera2 = Maceta('Jardinera 2', 60, 60)
    accion1 = Accion(lechuga, jardinera1, (10, 10), 2)
    accion2 = Accion(lechuga, jardinera2, (10, 10), 3)
    sol.agregar_accion(accion1)
    sol.agregar_accion(accion2)
    assert sol.es_solucion_factible()
  
  def test_solucion_cuatro_acciones_dos_se_superponen_no_factible(self):
    sol = Solucion()
    zanahoria = Planta('Lechuga', (0, 255, 0, 255), [2, 2, 2, 2, 2])
    jardinera = Maceta('Jardinera 1', 60, 60)
    accion1 = Accion(zanahoria, jardinera, (10, 10), 2)
    accion2 = Accion(zanahoria, jardinera, (20, 20), 3)
    accion3 = Accion(zanahoria, jardinera, (30, 20), 2)
    accion4 = Accion(zanahoria, jardinera, (22, 20), 2)
    sol.agregar_accion(accion1)
    sol.agregar_accion(accion2)
    sol.agregar_accion(accion3)
    sol.agregar_accion(accion4)
    assert not sol.es_solucion_factible()
    