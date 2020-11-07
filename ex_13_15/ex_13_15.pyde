
def setup():
    global img1,img2
    size(100,100);
    img1 = loadImage("forest.jpg")
    img2 = loadImage("forest.jpg")
    img2.filter(INVERT)
    
def draw():
  global img1,img2
  image(img1,0,0)
  image(img2,50,0)
