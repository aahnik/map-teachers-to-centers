from locatable import Teacher, ExamCenter
from my_io import generateSaveAndPlot, connect
from my_algo import algorithm


def main():
    centers = generateSaveAndPlot(ExamCenter, 20, 'ExamCenters')
    vacancy = ExamCenter.total_vacancy(centers)
    teachers = generateSaveAndPlot(Teacher, vacancy, 'Teachers')
    connections = algorithm(teachers, centers)
    connect(connections)


if __name__ == "__main__":
    main()
