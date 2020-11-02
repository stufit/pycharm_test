kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]
index = 0;
for subject in midterm_score:
    # print(subject)
    for score in subject:
        student_score[index] += score
        index += 1
    # 과목이 바뀔때 학생(index)을 초기화
    index = 0

else:
    print(student_score)
    a, b, c, d, e = student_score
    student_avg = [int(a / 3), int(b / 3), int(c / 3), int(d / 3), int(e / 3)]
    print(student_avg)

# 내가한거
A = (midterm_score[0][0] + midterm_score[1][0] + midterm_score[1][0]) / 3
B = (midterm_score[0][1] + midterm_score[1][1] + midterm_score[1][1]) / 3
C = (midterm_score[0][2] + midterm_score[1][2] + midterm_score[1][2]) / 3
D = (midterm_score[0][3] + midterm_score[1][3] + midterm_score[1][3]) / 3
E = (midterm_score[0][4] + midterm_score[1][4] + midterm_score[1][4]) / 3
