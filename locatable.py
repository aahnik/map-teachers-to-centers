import my_io


class Locatable:
    def __init__(self, id):
        self.id = id
        self.x, self.y = my_io.get_unique_pos()


class Teacher(Locatable):
    def __init__(self, id):
        super(Teacher, self).__init__(id)
        self.allocated = False


class ExamCenter(Locatable):
    def __init__(self, id):
        super(ExamCenter, self).__init__(id)
        self.vacancy = my_io.randVACANCY()

    @classmethod
    def total_vacancy(cls, exam_centers):
        count = 0
        for exam_center in exam_centers:
            count += exam_center.vacancy
        return count
