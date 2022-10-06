student_marks = {
    'Krishna': {67, 68, 69},
    'Arjun': {70, 98, 63},
    'Malika': {52, 56, 60}
}

x = (student_marks.get('Malika'))

total_marks = 0
subjects = 0
for i in x:
    total_marks += i
    subjects += 1

print(subjects)
avg = total_marks / subjects
avg = "{:.2f}".format(avg)
print(avg)

