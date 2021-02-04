from PIL import Image, ImageDraw

class GraficadorSoluciones():
  def __init__(self, macetas, paso=10, semanas=10, path='tests/testout/'):
    self.macetas = macetas
    self.paso = paso
    self.semanas = semanas
    self.path = path
    self.margen = 10
    self.escala = 10

  def graficar_solucion(self, solucion):
    for maceta in self.macetas:
      acciones_en_maceta = list(filter(lambda a : a.maceta == maceta, solucion.acciones))
      self.graficar_maceta(maceta, acciones_en_maceta, str(id(solucion)) + '_')

  def graficar_maceta(self, maceta, acciones_en_maceta, prefijo_archivo=''):
    for semana in range(self.semanas):
      self.graficar_maceta_en_semana(maceta, acciones_en_maceta, semana + 1, prefijo_archivo)

  def graficar_maceta_en_semana(self, maceta, acciones_en_maceta, semana, prefijo_archivo):
    canvas = (maceta.ancho * self.escala + 2 * self.margen, maceta.largo * self.escala + 2 * self.margen)
    image = Image.new('RGBA', canvas, (255, 255, 255, 255))
    drawing = ImageDraw.Draw(image)
    x1_maceta, y1_maceta = self.margen, self.margen
    x2_maceta, y2_maceta = x1_maceta + maceta.ancho * self.escala, y1_maceta + maceta.largo * self.escala
    self.dibujar_contorno_maceta(drawing, x1_maceta, y1_maceta, x2_maceta, y2_maceta)
    self.dibujar_grilla(drawing, x1_maceta, y1_maceta, x2_maceta, y2_maceta)
    for accion in acciones_en_maceta:
      self.dibujar_accion_en_semana(drawing, accion, semana)
    image.save(self.path + prefijo_archivo + maceta.identificador + '_sem' + str(semana) + '.png')

  def dibujar_contorno_maceta(self, drawing, x1, y1, x2, y2):
    drawing.rectangle([x1, y1, x2, y2], outline=(0, 0, 0, 255), width=3)

  def dibujar_grilla(self, drawing, x1, y1, x2, y2):
    for x in range(self.paso, x2 - x1, self.paso):
      drawing.line([(x1 + x, y1), (x1 + x, y2)], fill=(170, 170, 170, 255), width=1)
    for y in range(self.paso, y2 - y1, self.paso):
      drawing.line([(x1, y1 + y), (x2, y1 + y)], fill=(170, 170, 170, 255), width=1)

  def dibujar_accion_en_semana(self, drawing, accion, semana):
    if semana >= accion.semana and semana < accion.semana + len(accion.planta.crecimiento):
      tamanio = accion.planta.crecimiento[semana - accion.semana]
      borde_izq, borde_der, borde_sup, borde_inf = accion.planta.bordes_en_posicion(accion.posicion, tamanio)
      x1, x2, y1, y2 = self.adaptar_escala((borde_izq, borde_der + 1, borde_sup, borde_inf + 1))
      for i in range(borde_izq, borde_der + 1):
        for j in range(borde_sup, borde_inf + 1):
          self.pintar_celda(drawing, i, j, color=accion.planta.color)
      drawing.arc([x1, y1, x2, y2], 0, 360, fill=(0, 0, 0, 255), width=2)

  def adaptar_escala(self, bordes):
    return (borde * self.escala + self.margen for borde in bordes)

  def pintar_celda(self, drawing, row, column, color=(0,255,0,255)):
    x1, x2, y1, y2 = self.adaptar_escala((row, row + 1, column, column + 1))
    drawing.rectangle([(x1, y1), (x2, y2)], outline=(170, 170, 170, 255), fill=color, width=1)
