def algorithm(teachers, centers):
    connections = {}
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
