from locatable import Teacher, ExamCenter
import my_io


def main():
    centers = my_io.generateSaveAndPlot(ExamCenter, 20, 'ExamCenters')
    vacancy = ExamCenter.total_vacancy(centers)
    teachers = my_io.generateSaveAndPlot(Teacher, vacancy, 'Teachers')



if __name__ == "__main__":
    main()
