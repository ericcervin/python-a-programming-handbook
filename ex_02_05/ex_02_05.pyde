def setup():
    size(100,100)

def draw():
    background(204)
    x = mouseX
    y = mouseY
    line(x,y,x+20,y-40)
    line(x+10,y,x+30,y-40)
    line(x+20,y,x+40,y-40)
