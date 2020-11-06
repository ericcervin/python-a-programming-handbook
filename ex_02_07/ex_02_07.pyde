class Diagonals():    
    def __init__(self,xpos,ypos,s,t,g):
        self.x = xpos
        self.y = ypos
        self.speed = s
        self.thick = t
        self.gray = g

    def update(self):        
      strokeWeight(self.thick)
      stroke(self.gray)
      line(self.x,self.y,self.x+20,self.y-40)
      line(self.x+10,self.y,self.x+30,self.y-40)
      line(self.x+20,self.y,self.x+40,self.y-40)
      self.x += self.speed
      if (self.x > 100):
          self.x = -100

da = Diagonals(0,80,1,2,0)
db = Diagonals(0,55,2,6,255)          
        
def setup():
    size(100,100)
    
    
def draw():
    background(204)
    da.update()
    db.update()
