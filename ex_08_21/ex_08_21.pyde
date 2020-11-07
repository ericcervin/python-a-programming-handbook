background(255)
rectMode(CENTER)
for y in range(9,height,20):
    for x in range(9,width,20):
        for d in range(18,0,-4):
            rect(x,y,d,d)
