w = 0
k = 0

def setup():
    size(200,400)

def draw():
    global k
    global w
    background(0,0,255)
    fill(255)
    ellipse(width / 1.5, w, 50, 50)
    fill(140,0,255)
    ellipse(width / 3.5, k, 50, 50)
    if w > height:
       w = 0 
    else:  
       w = map(second(), 0, 59, 0, height)
    if k > height:
       k = 0
    else:
       k = map(minute(), 0, 59, 0, height)
