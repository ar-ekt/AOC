print(*(lambda program: map(lambda func: sum((lambda rec: lambda p1, p2, p3, p4, p5: rec(rec, p1, p2, p3, p4, p5))(lambda emulator, func, program, n, mask, ind: {} if ind == n else emulator(emulator, func, program, n, program[ind][1], ind+1) if "mask" in program[ind] else {**func(program[ind][1], program[ind][2], mask), **emulator(emulator, func, program, n, mask, ind+1)})(func, program, len(program), "", 0).values()), (lambda memory, value, mask: {memory: int((lambda mask, val: "".join((bitN if bitM == "X" else bitM for bitM, bitN in zip(mask, val))))(mask, f"{int(value):036b}"), 2)}, lambda memory, value, mask: {adrs: int(value) for adrs in (lambda mask, adrs: (lambda rec: lambda par1, par2: rec(rec, par1, par2))(lambda possible_adrs, adrs, ind: [''] if ind == -1 else [bit + left_bits for left_bits in possible_adrs(possible_adrs, adrs, ind-1) for bit in '01'] if adrs[ind] == 'X' else [adrs[ind] + left_bits for left_bits in possible_adrs(possible_adrs, adrs, ind-1)])("".join((bitN if bitM == "0" else bitM for bitM, bitN in zip(mask, adrs))), 35))(mask, f"{int(memory):036b}")})))([instruc.split() for instruc in open("Day14.txt").read().replace("= ", "").replace("[", " ").replace("]", "").split("\n")]), sep = "\n")
