from locatable import Node, Teacher, ExamCenter   # AAHNIK 2020
from my_io import generateSaveAndPlot, plot_connections   # AAHNIK 2020
from my_algo import sort, connect   # AAHNIK 2020


def main(n):

    centers = generateSaveAndPlot(ExamCenter, 20, 'ExamCenters')
    vacancy = ExamCenter.total_vacancy(centers)
    count = int((vacancy*n)//1)  # no of teachers
    teachers = generateSaveAndPlot(Teacher, count, 'Teachers')
    # no of teachers must be greater than no of vacancies
    origin = Node(0)
    origin.x, origin.y = 50, 50

    sort(centers, origin)

    connect(teachers, centers)
    plot_connections(centers)


if __name__ == "__main__":
    main(4) # no of teachers is about 4 times the total vacancy of exam centers
# AAHNIK 2020
