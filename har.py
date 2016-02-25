import numpy

def part_d(best, worst,y):
    a=[[1,best],[1,worst]]
    b=numpy.linalg.solve(a,[[1.5],[-0.426]])
    d=numpy.exp(-numpy.exp(-(b[0][0]+ b[1][0]*y)))
    #assert numpy.abs((numpy.dot(a1,x)-b)==0)
    return d
def d1(y):
    return part_d(10,55,y)
def d2(y):
    return part_d(0.95,0.1,y)
def d(y1,y2):
    return numpy.sqrt((d1(y1)**2)*(d2(y2)**2))

