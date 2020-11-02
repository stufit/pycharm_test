import numpy as np
points = np.array(([[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]])) #9행2열
p = np.array([2.5, 2])
import matplotlib.pyplot as plt
plt.plot(points[:,0], points[:,1], "ro") #[:,0] 전체에서 0열에 대한 데이터 추출
plt.plot(p[0], p[1], "bo")

x= np.arange(8)
y=10 +3*np.random.random(8)
plt.bar(x,y)
plt.show()

x=np.linspace(0,5,10)
print(x)
y=x**2
plt.plot(x,y)

plt.show()

