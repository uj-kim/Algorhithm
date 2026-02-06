def solution(park, routes):
    h, w = len(park), len(park[0])

    # 시작 위치
    x = y = 0
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                x, y = i, j

    dir_map = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}

    for m in routes:
        d, p = m.split()
        p = int(p)
        dx, dy = dir_map[d]

        nx, ny = x, y
        ok = True

        for _ in range(p):
            nx += dx
            ny += dy
            if not (0 <= nx < h and 0 <= ny < w) or park[nx][ny] == 'X':
                ok = False
                break

        if ok:
            x, y = nx, ny

    return [x, y]
