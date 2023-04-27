set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
def common_elements(set1, set2):
    return set1.intersection(set2)
result = common_elements(set1, set2)
print("Common elements:", result)
