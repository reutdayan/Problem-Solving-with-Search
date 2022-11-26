import csv

from algorithms.a_star import a_star
from algorithms.ida_star import ida_star
from algorithms.ucs import ucs
from ways import load_map_from_csv


def write_to_txt(list, file_path):
    with open(file_path, 'w') as f:
        for line in list:
            f.write(line)
            f.write('\n')
    f.close()


def run_on_problems():
    with open("./problems.csv", 'r') as file:
        problems = csv.reader(file)
        roads = load_map_from_csv()
        answersUCS = []
        answersA_STAR = []
        for problem in problems:
            path, time = ucs(roads, int(problem[0]), int(problem[1]))
            answersUCS.append(' '.join(str(j) for j in path) + ' - ' + str(round(time, 4)))
            path, time, estimate_time = a_star(roads, int(problem[0]), int(problem[1]))
            answersA_STAR.append(
                ' '.join(str(j) for j in path) + ' - ' + str(round(time, 4)) + ' - ' + str(round(estimate_time, 4)))
        write_to_txt(answersUCS, "./results/UCSRuns.txt")
        write_to_txt(answersA_STAR, "./results/AStarRuns.txt")


if __name__ == "__main__":
    run_on_problems()
