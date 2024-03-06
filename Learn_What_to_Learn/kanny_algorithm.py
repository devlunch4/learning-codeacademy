# This is a Python Dictionary that contains all of the students in Kenny's class as well as their grades.
student_grades = {"Jeremy" : 87, "Kyla" : 82, "Ayesha" : 90, "Aleida" : 94, "Todd" : 79, "Maxwell" : 98, "Yolonda" : 81, "Kiyoko" : 71, "Dagmar" : 73, "Laura" : 91, "Shimeah" : 81, "Songqiao" : 92, "Frankie" : 87, "Natalia" : 95, "Gonzalo" : 82, "Pavel" : 78}

# This is a function that determines the student with the highest grade given a dictionary
def highest_grade(grades):
	top_of_class = list(grades.keys())[0]
	for student_a in grades:
		for student_b in grades:
			if (grades[student_a] > grades[student_b]) and (grades[student_a] > grades[top_of_class]):
				top_of_class = student_a
			elif (grades[student_b] > grades[student_a]) and (grades[student_b] > grades[top_of_class]):
				top_of_class = student_b
	return top_of_class

# This is a function that determines the student with the lowest grade given a dictionary
def lowest_grade(grades):
	bottom_of_class = list(grades.keys())[0]
	for student_a in grades:
		for student_b in grades:
			if (grades[student_a] < grades[student_b]) and (grades[student_a] < grades[bottom_of_class]):
				bottom_of_class = student_a
			elif (grades[student_b] < grades[student_a]) and (grades[student_b] < grades[bottom_of_class]):
				bottom_of_class = student_b
	return bottom_of_class

# This is Kenny's Algorithm! It sorts the students into pairs based on their grades.
def kennys_algorithm(grade_dict):
	student_pairs = []
	while len(grade_dict) > 0:
		student_pairs.append([highest_grade(grade_dict), lowest_grade(grade_dict)])
		grade_dict.pop(highest_grade(grade_dict))
		grade_dict.pop(lowest_grade(grade_dict))
	print(student_pairs)
  
# Paste the code below!
kennys_algorithm(student_grades)

print("English END")
print()
print("KOREAN START")
# KOREAN.
# 학생 이름과 성적을 딕셔너리에 저장
student_grades = {"제레미": 87, "카일라": 82, "아이샤": 90, "알레이다": 94, "토드": 79,
                "맥스웰": 98, "욜론다": 81, "키요코": 71, "다그마르": 73, "로라": 91,
                "시메아": 81, "송치아오": 92, "프랭키": 87, "나탈리아": 95, "곤잘로": 82, "파벨": 78}

# 딕셔너리에서 최고 성적을 가진 학생을 찾는 함수
def highest_grade(grades):
    top_student = list(grades.keys())[0]  # 처음 학생을 임시 최고 성적자로 설정
    for student_a in grades:
        for student_b in grades:
            # 현재 최고 성적보다 더 높은 학생이 있으면 갱신
            if grades[student_a] > grades[student_b] and grades[student_a] > grades[top_student]:
                top_student = student_a
            # 다른 학생이 더 높은 성적을 가졌을 때 비교
            elif grades[student_b] > grades[student_a] and grades[student_b] > grades[top_student]:
                top_student = student_b
    return top_student

# 딕셔너리에서 최저 성적을 가진 학생을 찾는 함수
def lowest_grade(grades):
    bottom_student = list(grades.keys())[0]  # 처음 학생을 임시 최저 성적자로 설정
    for student_a in grades:
        for student_b in grades:
            # 현재 최저 성적보다 더 낮은 학생이 있으면 갱신
            if grades[student_a] < grades[student_b] and grades[student_a] < grades[bottom_student]:
                bottom_student = student_a
            # 다른 학생이 더 낮은 성적을 가졌을 때 비교
            elif grades[student_b] < grades[student_a] and grades[student_b] < grades[bottom_student]:
                bottom_student = student_b
    return bottom_student

# 케니의 알고리즘: 학생들을 성적에 따라 짝짓음
def kennys_algorithm(grade_dict):
    student_pairs = []
    while len(grade_dict) > 0:
        # 최고/최저 성적 학생 쌍 추가
        student_pairs.append([highest_grade(grade_dict), lowest_grade(grade_dict)])
        # 딕셔너리에서 제거
        grade_dict.pop(highest_grade(grade_dict))
        grade_dict.pop(lowest_grade(grade_dict))
    print(student_pairs)  # 쌍 목록 출력

# 케니의 알고리즘 실행
kennys_algorithm(student_grades)
print("KOREAN END")
