class1_students = ["김철수", "홍길동", "문재인", "김정은", "트럼프", "성춘향"]

class2_students = ["손흥민", "이강인", "권창훈", "정우영", "김진수", "김민재"]


def check_list(paramList, nameStr):
    result = False

    for item in paramList:

        if nameStr == item:
            result = True

    return result


print(check_list(class1_students, '홍길동'))

print(check_list(class2_students, '손흥민'))

print(check_list(class1_students, '박신웅'))

print(check_list(class2_students, '박신웅'))



