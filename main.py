from locatable import Teacher, ExamCenter   # AAHNIK 2020
from my_io import generateSaveAndPlot, connect   # AAHNIK 2020
from my_algo import algorithm   # AAHNIK 2020


def main():
    centers = generateSaveAndPlot(ExamCenter, 20, 'ExamCenters')
    vacancy = ExamCenter.total_vacancy(centers)
    teachers = generateSaveAndPlot(Teacher, vacancy, 'Teachers')
    connections = algorithm(teachers, centers)
    connect(connections)


if __name__ == "__main__":
    main()
# AAHNIK 2020
