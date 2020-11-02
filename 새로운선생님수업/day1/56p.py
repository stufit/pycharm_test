from datetime import datetime as dt

thisyear = dt.today().year

year = int(input("태어난 년도를 입력하시오 : "))
age = (thisyear - year) + 1

if 17 <= age < 20:
    print("고등학생입니다.")
    print("나이는 %d살 입니다." % age)
elif 20 <= age < 27:
    print("대학생입니다.")
    print("나이는 %d살 입니다." % age)
else:
    print("학생이 아닙니다.")
    print("나이는 %d살 입니다." % age)
