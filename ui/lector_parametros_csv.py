import csv
from model.planta import Planta

def leer_parametros_plantas():
  with open('plantas.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    plantas = {}
    for row in reader:
      if(row):
        nombre, color, crecimiento, produccion_por_planta, precio_por_peso, semanas_validas_plantacion = row
        color = tuple([int(c) for c in color.split(',')])
        crecimiento = [int(c) for c in crecimiento.split(',')]
        produccion_por_planta = float(produccion_por_planta)
        precio_por_peso = float(precio_por_peso)
        if semanas_validas_plantacion:
          semanas_validas_plantacion = [int(sem) for sem in semanas_validas_plantacion.split(',')]
          planta = Planta(nombre, color, crecimiento, produccion_por_planta, precio_por_peso, semanas_validas_plantacion)
        else:
          planta = Planta(nombre, color, crecimiento, produccion_por_planta, precio_por_peso)
        plantas[planta.nombre] = planta
    return plantas

if __name__ == "__main__":
  leer_parametros_plantas()