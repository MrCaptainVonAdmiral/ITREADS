import ImageGrab

#Bound box coords
x1, x2, y1, y2 = 622, 636, 44, 59
Row = y1 - y2
Col = x2 - x1

TL=[x1,y1]
BR=[x2,y2]
print TL, BR

image = ImageGrab.grab()
for i in xrange(Row)
    for j in xrange(Col)
    color(i,j) = image.getpixel((i, j))
    print color(i,j)
    
