noStroke()
for y in range(0,100,10):
  for x in range(0,100,10):
       fill((x + y) * 1.4)
       rect(x,y,10,10)
