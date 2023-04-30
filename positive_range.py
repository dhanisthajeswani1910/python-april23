# Accept the range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Print all positive numbers in the range
print("Positive numbers in the range", start, "to", end, "are:")
for i in range(start, end+1):
    if i > 0:
        print(i)
