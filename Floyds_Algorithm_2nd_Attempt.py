# This is my attempt to re-write the code from the PDF and to get it to work #

import sys
import itertools

NO_PATH = sys.maxsize
graph = [[1,7,NO_PATH,8],[NO_PATH,0,5,NO_PATH],[NO_PATH,NO_PATH,NO_PATH,0]]
MAX_LENGTH = len(graph[0])



def floyd(distance):
    for intermediate, start_node,end_node\
        in itertools.product\
                (range(MAX_LENGTH),range(MAX_LENGTH),range(MAX_LENGTH)):
        if start_node == end_node:
            distance[start_node][end_node]=0
            continue
            distance[start_node][end_node] = min(distance[start_node][end_node],distance[start_node][intermediate]+distance[intermediate][end_node])
            print(distance)




