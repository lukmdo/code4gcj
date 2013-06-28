#!/usr/bin/python3
"""
https://code.google.com/codejam/contest/90101/dashboard#s=p1

python Bwatersheds.py < IN-FILE.in > OUT-FILE.out
python -u Bwatersheds.py < IN-FILE.in | tee OUT-FILE.out
"""
import string


def get_label_matrix(matrix):
    """top level function - get labels only"""
    linked_matrix = get_linked_matrix(matrix)
    labelled_matrix = get_labelled_matrix(linked_matrix)

    return [[c[2] for c in r] for r in labelled_matrix]


def get_labelled(labels, linked_matrix, i, j):
    if len(linked_matrix[i][j]) == 3:
        label = linked_matrix[i][j][2]
        return label, labels

    bain_path = [[i, j]]
    label = None
    link = linked_matrix[i][j][1]
    while link:
        linked = linked_matrix[link[0]][link[1]]
        if len(linked) == 3:
            label = linked[2]
            break
        bain_path.append(link)
        if not linked[1]:
            break
        link = linked[1]
    if not label:
        label = labels.pop(0)
    for i, j in bain_path:
        linked_matrix[i][j].append(label)

    return label, labels


def get_labelled_matrix(linked_matrix):
    labels = list(string.ascii_lowercase)

    for i, r in enumerate(linked_matrix):
        for j, c in enumerate(r):
            label, labels = get_labelled(labels, linked_matrix, i, j)

    return linked_matrix


def get_neighbor_cells(matrix, row, col, height, width):
    # [(val, row, col), ...]
    if row > 0:
        r, c = row - 1, col
        yield matrix[r][c], r, c
    if col > 0:
        r, c = row, col - 1
        yield matrix[r][c], r, c
    if col < width - 1:
        r, c = row, col + 1
        yield matrix[r][c], r, c
    if row < height - 1:
        r, c = row + 1, col
        yield matrix[r][c], r, c


def get_linked_matrix(matrix):
    H, W = (len(matrix), len(matrix[0]))

    m = [[[matrix[i][j], None] for j in range(W)] for i in range(H)]
    if H == 1 and W == 1:
        return m

    for i, r in enumerate(matrix):
        for j, c in enumerate(r):
            val, x, y = min(get_neighbor_cells(matrix, i, j, H, W))
            if val < c:
                m[i][j][1] = [x, y]

    return m


def solve(num_cases):
    for i in range(1, num_cases + 1):
        h, w = input().split(' ')
        matrix_in = [list(map(int, input().split(' '))) for i in range(int(h))]
        matrix_out = get_label_matrix(matrix_in)
        print('Case #{num}:'.format(num=i))
        for row in matrix_out:
            print(' '.join(row))


if __name__ == '__main__':
    num_cases = int(input())
    solve(num_cases)
