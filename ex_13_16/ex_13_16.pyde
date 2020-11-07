def setup():
    global img
    size(100,100)
    img = loadImage("airport.jpg")
    maskImg = loadImage("airportmask.jpg")
    img.mask(maskImg)

def draw():
    global img
    background(255)
    image(img,0,0)
