# grid = list(map(lambda row: list(map(int, row)), open('Day08.txt').read().splitlines()))
# no_row = len(grid)
# no_col = len(grid[0])

# visible = set()
# [[1]*no_col for _ in range(no_row)]
# for row_index in range(no_row):
#     biggest = float('-inf')
#     for col_index in range(no_col):
#         if grid[row_index][col_index] > biggest:
#             biggest = grid[row_index][col_index]
#             visible.add((row_index, col_index))
    
#     biggest = float('-inf')
#     for col_index in range(no_col-1, -1, -1):
#         if grid[row_index][col_index] > biggest:
#             biggest = grid[row_index][col_index]
#             visible.add((row_index, col_index))

# for col_index in range(no_col):
#     biggest = float('-inf')
#     for row_index in range(no_row):
#         if grid[row_index][col_index] > biggest:
#             biggest = grid[row_index][col_index]
#             visible.add((row_index, col_index))

#     biggest = float('-inf')
#     for row_index in range(no_row-1, -1, -1):
#         if grid[row_index][col_index] > biggest:
#             biggest = grid[row_index][col_index]
#             visible.add((row_index, col_index))

# print(len(visible))

from collections import defaultdict
data = open('Day08.txt').read().strip()
lines = [x for x in data.split('\n')]

G = []
for line in lines:
    row = line
    G.append(row)

DIR = [(-1,0),(0,1),(1,0),(0,-1)]
R = len(G)
C = len(G[0])

p1 = 0
for r in range(R):
    for c in range(C):
        vis = False
        for (dr,dc) in DIR:
            rr = r
            cc = c
            ok = True
            while True:
                rr += dr
                cc += dc
                if not (0<=rr<R and 0<=cc<C):
                    break
                if G[rr][cc] >= G[r][c]:
                    ok = False
            if ok:
                vis = True
        if vis:
            p1 += 1
print(p1)

p2 = 0
for r in range(R):
    for c in range(C):
        score = 1
        for (dr,dc) in DIR:
            dist = 1
            rr = r+dr
            cc = c+dc
            while True:
                if not (0<=rr<R and 0<=cc<C):
                    dist -= 1
                    break
                if G[rr][cc]>=G[r][c]:
                    break
                dist += 1
                rr += dr
                cc += dc
            score *= dist
        p2 = max(p2, score)
print(p2)

