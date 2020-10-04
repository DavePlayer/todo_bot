from exams import exam

class ExamsArray :
    def __init__(self):
        self.exams = []

    def addExam(self, day, month, subject, examType):
        self.exams.append(exam.Exam(day, month, subject, examType))
        print(self.exams)