#어떤 사람이 수강생 목록에 존재하는지 check하는 함수를 작성하라.
#목록에 존재하면 True, 존재하지 않으면 False를 반환한다.

#Students = ["김철수","홍길동",문재인",김정은","트럼프","성춘향"]

#출력예상
#print(check_list(students,"홍길동"))

Students = ["김철수","홍길동","문재인","김정은","트럼프","성춘향"]
name=input("이름을 입력하시오")

for person in Students:
    if person in name:
        print("True")
        break
    else:
        print("False")





