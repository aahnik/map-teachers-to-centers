import my_io   # AAHNIK 2020
import math


class Locatable:
    def __init__(self, id):
        self.id = id
        self.x, self.y = my_io.get_unique_pos()

    def get_distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return(math.sqrt((dx**2)+(dy**2)))


class Teacher(Locatable):
    def __init__(self, id):
        super(Teacher, self).__init__(id)
        self.allocated = False


class ExamCenter(Locatable):
    def __init__(self, id):
        super(ExamCenter, self).__init__(id)
        self.vacancy = my_io.randVACANCY()
        self.allocated_teachers = []

    @classmethod
    def total_vacancy(cls, exam_centers):
        count = 0
        for exam_center in exam_centers:
            count += exam_center.vacancy
        return count

    def plot_connect_with_teachers(self, plt, color):
        plt.scatter(self.x, self.y, marker='s', color='red')
        for t in self.allocated_teachers:
            plt.scatter(t.x, t.y, marker='.', color=color)
            plt.arrow(self.x, self.y, t.x - self.x, t.y - self.y, color=color)


# AAHNIK 2020
