import csv

from matplotlib import pyplot as plt

from algorithms.ida_star import ida_star
from ways import load_map_from_csv, draw


def save_ida_star_plot():
    with open("./problems.csv", 'r') as file:
        problems_csv = csv.reader(file)
        problems = list(problems_csv)
        roads = load_map_from_csv()
        for problem in problems[80:90]:
            path = ida_star(roads, int(problem[0]), int(problem[1]))
            print(path)
            draw.plot_path(roads, path)
            path_to_dir = './solutions_img/' + str(problem[0])+'-'+str(problem[1]) + '.png'
            plt.savefig(path_to_dir)


if __name__ == '__main__':
    save_ida_star_plot()
