print(*(lambda time, bus_ids: ((lambda earliest_bus: earliest_bus[0] * earliest_bus[1])(sorted([(bus_id[0] - (time % bus_id[0]), bus_id[0]) for bus_id in bus_ids if bus_id != "x"])[0]), (lambda bus_ids, sum_ids: sum(((bus_id - ind) % bus_id) * sum_ids // bus_id * ((sum_ids // bus_id) ** (bus_id - 2) % bus_id) for bus_id, ind in bus_ids) % sum_ids)(bus_ids, __import__("functools").reduce(int.__mul__, [bus_id[0] for bus_id in bus_ids]))))(*(lambda data: (int(data[0]), [(int(bus_id), ind) for ind, bus_id in enumerate(data[1].split(",")) if bus_id != "x"]))(open("Day13.txt").read().split("\n"))), sep = "\n") # Chinese Remainder Theorem