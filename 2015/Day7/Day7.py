print(*(lambda func, gates: (lambda b: (b, func({k: [-1, [str(b)] if k == "b" else v[1]] for k, v in gates.items()}, "a")))(func(gates, "a")))(lambda gates, letter: (lambda rec: lambda par1, par2: rec(rec, par1, par2))(lambda part1, gates, wire: int(wire) if wire.isdigit() else gates[wire][0] if gates[wire][0] != -1 else (lambda gates, wire, result: (result, exec("gates[wire][0] = result")))(gates, wire, (lambda inp: 65535 - part1(part1, gates, inp[1]) if "NOT" in inp else part1(part1, gates, inp[0]) & part1(part1, gates, inp[2]) if "AND" in inp else part1(part1, gates, inp[0]) | part1(part1, gates, inp[2]) if "OR" in inp else part1(part1, gates, inp[0]) << part1(part1, gates, inp[2]) if "LSHIFT" in inp else part1(part1, gates, inp[0]) >> part1(part1, gates, inp[2]) if "RSHIFT" in inp else part1(part1, gates, inp[0]))(gates[wire][1]))[0])(gates, letter), {gate.split(" -> ")[1]: [-1, gate.split(" -> ")[0].split()] for gate in open("Day7.txt").read().split("\n")}), sep = "\n")