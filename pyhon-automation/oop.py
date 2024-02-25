class Students:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Course:
    def __init__(self, course_name, max_score):
        self.course_name = course_name
        self.max_score = max_score
        self.students = []

    def add_students(self, student):
        if student.score >= self.max_score:
            self.students.append(student)


s1 = Students("mohamed", 88)
s2 = Students("Khaled", 66)
s3 = Students("joe", 77)

c2 = Course("ethical_hacking", 90)
c2.add_students(s2)
c2.add_students(s1)
print(c2.students[1].score)
