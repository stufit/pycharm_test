'''
try:
    num = int(input("정수 입력> "))
except:
    print("정수 입력 해달라고요~")
else:
    print("원의 반지름 : ",num)
    print('원의 둘레 : ',2*3.14*num)
    print('원의 넓이 : ',3.14*num*num)
print("프로그램 끝났어요")
'''

'''
try:
    num = int(input("정수 입력> "))

    print("원의 반지름 : ",num)
    print('원의 둘레 : ',2*3.14*num)
    print('원의 넓이 : ',3.14*num*num)
except Exception as err:
    print("exception : ",err)
    print('type(err) : ',type(err))
'''
'''
lst = [52,273,32,75,100]

try:
    num = int(input('intger data input'))
    print('{}번째 요소 : {}'.format(num,lst[num]))

except ValueError as err:
    print('ValueError 정수를 입력해줘~~')
    print('err : ',err)

except IndexError as err:
    print('IndexError 리스트의 인덱스를 벗어났어요')
    print('err : ',err)

except Exception as err:
    print("exception : ", err)
    print('type(err) : ', type(err))
    '''

def methodEx():
    print('methodEx 함수의 첫 줄 입니다.')

    try:
        print('try 구문이 실행되었습니다.')
        return #그냥 실행 또는 주석처리하고 실행해보고 결과 확인하기
        print('try 구문의 return 키워드 윗줄입니다.')
    except:
        print('except 구문이 실행되었습니다.')
    else:
        print('else 구문이 실행되었습니다.')
    finally:
        print('finally 구문이 실행되었습니다.')

    print('methodEx 함수의 마지막 줄 입니다.')

print(methodEx(),)





