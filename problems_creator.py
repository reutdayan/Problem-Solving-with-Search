import csv
import random

from ways import load_map_from_csv


def create_problems():
    roads = load_map_from_csv()
    problems = create_vector_problems(roads)
    write_to_csv(problems)


def create_vector_problems(roads):
    """Create problems for the user to solve"""
    problems = []
    while len(problems) < 100:
        a = random.choice(roads.junctions())
        d = random.randint(30, 40)
        current = a
        for j in range(d):
            # change current to be one of current children.
            if len(current.links) == 0:
                break
            next_index = random.choice(current.links).target
            current = roads.junctions()[next_index]
        b = current
        if a == b:
            continue
        problems.append((a.index, b.index))
    return problems


def write_to_csv(problems, file_path='./problems.csv'):
    """Write the problems to a csv file"""
    # open the file in the write mode
    f = open(file_path, 'w', newline='')
    # create the csv writer
    writer = csv.writer(f)

    # write rows to the csv file
    for problem in problems:
        writer.writerow(problem)

    # close the file
    f.close()


if __name__ == "__main__":
    create_problems()
