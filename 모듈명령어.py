import random   #내부 라이브러리(모듈)
print("# random 모듈")


#random() : 난수 구하는 함수-> 0.0<=x<1.0 사이의 float를 리턴한다.
print("random(): ",random.random())


#uniform(min,max) : 지정한 범위 사이의 float를 리턴한다.
print("uniform(10,20) : ", random.uniform(10,20))

#randomrange() : 지정한 범위 내의 int값을 리턴한다.
 #randomrange(max) : 0부터 max 사이의 값을 리턴한다.
 #randomrange(min,max) : min부터 max 사이의 값을 리턴한다.
print("randomrange(10) :", random.randrange(10,300))

#choice(list) : 리스트의 요소들을 랜덤하게 섞는다.
print("choice([1,2,3,4,5] :",random.choice([1,2,3,4,5]))

#shuffle(list) : 리스트의 요소들을 랜덤하게 섞는다.
print("shuffle([1,2,3,4,5]) : ",random.shuffle([1,2,3,4,5]))

#sample(list, i<=숫자) : 리스트의 요소 중에 k개를 추출한다.
print("sample([1,2,3,4,5,90],k=3) : ", random.sample([1,2,3,4,5,90],k=3))

rand=random.randrange(1,10)
print(rand)

for i in range(6):
    print(random.randrange(1,10), end = '\t')


print('\n','-----------------------------------------')

# 문제] lotto 프로그램 작성

#1~45 사이의 값만 출력
#6개의 값을 추출한다.(같은 수는 배제)



# 업다운 게임 만들기
# 1~100 사이의 난수 값 추출하고, 사용자로부터 입력 받기
import random

number = random.randint(1, 100)  # 랜덤한 숫자 생성
print(number)


