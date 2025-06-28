from Classes import Student,Teacher,TeachingAssistant

s = Student("Nam", 20, "SV123", "Computer Science")
print(s.introduce())

t = Teacher("Cô Hương", 35, "GV456", "Mathematics")
print(t.introduce())

ta = TeachingAssistant("An", 22, "SV456", "Computer Science", "Programming 101")
print(ta.introduce())