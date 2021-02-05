def inicializador_random(lista):
  generador_probabilidades = (prob for prob in lista)
  return lambda : next(generador_probabilidades)
