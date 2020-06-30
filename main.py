from locatable import Locatable, Teacher, ExamCenter   # AAHNIK 2020
from my_io import generateSaveAndPlot, connect   # AAHNIK 2020
from my_algo import sort, run_algorithm   # AAHNIK 2020


def main():

    centers = generateSaveAndPlot(ExamCenter, 20, 'ExamCenters')
    vacancy = ExamCenter.total_vacancy(centers)
    teachers = generateSaveAndPlot(Teacher, vacancy, 'Teachers')

    origin = Locatable(0)
    origin.x, origin.y = 50, 50

    sort(centers, origin)

    run_algorithm(teachers, centers)
    connect(centers)


if __name__ == "__main__":
    main()
# AAHNIK 2020
