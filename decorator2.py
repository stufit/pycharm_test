import datetime as dt

def workTime(func):
    def decorated():
        print(dt.datetime.now())
        func()
        print(dt.datetime.now())
    return decorated()


@workTime
def mainFunc():
    print(dt.datetime.now())
    print('mainFunc function call~~')

@workTime
def mainFunc_1():
    print('mainFunc function_1 call~~')
    for i in range(1, 11):
        print(i, end= '  ')
        print()


@workTime
def mainFucn_2():
    print('mainFunc function_2 call~~')

