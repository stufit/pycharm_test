def celsius_to_fahrenheit(degree):
    return (9/5)*degree +32

degree = float(input("Input celsius data : "))
print("바뀐 온도의 결과값 : ", celsius_to_fahrenheit(degree))
