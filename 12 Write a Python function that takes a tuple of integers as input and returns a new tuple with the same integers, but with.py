def square_tuple(tup):
 
    squared_list = []
    
    # Square each integer in the input tuple and append to the squared_list
    for num in tup:
        squared_list.append(num**2)
    

    return tuple(squared_list)


my_tuple = (1, 2, 3, 4, 5)
squared_tuple = square_tuple(my_tuple)
print(squared_tuple)
