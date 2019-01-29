import numpy as np
import matplotlib.pyplot as plt

def check(point, p1, p2):
    return (point[0] - p2[0]) * (p1[1] - p2[1]) - (p1[0] - p2[0]) * (point[1] - p2[1]) >= 0

def inTriangle(point, tri1, tri2, tri3):
    
    d1, d2, d3 = check(point, tri1, tri2), check(point, tri2, tri3), check(point, tri3, tri1)
    
    return (d1 and d2 and d3) or (not d1 and not d2 and not d3)

def inTri(point, tri):
    return inTriangle(point, tri[0], tri[1], tri[2])

def createGrid(width, height):
    return np.zeros((height, width))

def raster(buffer, triangle, AA=False):
    for x, rows in enumerate(buffer):
        for y, _ in enumerate(rows):
            i = len(buffer) - x - 1
            if not AA:
                buffer[i, y] = int(inTri((x+0.5, y+0.5), triangle))
            else:
                p = 1 / AA
                v = 0
                for j in range(AA):
                    for k in range(AA):
                        point = (x + p/2 + (j*p) , y + p/2 + (k*p))
                        v += int(inTri(point, triangle))
                buffer[i, y] = v / (AA*AA)
        

grid = createGrid(1024, 768)
tp1 = (10, 10)
tp2 = (800, 200)
tp3 = (300, 900)
tri = (tp1, tp2, tp3)

#raster(grid, tri)
size = 5
aa = createGrid(size*10, size*10)
ori = createGrid(size*10, size*10)
stp1 = (1*size, 1*size)
stp2 = (8*size, 2*size)
stp3 = (3*size, 9*size)
stri = (stp1, stp2, stp3)

raster(aa, stri, AA=2)
raster(ori, stri)

plt.imshow(aa, cmap='gray')
plt.show()
plt.imshow(ori, cmap='gray')
plt.show()