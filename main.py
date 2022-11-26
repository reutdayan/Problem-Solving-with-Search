'''
Parse input and run appropriate code.
Don't use this file for the actual work; only minimal code should be here.
We just parse input and call methods from other modules.
'''
from algorithms.a_star import a_star
from algorithms.ida_star import ida_star
from algorithms.ucs import ucs
from ways import load_map_from_csv

# do NOT import ways. This should be done from other files
# simply import your modules and call the appropriate functions

roads = load_map_from_csv()


def find_ucs_rout(source, target):
    return ucs(roads, source, target)


def find_astar_route(source, target):
    return a_star(roads, source, target)


def find_idastar_route(source, target):
    return ida_star(roads, source, target)


def dispatch(argv):
    from sys import argv
    source, target = int(argv[2]), int(argv[3])
    if argv[1] == 'ucs':
        path, time = find_ucs_rout(source, target)
    elif argv[1] == 'astar':
        path, time, estimate_time = find_astar_route(source, target)
    elif argv[1] == 'idastar':
        path = find_idastar_route(source, target)
    print(' '.join(str(j) for j in path))


if __name__ == '__main__':
    from sys import argv

    dispatch(argv)


'''
# 3 - create 100 random problems
from problems_creator import create_problems
create_problems()

# 5, 9- run algorithms on problems (ucs, a_star).
from run_algorithms import run_on_problems
run_on_problems()

# 12- draw plots
from run_draw_plots import save_ida_star_plot
save_ida_star_plot()

# 13- measure average running time oneach algorithm
from algorithms_running_time import average_running_time
average_running_time()
'''
