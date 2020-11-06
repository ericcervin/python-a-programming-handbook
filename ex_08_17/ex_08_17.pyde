fill(0)
noStroke()
for y in range(-10,101,10):
    for x in range(-40,101,10):
      ellipse(x + y/3.0, y + x/8.0, 4,7)
