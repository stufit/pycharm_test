class Point:
    def __init__(self,x,y):
        self.x=0
        self.y=0


    def selfX(self,x):
        self.x=x

    def getX(self):
        return self.x


    def selfY(self,y):
        self.y=y

    def getY(self):
        return self.y


    def show(self):
        print(self.x,self.y)

#pt=Point(100,50)
#pt.show()

class circle(Point):
    r = 0
    def setR(self,r):
        self.r= r

    def getR(self):
        return self.r

    def show(self):
        print('x =',self.x,'y =',self.y,'r =',self.r)


class Rect(Point):
    x2 = y2 = 0
    def selfX2(self,x2):
        self.x2 = x2
    def getX2(self):
        return self.x2
    def selfY2(self,y2):
        self.y2 = y2
    def getY2(self):
        return self.y2
    def show(self):
        print('x2 =',self.x2,'y2 =',self.y2)