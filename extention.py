# Accept filename from user
filename = input("Input the filename: ")

# Find the last occurrence of a period in the filename
last_dot_index = filename.rfind(".")

# Extract the extension
extension = filename[last_dot_index+1:]

# Print the extension
print("The extension of the file is:", extension)
