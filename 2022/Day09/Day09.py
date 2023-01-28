lines = map(str.split, open('Day09.txt').read().splitlines())

no_knots = 10
knots = [[0, 0] for _ in range(no_knots)]
visited = {(0, 0)}
plus = {'D': (-1, 0), 'U': (+1, 0), 'L': (0, -1), 'R': (0, +1)}
sign = lambda x: (x > 0) - (x < 0)
for direct, quantity in lines:
    for _ in range(int(quantity)):
        knots[0] = [h+p for h, p in zip(knots[0], plus[direct])]
        for index in range(1, no_knots):
            if any(abs(pre-cur) > 1 for pre, cur in zip(*knots[index-1:index+1])):
                knots[index] = [cur+sign(pre-cur) for pre, cur in zip(*knots[index-1:index+1])]
        visited.add(tuple(knots[-1]))

print(len(visited))