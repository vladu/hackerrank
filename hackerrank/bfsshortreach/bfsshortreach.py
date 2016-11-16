# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import collections


def _parse_query(input):
    node_count, edge_count = next(input)
    adjacency_list = list([] for _ in xrange(node_count))
    for _ in xrange(edge_count):
        left, right = next(input)
        adjacency_list[left - 1].append(right - 1)
        adjacency_list[right - 1].append(left - 1)
    return adjacency_list, next(input)[0] - 1


def generate_input(in_stream):
    for line in in_stream.readlines():
        yield list(int(n) for n in line.strip().split(' '))


def parse_input(in_stream):
    input = generate_input(in_stream)
    return list(_parse_query(input) for _ in xrange(next(input)[0]))


def perform_query(adjacency_list, start_node):
    distance = [-1] * len(adjacency_list)
    to_visit = collections.deque([(start_node, 0)])
    while len(to_visit) > 0:
        node, depth = to_visit.popleft()
        distance[node] = depth
        for adj in adjacency_list[node]:
            if distance[adj] < 0:
                t = (adj, depth + 1)
                to_visit.append(t)
    return distance


def format_output(distances):
    return ' '.join(str(d * 6 if d > 0 else d) for d in distances if d != 0)


def compute_short_reach(in_stream):
    input = parse_input(in_stream)
    for a, s in input:
        print(format_output(perform_query(a, s)))


def main(file_name=None):
    if file_name is None:
        compute_short_reach(sys.stdin)
    else:
        with open(file_name, 'r') as f:
            compute_short_reach(f)

    
if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else None)
