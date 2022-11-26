import csv
import time

from algorithms.a_star import a_star
from algorithms.ida_star import ida_star
from algorithms.ucs import ucs
from ways import load_map_from_csv


def average_running_time():
    # open the file in the read mode
    with open("./problems.csv", 'r') as file:
        problems_csv = csv.reader(file)
        problems = list(problems_csv)
        roads = load_map_from_csv()
        # run the ucs algorithm on the problems and measure the time
        start = time.time()
        for problem in problems[20:30]:
            ucs(roads, int(problem[0]), int(problem[1]))
        end = time.time()
        avg_ucs = (end - start) / 10
        print("Average running time for UCS: ", avg_ucs)

        # run the a_star algorithm on the problems and measure the time
        start = time.time()
        for problem in problems[20:30]:
            a_star(roads, int(problem[0]), int(problem[1]))
        end = time.time()
        avg_a_star = (end - start) / 10
        print("Average running time for A star: ", avg_a_star)

        # run the ida_star algorithm on the problems and measure the time
        start = time.time()
        for problem in problems[20:30]:
            ida_star(roads, int(problem[0]), int(problem[1]))
        end = time.time()
        avg_ida_star = (end - start) / 10
        print("Average running time for idA star: ", avg_ida_star)


if __name__ == "__main__":
    average_running_time()
