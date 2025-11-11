import sys
input = sys.stdin.readline

# 입력
sudoku = [list(map(int, input().split())) for _ in range(9)]

blank_pos = []
row_used = [set() for _ in range(9)]
col_used = [set() for _ in range(9)]
box_used = [set() for _ in range(9)]

def box_idx(r, c):
    return (r // 3) * 3 + (c // 3)

# 초기화
for r in range(9):
    for c in range(9):
        v = sudoku[r][c]
        if v == 0:
            blank_pos.append((r, c))
        else:
            row_used[r].add(v)
            col_used[c].add(v)
            box_used[box_idx(r, c)].add(v)

# 후보 계산
def candidates(r, c):
    used = row_used[r] | col_used[c] | box_used[box_idx(r, c)]
    return [v for v in range(1, 10) if v not in used]

def solve():
    # 빈칸이 없으면 완료
    if not blank_pos:
        print('\n'.join(' '.join(map(str, row)) for row in sudoku))
        return True

    # 후보가 가장 적은 칸 하나 선택
    best_i = -1
    best_cands = None
    min_len = 10
    for i, (r, c) in enumerate(blank_pos):
        cands = candidates(r, c)
        if not cands:                
            return False
        if len(cands) < min_len:
            min_len = len(cands)
            best_i = i
            best_cands = cands
            if min_len == 1:
                break

    # 선택한 칸 꺼내서 시도
    r, c = blank_pos.pop(best_i)
    b = box_idx(r, c)

    for v in sorted(best_cands):       
        sudoku[r][c] = v
        row_used[r].add(v)
        col_used[c].add(v)
        box_used[b].add(v)

        # 다음 단계 재귀
        if solve():
            return True

        # 되돌리기
        sudoku[r][c] = 0
        row_used[r].remove(v)
        col_used[c].remove(v)
        box_used[b].remove(v)

    # 이 칸 어떤 값도 안 되면 복구 후 실패
    blank_pos.insert(best_i, (r, c))
    return False

solve()
