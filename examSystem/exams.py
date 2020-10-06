from examSystem.exam import Exam
from datetime import date

class ExamsArray :
    def __init__(self):
        self.exams = []

    def addExam(self, day, year, month, subject, examType):
        self.exams.append(Exam(day, year, month, subject, examType))

    def resetExams(self):
        for i in self.exams:
            self.exams.pop(0)

        for exam in self.exams:
            print(f'(readToken({exam.day}.{exam.month} = {exam.subject} -- {exam.examType}')

    def giveExamSchedule(self):
        days = ["Poniedziałek", "Wtorek", "Sroda", "Czwartek", "Piątek"]
        new = True
        json = "["
        for i in range(5):
            json += "\n\t\"" + days[i] + "\": {"
            for exam in self.exams:
                if int(i) == int(date(int(exam.year), int(exam.month), int(exam.day)).weekday()):
                    new = True
                    json += "\n\t\t \"" + exam.day + "." + exam.month + " - " + exam.subject + "\": \"" + exam.examType + "\","
                    if self.exams[-1] == exam:
                        json += '\n'
                elif new == True:
                    new = False
                    json += "\n"
            json += "\t},"
        json += "\n]"
        return json

    def removeExam(self, day, month , subject):
        for exam in self.exams:
            if exam.day == day and exam.month == month and exam.subject == subject:
                print(exam.subject)
                self.exams.remove(exam)
                return True
        print('brak danego rekordu')
        return False