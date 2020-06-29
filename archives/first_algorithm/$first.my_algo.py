''' teachers and centers are lists of Teacher objects and ExamCenter objects respectively 
    class Teacher and class ExamCentre and defined in locatable.py 
    Link : https://github.com/aahnik/mapTeachersToCenters/blob/master/locatable.py  '''


def algorithm(teachers, centers):  # algorithm v

    connections = {}  # dictionary: centers as keys and its corresponding list of appointed teachers as values

    for teacher in teachers:

        factors = []

        for center in centers:
            dist = teacher.get_distance(center)
            factor = center.vacancy / dist
            factors.append(factor)

        index = factors.index(max(factors))
        centers[index].vacancy -= 1

        if centers[index] not in connections:
            connections[centers[index]] = []
        connections[centers[index]].append(teacher)

    return connections

# AAHNIK 2020
