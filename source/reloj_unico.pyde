first = 0
secon = 500
def setup():
    size(100,500)
def draw():
    background(10,100,100)
    fill(10,240,10)
    ellipse(width / 2, secon, 60, 60)
    fill(240,10,10)
    ellipse(width / 2, first, 40, 40)
    if first > height:
       first = 0 
    else:  
       first = map(second(), 0, 59, 0, height)
    if secon > height:
       secon = 500
    else:
       secon = map(minute(), 0, 59, 0, height)
    global first
    global secon
