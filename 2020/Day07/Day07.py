print(*(lambda bags: (sum((lambda rec: lambda par1, par2: rec(rec, par1, par2))(lambda part1, bags, bag: bag == "shiny gold" or any(1 for child in bags[bag] if part1(part1, bags, child)))(bags, bag) for bag in bags) - 1,  (lambda rec: lambda par1, par2: rec(rec, par1, par2))(lambda part2, bags, bag: sum(prop * (1 + part2(part2, bags, child)) for child, prop in bags[bag].items()))(bags, "shiny gold")))({k: v for k, v in [(lambda bag: [bag[0], {} if bag[1] == "no other" else {k: v for k, v in map(lambda inner_bag: [" ".join(inner_bag.split()[1:]), int(inner_bag.split()[0])], bag[1].split(" bag, "))}])(line.split(" bag contain ")) for line in ((open("Day7.txt").read()).replace("bags", "bag").replace(" bag.", "").split("\n"))]}), sep = "\n")