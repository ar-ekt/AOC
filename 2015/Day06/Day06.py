print(*(lambda instrucs: map(lambda ch_func: (lambda rec: lambda par1, par2, par3: rec(rec, par1, par2, par3))(lambda part2, n, ind, lamps: sum(sum(row) for row in lamps) if ind == n else (lambda instruc: part2(part2, n, ind+1, lamps[:instruc[1]] + [row[:instruc[2]] + [ch_func(lamp, instruc[0]) for lamp in row[instruc[2]: instruc[4]+1]] + row[instruc[4]+1:] for row in lamps[instruc[1]: instruc[3]+1]] + lamps[instruc[3]+1:]))(instrucs[ind]))(len(instrucs), 0, [[0]*1000 for _ in range(1000)]), (lambda lamp, inst: {"on": 1, "off": 0, "toggle": 1-lamp}[inst], lambda lamp, inst: max(lamp + {"on": 1, "off": -1, "toggle": 2}[inst], 0))))(list(map(lambda instruc: (lambda instruc: (instruc[0], *list(map(int, instruc[1:]))))(instruc.split()), open("Day06.txt").read().replace(",", " ").replace("turn ", "").replace("through ", "").split("\n")))), sep = "\n")