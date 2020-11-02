class EMP:
    def __init__(self,name,part,lev,tel):
        self.name = name
        self.part = part
        self.lev = lev
        self.tel = tel

    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name

    def setPart(self, part):
        self.part = part
    def getPart(self):
        return self.part

    def setLev(self, lev):
        self.lev = lev
    def getLev(self):
        return self.lev

    def setTel(self, tel):
        self.tel = tel
    def getTel(self):
        return self.tel

class Regular(EMP):
    # def __init__(self,pay):
    #      self.pay = pay

    def setPay(self,pay):
         self.pay= pay
    def getPay(self):
        return self.pay

class Sales(Regular):
    # def __init__(self,commision):
    #     self.commision = commision

    def setCommision(self,commision):
        self.commision
    def getCommision(self):
        return self.commision

    # def show(self):
    #     print("""name = {}
    #              part = {}
    #              lev  = {}
    #              tel  = {}
    #              pay  = {}
    #              commision = {}
    #              """.format(self.name,self.part,self.lev,self.tel,self.pay,self.commision))

    def show(self):
        print("dkdkdkd")


a = Sales('이관영','연구개발부', '사원','01086089516')
a.show()











