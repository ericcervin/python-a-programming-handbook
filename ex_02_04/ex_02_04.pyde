x = 0
y = 55

def setup():
    size(100,100)

def draw():
    global x,y
    background(204)
    line(x,y,x+20,y-40)
    line(x+10,y,x+30,y-40)
    line(x+20,y,x+40,y-40)
    x = x + 1
    if (x > 100):
        x = - 40
