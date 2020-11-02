#과제3]

#각 과일의 재고는 다음과 같다.
#바나나 : 6 개
#사과 : 0 개
#오렌지: 32 개
#배 : 15 개

price={'banana':4000,'apple':2000,'orange':1500,'pear':3000}
stock={'banana':6,'apple':0,'orange':32,'pear':15}



print("banana", str(price['banana']) +'원', str(stock['banana']) + "개")
print("apple", str(price['apple']) +'원', str(stock['apple']) + "개")
print("orange", str(price['orange']) +'원', str(stock['orange']) + "개")
print("pear", str(price['pear'])+'원' , str(stock['pear']) + "개")
print("total money is : ",(int(price['banana']))*(int(stock['banana']))+(int(price['apple']))*(int(stock['apple']))
                           +(int(price['orange']))*(int(stock['orange']))+(int(price['pear']))*(int(stock['pear'])),"원")


print("---------------------------------------")
priceDict = {'바나나': 4000, '사과': 2000, '오렌지': 1500, '배': 3000}

stockDict = {'바나나': 6, '사과': 0, '오렌지': 32, '배': 15}

sum = 0

for key in priceDict:
    sum += (priceDict[key] * stockDict[key])

    print('price : {}'.format(priceDict[key]))

    print('stock : {}'.format(stockDict[key]))

print('The total money is {}'.format(sum))


