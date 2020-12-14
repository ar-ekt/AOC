print(*(lambda data: (data.count('(') - data.count(')'), [i+1 for i in range(len(data)) if data[:i+1].count('(') - data[:i+1].count(')') == -1][0]))(open('Day1.txt').read()), sep = "\n")
