from examSystem.exam import Exam

class ExamsArray :
    def __init__(self):
        self.exams = []

    def addExam(self, day, year, month, subject, examType):
        self.exams.append(Exam(day, month, year, subject, examType))

    def resetExams(self):
        for i in self.exams:
            self.exams.pop(0)

        print("testing reseting")
        for exam in self.exams:
            print(f'(readToken({exam.day}.{exam.month} = {exam.subject} -- {exam.examType}')
