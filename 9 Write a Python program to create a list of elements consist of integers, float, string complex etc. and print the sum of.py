my_list = [1, 2.5, "3", 4+5j, 6, "7", 8.5, 9]
int_sum = 0
for elem in my_list:
    # Check if the element is an integer
    if isinstance(elem, int):
        # If the element is an integer, add it to the int_sum variable
        int_sum += elem
print("Sum of all integers in the list:", int_sum)
