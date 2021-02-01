from PIL import Image, ImageDraw

# size of image
canvas = (400, 300)

# scale ratio
scale = 1
thumb = canvas[0]/scale, canvas[1]/scale

# rectangles (width, height, left position, top position)
# frames = [(50, 50, 5, 5), (60, 60, 100, 50), (100, 100, 205, 120)]
frames = [(300, 250, 5, 5)]

# init canvas
rect = Image.new('RGBA', canvas, (255, 255, 255, 255))
draw_rect = ImageDraw.Draw(rect)

# draw rectangles
for frame in frames:
    x1, y1 = frame[2], frame[3]
    x2, y2 = frame[2] + frame[0], frame[3] + frame[1]
    paso = 25
    draw_rect.rectangle([x1, y1, x2, y2], outline=(0, 0, 0, 255), width=3)
    for x in range(paso, x2 - x1, paso):
      draw_rect.line([(x, y1), (x, y2)], fill=(170, 170, 170, 255), width=1)
    for y in range(paso, y2 - y1, paso):
      draw_rect.line([(x1, y), (x2, y)], fill=(170, 170, 170, 255), width=1)
    #draw_rect.rectangle([x1, y1, x2, y2], outline=(170, 170, 170, 255), width=3)



# make thumbnail
rect.thumbnail(thumb)

# save image
rect.save('rect.png')