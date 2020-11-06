num = 20;
dx = [i * 5 for i in range(num)]
dy = [(12 + (i * 6)) for i in range(num)]

def diagonals(x, y):
  line(x,y,x+20,y-40)
  line(x+10,y,x+30,y-40)
  line(x+20,y,x+40,y-40)

def setup():
    size(100,100)
    print(dx)
    print(dy)

def draw():
    background(204)
    for i in range(num):
      dx[i] += 1
      if dx[i] > 100:
        dx[i] = -100
      diagonals(dx[i],dy[i])
