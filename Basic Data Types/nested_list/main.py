python_students = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        python_students.append(student)



i = 0
scores = []

for student in python_students:
    for score in student:
        if i == 1:
            scores.append(score)
        i += 1
    i = 0

score_second = [x for x in scores if x > min(scores)]

ss = min(score_second)

for student in python_students:
    if ss in student:
        print(student)