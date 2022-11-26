'''
This file should be runnable to print map_statistics using 
$ python stats.py
'''
import collections
from collections import namedtuple
from ways import load_map_from_csv
from ways.info import ROAD_TYPES


def map_statistics(roads):
    '''return a dictionary containing the desired information
    You can edit this function as you wish'''
    Stat = namedtuple('Stat', ['max', 'min', 'avg'])
    return {
        'Number of junctions': len(roads.junctions()),
        'Number of links': sum([1 for l in roads.iterlinks()]),
        'Outgoing branching factor': Stat(max=max([len(j.links) for j in roads.junctions()]),
                                          min=min([len(j.links) for j in roads.junctions()]),
                                          avg=sum([len(j.links) for j in roads.junctions()]) / len(
                                              [len(j.links) for j in roads.junctions()])),
        'Link distance': Stat(max=max([l.distance for l in roads.iterlinks()]),
                              min=min([l.distance for l in roads.iterlinks()]),
                              avg=sum([l.distance for l in roads.iterlinks()]) / len(
                                  [l.distance for l in roads.iterlinks()])),
        # value should be a dictionary
        # mapping each road_info.TYPE to the no' of links of this type
        'Link type histogram': collections.Counter([ROAD_TYPES[l.highway_type] for l in roads.iterlinks()]),  # tip: use collections.Counter
    }


def print_stats():
    for k, v in map_statistics(load_map_from_csv()).items():
        print('{}: {}'.format(k, v))


if __name__ == '__main__':
    from sys import argv

    assert len(argv) == 1
    print_stats()
