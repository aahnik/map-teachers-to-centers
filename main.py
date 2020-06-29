from locatable import Teacher, ExamCenter
import my_io




exam_centers = my_io.generateSaveAndPlot(ExamCenter, 110, 'ExamCenters')
vacancy = ExamCenter.total_vacancy(exam_centers)
teachers = my_io.generateSaveAndPlot(Teacher, vacancy, 'Teachers')
