from typing import Dict, Union


class Dir:
    def __init__(self, name: str, parent=None) -> None:
        self.parent: Union[None, Dir] = parent
        self.name: str = name
        self.childs: Dict[str, Dir] = {}
        self.files: Dict[str, int] = {}

    def add_child(self, name: str) -> 'Dir':
        child = Dir(name, self)
        self.childs[name] = child
        return child

    def add_fild(self, name: str, size: int) -> None:
        self.files[name] = size
    
    def total_size(self) -> int:
        global total_space_dirs_under_100000

        size = (
            sum(child.total_size() for child in self.childs.values())
            + sum(self.files.values())
        )

        if size <= 100000:
            total_space_dirs_under_100000 += size

        return size
    
    def find_smallest_to_delete(self):
        global min_dir_size, wanted_space

        size = (
            sum(child.find_smallest_to_delete() for child in self.childs.values())
            + sum(self.files.values())
        )

        if wanted_space <= size < min_dir_size:
            min_dir_size = size

        return size

        
lines = open('Day07.txt').read().splitlines()

root_dir = Dir('/')
current_dir = root_dir
for line in lines:
    prts = line.split()
    if prts[0] == '$':
        if prts[1] == 'ls':
            ...

        elif prts[2] == '/':
            current_dir = root_dir

        elif prts[2] == '..':
            current_dir = current_dir.parent

        else:
            if not prts[2] in current_dir.childs:
                current_dir = current_dir.add_child(prts[2])
            else:
                current_dir = current_dir.childs.get(prts[2])

    elif prts[0] == 'dir':
        current_dir.add_child(prts[1])

    else:
        current_dir.add_fild(prts[1], int(prts[0]))


total_space_dirs_under_100000 = 0
used_space = root_dir.total_size()
free_space = 70000000 - used_space
wanted_space = 30000000 - free_space
min_dir_size = float('+inf')
root_dir.find_smallest_to_delete()
print(min_dir_size)