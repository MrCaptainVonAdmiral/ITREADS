import ImageGrab, ImageDraw, time, Image

#Bound box coords
y1, y2, x1, x2 = 605, 645, 50, 80

Row = y2 - y1
Col = x2 - x1

TL=[x1,y1]
BR=[x2,y2]
print TL, BR
color=list(list())
GS=list(list())
for k in xrange(Col):
    temp_list=list()
    for q in xrange(Row):
        temp_list.append(0)
    color.append(temp_list)
    GS.append(temp_list)

image = ImageGrab.grab()
for i in xrange(Col):
    Col_Read=i+x1
    #print Row_Read
    for j in xrange(Row):
        Row_Read=y1+j
        #print Col_Read
        color[i][j] = image.getpixel((Row_Read, Col_Read))
        #find the grey-scale value
        #GS[i][j] = .21*color[i][j][0]+.71*color[i][j][1]+.07*color[i][j][2]
        #GS[i][j] = (color[i][j][0] + color[i][j][1] + color[i][j][2])/2
        Temp = (color[i][j][0] + color[i][j][1] + color[i][j][2])/3
        if Temp < 200:
            GS[i][j]=1
        else:
            GS[i][j]=0
        #print GS[i][j]

#for i in GS:
#    print repr(i)
    
for i in xrange(Col):
    Hold=""
    for j in xrange(Row):
        Hold = Hold + str(GS[i][j])
    print Hold
time.sleep(2)