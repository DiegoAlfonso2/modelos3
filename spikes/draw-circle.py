import math
from PIL import Image, ImageDraw

# size of each grid cell 
PASO = 25

# size of image
canvas = (400, 300)

# scale ratio
scale = 1
thumb = canvas[0]/scale, canvas[1]/scale

# rectangles (width, height, left position, top position)
# frames = [(50, 50, 5, 5), (60, 60, 100, 50), (100, 100, 205, 120)]
frames = [(250, 250, 5, 5)]

# init canvas
circle = Image.new('RGBA', canvas, (255, 255, 255, 255))
draw_circle = ImageDraw.Draw(circle)

def fill_cell(draw, row, column, x1, y1, color=(0,255,0,255)):
  draw.rectangle([(x1 + PASO * row, y1 + PASO * column), (x1 + PASO * (row + 1), y1 + PASO * (column + 1))], fill=color)

def is_fully_contained_in_circle(radius, row, column):
  x1_cell, y1_cell = column * PASO, row * PASO
  x2_cell, y2_cell = x1_cell + PASO, y1_cell + PASO
  def excedes_radius(x, y):
    return math.sqrt((radius - x) ** 2 + (radius - y) ** 2) > radius
  if x1_cell < radius and y1_cell < radius and excedes_radius(x1_cell, y1_cell):
    return False
  if x1_cell < radius and y2_cell > radius and excedes_radius(x1_cell, y2_cell):
    return False
  if x2_cell > radius and y1_cell < radius and excedes_radius(x2_cell, y1_cell):
    return False
  if x2_cell > radius and y2_cell > radius and excedes_radius(x2_cell, y2_cell):
    return False
  return True

# draw circle inside rectangles
for frame in frames:
    x1, y1 = frame[2], frame[3]
    x2, y2 = frame[2] + frame[0], frame[3] + frame[1]
    draw_circle.arc([x1, y1, x2, y2], 0, 360, fill=(0, 0, 0, 255), width=3)
    radius = (x2 - x1) / 2.0
    for d in range(PASO, x2 - x1, PASO):
      theta = math.asin((radius - d)/ radius)
      delta = radius - math.cos(theta) * radius
      startline = delta
      endline = (x2 - x1) - delta
      draw_circle.line([(x1 + d, y1 + startline), (x1 + d, y1 + endline)], fill=(170, 170, 170, 255), width=1)
      draw_circle.line([(x1 + startline, y1 + d), (x1 + endline, y1 + d)], fill=(170, 170, 170, 255), width=1)
    for i in range(0, math.ceil((x2 - x1) / float(PASO))):
      for j in range(0, math.ceil((x2 - x1) / float(PASO))):
        if is_fully_contained_in_circle(radius, i, j):
          fill_cell(draw_circle, i, j, x1, y1, color=(255,0,0,255))
    fill_cell(draw_circle, 2, 2, x1, y1)

# make thumbnail
#circle.thumbnail(thumb)

# save image
#circle.save('circle.png')
circle.show()