pattern = int(input("Enter the side length of the square:"))

rows = 0

while rows < pattern:
    for col in range(pattern):
        print("*", end=' ')


    print()

    rows += 1