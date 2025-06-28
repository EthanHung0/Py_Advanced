from Classes import Student,Teacher,TeachingAssistant

s = Student(student_id="SV123", major="Computer Science", name="Nam", age=20)
print(s.introduce())

t = Teacher(teacher_id="GV456", subject="Mathematics", name="Cô Hương", age=35)
print(t.introduce())

ta = TeachingAssistant(name="An", age=22, student_id="SV456", major="Computer Science", subject="Programming 101")
print(ta.introduce())