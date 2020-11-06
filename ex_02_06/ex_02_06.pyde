def setup():
    size(100,100)

def draw():
    background(204)
    diagonals(40,90)
    diagonals(60,62)
    diagonals(20,40)
    
def diagonals(x,y):    
    line(x,y,x+20,y-40)
    line(x+10,y,x+30,y-40)
    line(x+20,y,x+40,y-40)
