from examSystem.exam import Exam
from datetime import date

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

    def giveExamSchedule(self):
        days = ["Poniedziałek", "Wtorek", "Sroda", "Czwartek", "Piątek"]
        new = False
        json = "["
        for i in range(5):
            json += "\n\t\"" + days[i] + "\": {"
            for exam in self.exams:
                if int(i) == int(date(int(exam.year), int(exam.month), int(exam.day)).weekday()):
                    new = True
                    json += "\n\t\t \"" + exam.subject + "\": \"" + exam.examType + "\","
                    if i == 4:
                        json += '\n'
                elif new == True:
                    new = False
                    json += "\n"
            json += "\t},"
        json += "\n]"
        return json