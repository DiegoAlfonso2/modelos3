import ui.lector_parametros_csv as param
import ui.lector_request_json as request_parser
from drawing.graficador_soluciones import GraficadorSoluciones
from model.funcion_fitness import FuncionFitness, penalizacion_porcentaje_planta
from model.maceta import Maceta
import model.constantes as constantes
from model.algoritmo import Algoritmo

if __name__ == "__main__":
  plantas_dict = param.leer_parametros_plantas()
  request = request_parser.leer_request('request.json')
  plantas = []
  macetas = []
  funcion_fitness = FuncionFitness()
  for cultivo in request['cultivos']:
    nombre_planta = cultivo['planta']
    if not nombre_planta in plantas_dict:
      raise ValueError
    planta = plantas_dict[nombre_planta]
    plantas.append(planta)
    if 'porcentaje_minimo' in cultivo and 'penalizacion_porcentaje_minimo' in cultivo:
      funcion_fitness.agregar_penalizacion(penalizacion_porcentaje_planta(
        planta, float(cultivo['porcentaje_minimo']), float(cultivo['penalizacion_porcentaje_minimo']), lambda a,b: a >= b
      ))
    if 'porcentaje_maximo' in cultivo and 'penalizacion_porcentaje_maximo' in cultivo:
      funcion_fitness.agregar_penalizacion(penalizacion_porcentaje_planta(
        planta, float(cultivo['porcentaje_maximo']), float(cultivo['penalizacion_porcentaje_maximo']), lambda a,b: a <= b
      ))
  for maceta in request['macetas']:
    macetas.append(Maceta(maceta['identificador'], int(maceta['ancho']), int(maceta['largo'])))
  algoritmo = Algoritmo(constantes.CANT_ITERACIONES, funcion_fitness)
  solucion, valor = algoritmo.obtener_solucion_optima(plantas, macetas)
  print('El fitness de la mejor solucion obtenida es', valor)
  acciones = sorted(solucion.acciones, key=lambda accion: accion.semana)
  semana_anterior = 0
  for accion in acciones:
    if accion.semana > semana_anterior:
      print('Semana ', accion.semana)
      semana_anterior = accion.semana
    print('Plantar {} en {}, a {} cms hacia la derecha y {} cms hacia abajo del borde superior izquierdo'.format(accion.planta.nombre, accion.maceta.identificador, accion.posicion[0], accion.posicion[1]))
  graficador = GraficadorSoluciones(macetas, path='salida/')
  graficador.graficar_solucion(solucion)
