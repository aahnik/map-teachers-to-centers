from locatable import Locatable, Teacher, ExamCenter   # AAHNIK 2020
from my_io import generateSaveAndPlot, plot_connections   # AAHNIK 2020
from my_algo import sort, connect   # AAHNIK 2020


def main():

    centers = generateSaveAndPlot(ExamCenter, 20, 'ExamCenters')
    # vacancy = ExamCenter.total_vacancy(centers)
    teachers = generateSaveAndPlot(Teacher, 1000, 'Teachers')
    # no of teachers must be greater than no of vacancies
    origin = Locatable(0)
    origin.x, origin.y = 50, 50

    sort(centers, origin)

    connect(teachers, centers)
    plot_connections(centers)


if __name__ == "__main__":
    main()
# AAHNIK 2020
