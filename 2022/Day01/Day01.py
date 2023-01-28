print(*(lambda elves: (max(elves), sum(__import__('heapq').nlargest(3, elves))))(list(map(lambda elf: sum(map(int, elf.splitlines())), open('Day01.txt').read().split('\n\n')))), sep='\n')
