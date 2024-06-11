from collections import namedtuple
import math

point=namedtuple('point',['x','y'])
p1=point(1,2)
p2=point(4,6)

dist=math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
print("distance between point1 and point2:",dist) 