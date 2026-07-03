set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union (All unique items from both sets)
print(set_a | set_b)          
print(set_a.union(set_b))     

# Intersection (Items present in both sets)
print(set_a & set_b)          
print(set_a.intersection(set_b))

# Difference (Items in A but not in B)
print(set_a - set_b)          
print(set_a.difference(set_b))

# Symmetric Difference (Items in either A or B, but NOT both)
print(set_a ^ set_b)          
