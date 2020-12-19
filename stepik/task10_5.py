def Lee(matrix, i_start, j_start, i_end, j_end):
    path = [[-1 if x == 0 else 0 for x in y] for y in matrix]
    if path[i_end][j_end] == -1 or path[i_start][j_start] == -1:
        print(-1)
        return

    if i_end == i_start and j_end == j_start:
        print(0)
        return

    path[i_start][j_start] = 1
    weight = 1

    for i in range(100):
        weight += 1
        for y in range(10):
            for x in range(10):
                if path[y][x] == (weight - 1):
                    if y > 0 and path[y-1][x] == 0:
                        path[y-1][x] = weight
                    if y < 9 and path[y+1][x] == 0:
                        path[y+1][x] = weight
                    if x > 0 and path[y][x-1] == 0:
                        path[y][x-1] = weight
                    if x < 9 and path[y][x+1] == 0:
                        path[y][x+1] = weight

                    if abs(y-i_end) + abs(x-j_end) == 1:
                        path[i_end][j_end] = weight
                        print(weight-1)
                        return
    print(-1)
