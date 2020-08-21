from math import sqrt
from heapq import heappush, heappop


# Helper functions
def measure_distance(begin, end):
    x = abs(begin[0] - end[0])
    y = abs(begin[1] - end[1])

    return sqrt(x * x + y * y)


def find_next_shortest_path(M, start, goal, minHeap, visited, prev):
    begin = M.intersections[start]
    end = M.intersections[goal]

    for road in M.roads[start]:
        roadd = M.intersections[road]
        g = visited[start] + measure_distance(begin, roadd)

        if road not in visited or g < visited[road]:
            h = measure_distance(roadd, end)
            f = g + h

            heappush(minHeap, (f, road))
            visited[road] = g
            prev[road] = start
    
    return heappop(minHeap)


def generate_path(prev, start, goal):
    current = goal
    path = [current]

    while current != start:
        current = prev[current]
        path.append(current)

    path.reverse()
    return path


# Main function
def shortest_path(M, start, goal):
    minHeap = list()
    prev = {start: None}
    visited = {start: 0}

    smallest = (0, start)

    while smallest[1] != goal:
        
        smallest = find_next_shortest_path(M, smallest[1], goal, minHeap, visited, prev)
        
    return generate_path(prev, start, goal)