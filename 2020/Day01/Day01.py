print(*(lambda array: (*(array[ind1] * array[ind2] for ind1 in range(len(array)) for ind2 in range(ind1+1, len(array)) if array[ind1] + array[ind2] == 2020), *(array[i] * array[ind2] * array[k] for i in range(len(array)) for ind2 in range(i+1, len(array)) for k in range(ind2+1, len(array)) if array[i] + array[ind2] + array[k] == 2020)))(list(map(int, open("Day1.txt").read().split("\n")))), sep = "\n")