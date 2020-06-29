import io


class Locatable:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y


class Teacher(Locatable):
    def __init__(self, id, x, y, allocated=False):
        super(Teacher, self).__init__(id, x, y)
        self.allocated = allocated


class ExamCenter(Locatable):
    def __init__(self, id, x, y, vacancy=io.randVACANCY()):
        super(ExamCenter, self).__init__(id, x, y)
        self.vacancy = vacancy
