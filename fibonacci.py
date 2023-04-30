# Accept the number of terms to be printed
nterms = int(input("Enter the number of terms: "))

# Initialize the first two terms of the sequence
n1, n2 = 0, 1

# Check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence up to", nterms, ":")
   print(n1)
else:
   print("Fibonacci sequence:")
   count = 0
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # Update the values of n1 and n2 for the next term
       n1 = n2
       n2 = nth
       count += 1
