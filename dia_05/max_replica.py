student_scores = [89, 90, 76, 60, 54, 99, 100, 50, 34, 86, 94]

print(max(student_scores))

high_score = 0

for score in student_scores:
    if score > high_score:
        high_score = score

print(high_score)