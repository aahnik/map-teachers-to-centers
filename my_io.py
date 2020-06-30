import os
import random as r
import itertools
import matplotlib.pyplot as plt

# set of all co-ordinates involved in the problem, used to prevent overlapping points
reference = set()

colors = itertools.cycle(['red', 'green', 'orange', 'purple',
                          'black', 'blue', 'pink', 'grey', 'yellow', 'cyan'])


# all functions are crafted for use only in context of this program , not for generic use


def randPOS(): return r.randint(1000, 9999) / 100, r.randint(1000, 9999) / 100


def randVACANCY(): return r.randint(3, 12)


def is_unique(points, reference):
    return True if points not in reference else False


def get_unique_pos():
    global reference
    points = randPOS()
    if is_unique(points, reference):
        reference.add(points)
        return points[0], points[1]
    else:
        return get_unique_pos()


def plot_points(locatables, title, m='.'):
    for l in locatables:
        plt.scatter(l.x, l.y, marker=m)
    plt.title(title)
    plt.savefig(f'{os.getcwd()}/data/{title}.png',
                dpi=150, bbox_inches='tight')
    plt.show()


# connections is a dictionary where key is exam center and value is list of teachers
def plot_connections(centers):
    for center in centers:
        color = next(colors)
        center.connect_with_teachers(plt, color)
    plt.savefig(f'{os.getcwd()}/data/connections.png',
                dpi=150, bbox_inches='tight')
    plt.show()


def save_to_file(title, locatables, file):
    with open(file, 'w+') as f:
        f.write(f'{title}\n')
        for l in locatables:
            if title == 'Teachers':
                f.write(f"id={l.id}\t|\tx={l.x}\t|\ty={l.y}\n")
            if title == 'ExamCenters':
                f.write(
                    f"id={l.id}\t|\tx={l.x}\t|\ty={l.y}\t|\tvacancy={l.vacancy}\n")


def generateSaveAndPlot(Locatable, count, title):
    locatable_objects = []
    for i in range(count):
        obj = Locatable(i)
        locatable_objects.append(obj)
    file = f'{os.getcwd()}/data/{title}.txt'
    save_to_file(title, locatable_objects, file)
    plot_points(locatable_objects, title)
    return locatable_objects


# AAHNIK 2020
