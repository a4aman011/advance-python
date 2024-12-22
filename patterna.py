rows = 7
for i in range(rows):
    for j in range(2 * rows - 1):
        if j == rows - i - 1 or j == rows + i - 1 or (i == rows // 2 and rows - i - 1 < j < rows + i - 1):
            print("A", end="")
        else:
            print(" ", end="")
    print()
