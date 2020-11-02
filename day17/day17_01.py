import numpy as np

# x= np.array([1,3,5])
# print(x.mean())  #해당 배열에 있는 평균값

# a = np.array(([1,2,3], [2,3,4])) #2행3열
# print(a)
#
# x= np.array([1,3,5,7,9,11]).reshape(3,2)  #원하는 행렬로 데이터 추
# print(x)

x= np.array(([1,3,5],[2,4,6]))
print(x[1])
print(x[1].mean())
print(x.mean())
print(x.shape)  #2행 3열

print('----------------------')

list1= [[1,11],[2,12],[3,13]]  #3행2열
np_ary = np.array(list1)
print(np_ary[:,1]) # 전체 행열에서 1열의 값만 추출한다.


list2= [[1,11,111],[2,12,121],[3,13,131]]  #3행3열
np_ary = np.array(list2)
print(np_ary[:,2]) # 전체 행열에서 2열의 값만 추출한다.

import math
print(math.sqrt(16))  #근의제곱

a=np.arange(15)  #0부터 14까
print(a)

a=np.arange(15).reshape(5,3)
print(a)

zero_vector = np.zeros(15) #zeros()  0으로 채운다
print(zero_vector)

zero_matrix = np.zeros((4,3)) #2차원 행렬로 만들어서 데이터값은 0으로 채운다.
print(zero_matrix)

my_array = np.zeros(15).reshape(3,5)
my_array +=4
print(my_array)

ary = np.array(([1,2],[3,4]))
print(ary.transpose())

print('---------------------')
x=np.array([1,2,3])
y=np.array([4,5,6])
z=x*y
print(z)  #각 열끼리 연산이 된다.

s= np.array([1,2,3])
t = s+1  #각 열마다 1을 더한
print(t)

print('****************')
X = np.array(([1,2,3],[4,5,6],[7,8,9]))
print(X[1])
print(X[:,1])

print('-----------------')

X =np.array(([1,2,3],[4,5,6],[7,8,9]))
Y = np.array(([2,3,4],[5,6,7],[8,9,10]))
print(X[:,1]+Y[:,1])

print('&&&&&&&&&&&&&&&&&&&&&')
#문제1) X의 데이터에서 2행의 데이터 추출해서 평균값 구하기기
X =np.array(([1,2,3],[4,5,6],[7,8,9]))
Y = np.array(([2,3,4],[5,6,7],[8,9,10]))
print(X[1].mean())

print('------------------------')
#문제2) Y의 데이터에서 1행의 데이터 추출해서 원소 개수 구하기
X =np.array(([1,2,3],[4,5,6],[7,8,9]))
Y = np.array(([2,3,4],[5,6,7],[8,9,10]))
print(Y[0].size)

print('+++++++++++++++++++++++++++')
#문제3) X,Y의 데이터에서 2행의 데이터 추출해서 곱한 결과 출력하기
X =np.array(([1,2,3],[4,5,6],[7,8,9]))
Y = np.array(([2,3,4],[5,6,7],[8,9,10]))
print(X[1]*Y[1])


print('%%%%%%%%%%%%%%%%%%%%')

a= np.array([10,20,30,40,50])
i= [1,3,4]
print(a[i])

print('+++++++++++++++++++++++++++')
a =np.array([10,20,30,40,50,60,70])
b = a>50
print(b)

print('------------------------')

ary = np.random.random(5)
print(ary)
print(np.all(ary>=0.3))   #ary중 모든 수가 0.3 이상 되야한다.
print(np.any(ary>0.7))    #ary중 아무거나 하나만 0.7 이상 되야한다.

print('&&&&&&&&&&&&&&&&&&&&&')

np.linspace(0,12,4)  #0부터 시작해서 12까지 중에서 4칸간격을 띄운다.
print(np.linspace(0,12,4))
print('------------------------')

np.logspace(np.log10(10),np.log10(100),5)
print(np.logspace(np.log10(10),np.log10(100),5))

print('~~~~~~~~~~~~~~~~~~~~~')

a= np.array([1,2,3,'aaa'])
print(a)
print(type(a[0]))



