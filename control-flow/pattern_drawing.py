# pattern_drawing.py

size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:  # outer while loop for rows
    for col in range(size):  # inner for loop for columns
        print("*", end="")  # ✅ required pattern (no newline between stars)
    print()  # move to the next line after each row
    row += 1