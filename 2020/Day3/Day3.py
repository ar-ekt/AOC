print(*(lambda area: (lambda trees: (trees[1], trees[0]*trees[1]*trees[2]*trees[3]*trees[4]))(list(map(lambda slope: sum(area[row][row * slope[0] % len(area[0])] == "#" for row in range(0, len(area), slope[1])), ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))))))(open("Day3.txt").read().split("\n")), sep = "\n")
