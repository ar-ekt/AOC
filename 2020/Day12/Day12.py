print(*(lambda instrucs: ((lambda rec: lambda p1, p2, p3, p4, p5: rec(rec, p1, p2, p3, p4, p5))(lambda part1, instrucs, n, ind, coor, f: abs(coor[0]) + abs(coor[1]) if ind == n else part1(part1, instrucs, n, ind+1, *(lambda action, value: (coor, (f + (value // 90)*{"L": -1, "R": +1}[action]) % 4) if action in 'LR' else ((lambda cp: [coor[i] + value * cp[i] for i in (0, 1)])(((0, 1), (1, 0), (0, -1), (-1, 0))[f if action == "F" else "NESW".index(action)]), f))(*instrucs[ind])))(instrucs, len(instrucs), 0, [0, 0], 1),  (lambda rec: lambda p1, p2, p3, p4, p5: rec(rec, p1, p2, p3, p4, p5))(lambda part2, instrucs, n, ind, coor, wp: abs(coor[0]) + abs(coor[1]) if ind == n else (lambda action, value: part2(part2, instrucs, n, ind+1, *([coor[i] + value * wp[i] for i in (0, 1)], wp) if action == "F" else  (coor, [wp, [wp[1], -wp[0]], [-wp[0], -wp[1]], [-wp[1], wp[0]]][(value * {"R": 1, "L": -1}[action] // 90) % 4]) if action in 'LR' else (coor, (lambda wpp: [wp[i] + value * wpp[i] for i in (0, 1)])(((0, 1), (1, 0), (0, -1), (-1, 0))["NESW".index(action)]))))(*instrucs[ind]))(instrucs, len(instrucs), 0, [0, 0], [10, 1])))(list(map(lambda instruc: (instruc[0], int(instruc[1:])), open("Day12.txt").read().split("\n")))), sep = "\n")
