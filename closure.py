def outerFunc():
    msg = 'Hello'

    def innerFunc():
        print(msg)

    return innerFunc

hi = outerFunc()
hi()
print("==================")
print(hi,type(hi))
print(outerFunc(),type(outerFunc()))
print('------------------------------')
hi()
#del outerFunc #outerFunc 제거
#print(outerFunc())
hi()
print('++++++++++++++++++++++++++')
print(hi.__name__)

print('************************')
print(outerFunc().__qualname__)
print(hi.__qualname__)

