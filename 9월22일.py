class Persion:
    def __init__(self):  #self 다른 이름으로 지정해도 된다.
        self.name= '관영'
        self.age= 30


    def show(self):
        print(self.name+'님은 운동합니다.')


    def setName(self,name):
        self.name=name

    def setAge(self,age):
        self.age=age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def output(self ):
        print(self.name,".",self.age)


p1=Persion()  #객채생성, 메모리에할당, 자동생성자함수 호출
p1.setName('rhksdud')
print(p1.getName())


