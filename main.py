from locatable import Teacher, ExamCenter
import my_io
# set of all co-ordinates involved in the problem, used to prevent overlapping points
reference = set()

center_count = 30
vacancy_count = 0

exam_centers = []
teachers = []

for i in range(center_count):
    x, y = my_io.randPOS()
    vacancy = my_io.randVACANCY()
    exam_center = ExamCenter(i, x, y, vacancy)
    if my_io.is_unique(exam_center, reference):
        reference.add((exam_center.x, exam_center.y))
        exam_centers.append(exam_center)
        vacancy_count += exam_center.vacancy

for i in range(vacancy_count):
    x, y = my_io.randPOS()
    teacher = Teacher(i, x, y)
    if my_io.is_unique(teacher, reference):
        reference.add((teacher.x, teacher.y))
        teachers.append(teacher)

my_io.save_to_file('Teachers', teachers, 'teachers.txt')
my_io.save_to_file('ExamCenters', exam_centers, 'examcenters.txt')

my_io.plot_points(teachers, 'Teachers', '.')
my_io.plot_points(exam_centers, 'ExamCenters', '*')