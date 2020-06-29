from locatable import Locatable


class ExamCenter(Locatable):
    def __init__(self, id, pos, vacancy):
        super(ExamCenter, self).__init__(id, pos)
        self.vacancy = vacancy
    def print_c(self):
        print(f"EXAM CENTER:{self.id}  location: {self.pos}")
