import ImageGrab, ImageDraw, time, Image

#Bound box coords
x1, x2, y1, y2 = 622, 636, 44, 59
Row = y2 - y1
Col = x2 - x1

TL=[x1,y1]
BR=[x2,y2]
print TL, BR
color=list(list())
GS=list(list())
for k in xrange(Row):
    temp_list=list()
    for q in xrange(Col):
        temp_list.append(0)
    color.append(temp_list)
    GS.append(temp_list)

image = ImageGrab.grab()
for i in xrange(Row):
    Row_Read=i+x1
    for j in xrange(Col):
        Col_Read=y1+j
        color[i][j] = image.getpixel((Row_Read, Col_Read))
        #find the grey-scale value
        #GS[i][j] = .21*color[i][j][0]+.71*color[i][j][1]+.07*color[i][j][2]
        #GS[i][j] = (color[i][j][0] + color[i][j][1] + color[i][j][2])/2
        Temp = (color[i][j][0] + color[i][j][1] + color[i][j][2])/2
        if Temp < 100:
            GS[i][j]=1
        else:
            GS[i][j]=0
        #print GS[i][j]


        
for i in xrange(Row):
    Hold=""
    for j in xrange(Col):
        Hold = str(GS[i][j]) + Hold
    print Hold
time.sleep(2)