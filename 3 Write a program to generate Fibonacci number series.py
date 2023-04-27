num_terms = int(input("Enter the number of terms: "))
first_term = 0
second_term = 1
print("Fibonacci series:")
for i in range(num_terms):
    print(first_term, end=" ")
    temp = first_term + second_term
    first_term = second_term
    second_term = temp
