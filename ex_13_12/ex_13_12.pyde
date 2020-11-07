def setup():
    global img
    size(100,100)
    img = loadImage("topanga.jpg")
   
    
def draw():
    image(img,0,0)
    v = mouseX / 100.0
    filter(THRESHOLD,v)
