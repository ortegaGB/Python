# 1015, Distance between two points
point1= input() .split(" ")
x1,y1= point1
point2= input().split(" ")
x2,y2= point2
Distance= ((float(x2) - float(x1))**2 + (float(y2) - float(y1))**2)**0.5
print("%0.4f" %Distance)