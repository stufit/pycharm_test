import random
guess_number = random.randint(1,100)
print("숫자를 입력해주세요(1~100)")
user_number = int(input())

cnt = 0
while(user_number is not guess_number):
    if user_number > guess_number:
        print("숫자가 너무 큽니다")
    else:
        print("숫자가 너무 작습니다")
    user_number = int(input())
    cnt = cnt+1
else:
    #print(f'정답은 {guess_number}이고 {cnt} 번만에 맞추었네요!')
     print('정답은 {}이고, {} 번만에 맞추었네요!'.format(guess_number,cnt))



