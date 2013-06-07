import ImageGrab

#Bound box coords
x1, x2, y1, y2 = 622, 636, 44, 59
Row = y2 - y1
Col = x2 - x1

TL=[x1,y1]
BR=[x2,y2]
print TL, BR
color=list(list())

for k in xrange(16):
    temp_list=list()
    for q in xrange(16):
        temp_list.append(0)
    color.append(temp_list)

image = ImageGrab.grab()
for i in xrange(Row):
    Row_Read=i+x1
    for j in xrange(Col):
        Col_Read=y1+j
        color[i][j] = image.getpixel((Row_Read, Col_Read))
        print color[i][j]
    
