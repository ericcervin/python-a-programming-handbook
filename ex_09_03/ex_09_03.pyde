gap = 20
thickness = 2

def setup():
  size(600,600)
  noFill()
  strokeWeight(thickness)
  stroke(0)

def draw():
   background(255)
   arcLength = mouseX / 95.0;
   for i in range(gap,width - gap,gap):
       angle = radians(i)
       arc(width/2, height/2, i,i,angle, angle + arcLength)
