''' teachers and centers are lists of Teacher objects and ExamCenter objects respectively 
    class Teacher and class ExamCentre and defined in locatable.py 
    Both are subclass of Locatable class
    Link : https://github.com/aahnik/mapTeachersToCenters/blob/master/locatable.py  '''


def sort(locatables, focal_centre):
    # sorts the list of objects of type Locatable in ascending order of distance from a given focal_centre
    # by using Insertion Sort algorithm

    for i in range(1, len(locatables)):

        key = locatables[i]
        key_dist = key.get_distance(focal_centre)

        j = i - 1

        while j >= 0 and key_dist < locatables[j].get_distance(focal_centre):
            locatables[j+1] = locatables[j]
            j -= 1

        locatables[j+1] = key


def run_algorithm(teachers, centers):  # algorithm v2.0
    for center in centers:
        active_teachers = [t for t in teachers if t.allocated == False]

        sort(active_teachers, center)

        for teacher in active_teachers:
            if center.vacancy == 0:
                break
            teacher.allocated = True
            center.allocated_teachers.append(teacher)
            center.vacancy -= 1

# AAHNIK 2020
