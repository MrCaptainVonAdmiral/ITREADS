from ctypes import windll
import time, math
dc= windll.user32.GetDC(0)

def getpixel(x,y):
    return windll.gdi32.GetPixel(dc,x,y)

time.clock()
    
for i in xrange(30):
    for y in xrange(30):
        getpixel(10+i,10+y)
        
print(math.sqrt(((900/time.clock())/60)))
